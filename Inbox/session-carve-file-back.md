---
created: 2026-07-20 15:07
updated: 2026-07-20 15:07
tags: []
type: reference
lang: en
status: draft
---
Because the file is split across three separate session logs in Arkime, the absolute best approach is to let Arkime handle the reassembly first, and then use standard forensic tools to carve out the payload.

Here is the most efficient, step-by-step workflow to get that file back.

### Step 1: Export a Unified PCAP from Arkime

Do not download three separate PCAP files. Arkime allows you to stitch them together automatically.

1. In your Arkime viewer, **check the selection boxes** on the far left for all three of these sessions.
    
2. Click the **Actions** button (usually a green or blue dropdown menu near the top left of the query bar).
    
3. Select **Export PCAP**.
    
4. Arkime will merge the packets in chronological order and download a single, continuous PCAP file to your machine.
    

### Step 2: Carve the File (Choose Your Tool)

Depending on what tools you prefer, choose one of the options below to extract the data from your new unified PCAP.

#### Option A: The Automated Command-Line Way (`tcpflow`)

If you are on Linux or macOS, `tcpflow` is the quickest way to reconstruct TCP streams without opening a GUI. It automatically strips away TCP headers and handles reordering.

1. Run the following command in your terminal:
    
    Bash
    
    ```
    tcpflow -r unified_capture.pcap -o output_directory/
    ```
    
2. Look inside the `output_directory`. You will find a file named something like `192.168.065.069.54583-010.099.040.020.00080`.
    
3. This file contains the entire raw HTTP POST request, including the file data.
    

#### Option B: The GUI Way (Wireshark)

If you prefer a visual approach, Wireshark can easily isolate the payload.

1. Open your unified PCAP in Wireshark.
    
2. Right-click on the very first packet (the one containing the HTTP `POST` request) and select **Follow -> TCP Stream**.
    
3. A window will pop up showing the entire conversation.
    
4. At the bottom of the window, change the drop-down menu that says **"Entire Conversation"** to show **only the traffic from the client to the server** (`192.168.65.69 -> 10.99.40.20`).
    
5. Change the display format from **ASCII** to **Raw**.
    
6. Click **Save as...** and name your file (e.g., `extracted_upload.bin`).
    

### Step 3: Clean Up the File (Crucial Step)

Because this was an HTTP `POST` request to `/file/upload`, the data you just saved isn't _just_ the raw file. It will be wrapped in HTTP protocol headers.

If you open your extracted file in a hex editor (like CyberChef or VS Code with a hex extension), you will see something like this at the very beginning:

Plaintext

```
POST /file/upload HTTP/1.1
Host: 10.99.40.20
User-Agent: curl/7.85.0
Content-Type: multipart/form-data; boundary=------------------------abcdef1234
...
--------------------------abcdef1234
Content-Disposition: form-data; name="file"; filename="important_data.zip"
Content-Type: application/zip

[REAL FILE BINARY DATA STARTS HERE]
```

1. **Identify the File Type:** Look at the `Content-Type` header in that text block to see what kind of file was uploaded (e.g., `application/zip`, `image/png`, `application/octet-stream`).
    
2. **Trim the Garbage:**
    
    - If you are using **CyberChef**, use the **"Strip HTTP Header"** recipe, or manually use the **"Drop bytes"** tool to delete everything from the `POST` command down to the very first byte of the actual file.
        
    - Don't forget to scroll to the very bottom of the file and delete the trailing MIME boundary marker (e.g., `--------------------------abcdef1234--`).
        
3. **Save:** Save the cleaned binary with its correct extension.
    

Do you suspect the uploaded file might be malicious (like a reverse shell or a script), or are you more concerned that this was an exfiltration event involving sensitive company data?

---

When you save a raw TCP stream from an HTTP `POST` upload, the actual file is sandwiched inside a text-based HTTP protocol wrapper.

The data layout in your `uploaded_data.bin` looks exactly like this:

Plaintext

```
[HTTP Headers (Text)]
\r\n\r\n
[Multipart Boundary Marker (Text)]
Content-Disposition: ... filename="secret.zip"
Content-Type: application/zip
\r\n\r\n
[THE ACTUAL BINARY FILE DATA]
\r\n\r\n
[Trailing Multipart Boundary Marker--]
```

To get a functional file, you must cleanly slice away the headers at the top and the boundary marker at the bottom. Here are three different ways to do it, ranging from fully automated Linux utilities to manual precision slicing.

### Approach 1: The Automated Linux Way (`binwalk`)

If you are on Linux, don't do the math yourself if you don't have to. Linux has an incredible firmware analysis and carving tool called `binwalk` that scans files for known signatures (magic bytes) and extracts them automatically.

1. **Install it** (if you don't have it):
    
    Bash
    
    ```
    sudo apt install binwalk   # Debian/Ubuntu
    sudo dnf install binwalk   # RHEL/CentOS
    ```
    
2. **Scan the raw file:**
    
    Bash
    
    ```
    binwalk uploaded_data.bin
    ```
    
    _This will output a list of what it found and the exact decimal byte offset where the real file (like a ZIP or PNG) begins._
    
3. **Carve it automatically:**
    
    Bash
    
    ```
    binwalk -e uploaded_data.bin
    ```
    
    `binwalk` will create a new directory (e.g., `_uploaded_data.bin.extracted/`) and cleanly extract just the inner payload, completely ignoring the HTTP headers and trailing boundaries.
    

### Approach 2: The Precise Linux CLI Way (`grep` + `dd`)

If `binwalk` doesn't recognize the file type (e.g., it's an obscure or proprietary data format), you can manually carve it using standard Linux core utilities.

To do this, we look for the **Magic Bytes** (file signatures) of the expected file type. For example, if the `Content-Type` header said it was a ZIP file, the magic bytes are `PK` (hex: `50 4b 03 04`).

1. **Find the exact byte offset where the file starts:**
    
    Bash
    
    ```
    grep -a -b -o "PK" uploaded_data.bin
    ```
    
    - `-a` treats the binary file as text.
        
    - `-b` prints the **0-based byte offset**.
        
    - `-o` prints only the matching part.
        
    
    _Example output:_ `245:PK` (This means your actual ZIP file starts exactly at byte 245).
    
2. **Use `dd` to slice the header off:**
    
    Bash
    
    ```
    dd ibs=1 skip=245 if=uploaded_data.bin of=cleaned_file.zip
    ```
    
    _(Replace `245` with the number your grep query returned)._
    

> **Note on the trailing footer:** Most modern file parsers (like ZIP extractors, PDF readers, and image viewers) read files from the header onward based on internal size definitions. They will completely ignore any trailing HTTP boundary garbage left at the end of the file, so you rarely need to waste time trimming the bottom!

### Approach 3: The CyberChef Way (Visual & Web-Based)

If you prefer a web GUI or are working from a machine without Linux utilities, **CyberChef** (the Swiss Army knife of security analysts) handles this brilliantly.

1. Open CyberChef and drag your `uploaded_data.bin` into the **Input** box.
    
2. In the Operations search bar, search for **"Strip HTTP Header"** and drag it into the Recipe flow. _(This cleanly removes the top layer of HTTP request headers)._
    
3. If it was a multipart upload, you will still see the form boundary text. Search for **"Drop bytes"** and add it to your recipe.
    
4. Adjust the **Length** value in the Drop Bytes tool until the very first bytes in your **Output** window match your file's signature (e.g., you see `PK` for a zip, or `‰PNG` for an image).
    
5. Click the **Save** icon (floppy disk) at the bottom right of the Output pane to download your clean file.
    

Based on the headers we saw in your earlier screenshot, do you happen to know what type of file extension this `curl` command was trying to upload?
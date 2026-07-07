---
created: 2026-05-13
tags: [dev, environment, obsidian]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[My Stack]] · [[CLAUDE]]

### 1. The "Agentic" Upgrade (Beyond VS Code)

While VS Code is great, the current standard for AI researchers and devs has shifted toward **Agentic IDEs** that understand entire codebases rather than just the file you’re typing in.

* **Cursor / Windsurf:** These are forks of VS Code built with AI as a first-class citizen. They are significantly better at "reasoning" through complex AI research code or finding security flaws in your logic.
* **Zed:** If you value speed above all else. It's written in Rust and is incredibly fast, which is great for when you're jumping through large datasets or massive log files.

### 2. The C & Low-Level Stack

For cybersecurity and AI (especially performance-critical kernels), a robust C environment is essential.

* **Compilers:** Install the `build-essential` package in WSL (Kali/Ubuntu) for `gcc` and `g++`. For Windows-native C, **LLVM/Clang** is often preferred over MinGW in 2026 for its superior error messages and cross-compilation support.
* **CMake & Ninja:** Essential for managing complex C/C++ builds in AI libraries (like custom PyTorch operators).
* **GDB + GEF/Pwnbg:** Since you're in cybersecurity, don't just use standard GDB. Install the **GEF (GDB Enhanced Features)** or **Pwnbg** plugin inside your Kali WSL. It makes exploit development and memory analysis much more visual.
```powershell
winget install LLVM.LLVM --source winget
clang --version
```
```bash
# In WSL (Kali/Ubuntu)
sudo apt update && sudo apt install -y build-essential cmake clang gdb git curl wget docker.io
# sudo apt update && sudo apt install -y build-essential cmake clang lldb gdb python3-dev libssl-dev
ggc --verison
sh -c "$(curl -fsSL https://raw.githubusercontent.com/hugsy/gef/main/scripts/gef.sh)" # Install GEF for GDB

```

### 3. AI Research Essentials

* **Conda / Mamba:** Don't rely solely on system Python. Use **Micromamba** (the faster, C++ version of Conda) to manage environments. It’s crucial for keeping your "Stable Diffusion" environment separate from your "Transformer" or "Security Scripting" environments.
* **Docker Desktop:** Essential for "containerizing" AI models or vulnerable apps you want to pentest without messing up your host OS.
* **Hugging Face CLI:** For quickly pulling models and managing your local cache.

### 4. Cybersecurity Toolkit (Host Side)

Since you already have Kali in WSL, use your host OS (Windows/Mac) for the "clean" analysis tools:

* **Burp Suite (Community/Pro):** The gold standard for web analysis.
* **Wireshark:** Install this on the host (Windows) to capture traffic more reliably than inside WSL.
* **Ghidra:** The NSA’s open-source reverse engineering tool. Essential for malware analysis and understanding how those C programs you're writing actually look in assembly.
* **Obsidian:** High-level researchers use this for "Second Brain" note-taking. With the **Canvas** feature, it’s perfect for mapping out attack surfaces or neural network architectures.

### 5. Essential Utilities

* **Windows Terminal (Preview):** If you're on Windows, use the Preview version for better multiplexing (splitting screens between your Python logs and your Kali listener).
* **PowerToys:** Use "FancyZones" to snap your windows into a grid (e.g., Code on the left, Terminal on the bottom right, Research paper on the top right).
* **Insomnia / Postman:** For testing APIs (both for AI endpoints and searching for vulnerabilities).

---

- git, vscode (extension), [MSVC(visual studio), MinGW(GCC for Windows)], python


---

Since you've successfully installed LLVM via `winget`, you now have one of the most powerful compiler toolchains at your disposal. Let's get it verified and hooked into VS Code so you can stop worrying about "Developer Environments" and start coding.

### Step 1: Verify the Installation

First, ensure Windows actually "sees" the new compiler. Open a **new** PowerShell or Command Prompt window (this is important to refresh your Environment Variables) and run:

```powershell
clang --version

```

If it returns `clang version 22.1.5` (or similar), you are good to go. If it says "command not found," you may need to restart your PC or manually add `C:\Program Files\LLVM\bin` to your System PATH.

---

### Step 2: Configure VS Code for Clang

To implement **Option B**, follow these precise steps to swap from the "failing" MSVC to the "working" Clang:

#### 1. Select the IntelliSense Configuration

* In VS Code, press `Ctrl + Shift + P`.
* Search for **"C/C++: Select IntelliSense Configuration..."**
* Choose **"Use clang++.exe"** (or `clang.exe` if you are writing pure C).
* *This stops the red squiggly lines from complaining about Windows-specific headers.*

#### 2. Update `tasks.json` (The "Build" step)

This is what actually compiles your code when you hit "Build" or "Run."

* Press `Ctrl + Shift + P` and type **"Tasks: Configure Default Build Task"**.
* Select **"C/C++: clang++.exe build active file"**.
* VS Code will generate/open a `tasks.json` file. Ensure the `command` line looks like this:
* `"command": "C:\\Program Files\\LLVM\\bin\\clang++.exe"` (or simply `"clang++"`)



#### 3. Update `launch.json` (The "Debug" step)

This connects the debugger so you can set breakpoints.

* Go to the **Run and Debug** tab (Ctrl+Shift+D) and click **"create a launch.json file"** if you don't have one.
* In the configuration block, ensure the `externalConsole` is `false` and the `MIMode` is set to **`lldb`** or **`gdb`**.
> **Note:** Since you installed LLVM, you should use **`lldb`** as your debugger. It is the natural companion to Clang.



---

### Step 3: The "Hello World" Test

Let's make sure the hand-shake is working. Create a file named `test.cpp`:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> msg {"Clang", "is", "working!"};
    for (const std::string& word : msg) {
        std::cout << word << " ";
    }
    return 0;
}

```

1. Press `Ctrl + Shift + B` to build.
2. If it builds successfully, run it by typing `./test.exe` in your terminal.

### Why this is better for you:

As a **Cybersecurity Analyst**, you can now use Clang's **AddressSanitizer**. Try adding `-fsanitize=address` to your `args` in `tasks.json`. If you write code that overruns a buffer, Clang will give you a detailed report of exactly where the memory corruption happened—MSVC won't do that nearly as clearly.

Are you planning to dive into **Reverse Engineering** with this setup, or is your C focus mainly on building high-performance **AI kernels**?
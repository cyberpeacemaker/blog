The Librem 5 is a fantastic device for privacy and open-source enthusiasts, but it runs PureOS (a Linux distribution), not Android. Because of this, you cannot run Android apps natively right out of the box.

However, you can absolutely run Android apps using a containerized compatibility layer. The current and best standard for this is **Waydroid** (which has largely replaced the older Anbox system). Waydroid allows Android apps to run directly on the Linux kernel with near-native performance.

Here is the straightforward guide on how to get Android apps running on your Librem 5.

---

### 1. Install Waydroid

Purism has been working on integrating Waydroid into PureOS, meaning you can install it directly from your terminal.

1. Open the **Terminal** app on your Librem 5.
2. Update your package list to ensure you are pulling the latest software:
`sudo apt update`
3. Upgrade your system (always a good practice before installing new core software):
`sudo apt full-upgrade`
4. Install Waydroid:
`sudo apt install waydroid`

> **Note:** The first time you launch Waydroid, it will take a while to initialize and boot up the Android container. You must have an active internet connection for this first run so it can download the necessary images.

---

### 2. Launching and Using Waydroid

Once installed, you should see a **Waydroid** icon in your app drawer. Tap it to launch the Android environment.

* **Window Sizing:** When launching an Android app, make sure your on-screen keyboard is minimized first. Otherwise, the Android app might scale incorrectly and only occupy the top half of your screen.
* **Performance:** Most standard apps work remarkably well, but keep in mind that hardware-intensive apps (like heavy 3D games) or apps requiring deep hardware hooks (like certain banking apps) might struggle or fail to run.

---

### 3. Installing Android Apps

Waydroid does **not** come with Google Play Services installed out of the box for privacy and compatibility reasons. To get your Android apps, you will need to use alternative app stores within the Waydroid environment:

* **F-Droid:** The best choice for free and open-source Android apps. You can download the F-Droid APK directly from your browser inside Waydroid and install it.
* **Aurora Store:** If you need specific apps that are only available on the Google Play Store (like WhatsApp or Spotify), use the Aurora Store. It allows you to download apps anonymously directly from Google's servers without needing a Google account or Play Services running on your phone. You can download Aurora Store via F-Droid.

### 4. A Quick Caveat on Integration

While Waydroid is excellent, it operates in an isolated container. This means that things like your Librem 5's clipboard might not seamlessly sync with the Android clipboard. If you need to move files between your Linux host and the Android container, using a cloud service like Nextcloud is currently the most frictionless workaround.

---

Ah, that classic Linux headache! Don't worry, this just means your Librem 5's package manager doesn't know where to look for Waydroid yet.

Because PureOS is a strict, fully free-software distribution, Waydroid isn't sitting in the default out-of-the-box repository. Furthermore, Waydroid's official automated installation script doesn't natively recognize the name "PureOS." We have to manually point your phone to the Waydroid servers and tell it which underlying Debian version PureOS is based on.

Here is how to bypass that error and get it installed.

---

### 1. Identify Your PureOS Version

Most Librem 5s run PureOS **Byzantium** (which is built on Debian Bullseye). If you recently upgraded to the bleeding-edge release, you might be on PureOS **Crimson** (built on Debian Bookworm).

### 2. Add the Waydroid Repository

Open your **Terminal** app again and run the following commands.

First, make sure you have `curl` installed so your phone can download the repository data:
`sudo apt install curl`

Next, add the official Waydroid repository.
**If you are on Byzantium (most likely):**
`curl https://repo.waydro.id | sudo bash -s bullseye`

**If you are on Crimson:**
`curl https://repo.waydro.id | sudo bash -s bookworm`

> **What this does:** It fetches the software repository list from Waydroid's servers and the `-s` flag forces it to use the Debian branch that matches your system, completely bypassing the OS name confusion.

### 3. Install the Package

Once that script finishes running and updates your sources, your package manager will know exactly where Waydroid is. You can now run the installation command successfully:

`sudo apt install waydroid`

After that finishes, you should see the Waydroid app icon appear in your app drawer, and you can tap it to initialize your Android environment!

---

That is a perfectly valid question. It is always better to check exactly what system you are running rather than guessing and messing up your software repositories.

Since PureOS doesn't always broadcast its version name on the home screen, you can ask your phone directly using the terminal.

### How to Check Your PureOS Version

1. Open your **Terminal** app.
2. Type the following command and press Enter:
`cat /etc/os-release`

This command tells the terminal to print out the file that contains your operating system's identity information.

### What to Look For

You will see a list of data appear on the screen. Look for the line that says **`VERSION_CODENAME=`** or **`VERSION=`**.

* If it says **`byzantium`**: You are on the stable branch (based on Debian Bullseye). You will use the `bullseye` command from the previous step.
* If it says **`crimson`**: You are on the newer branch (based on Debian Bookworm). You will use the `bookworm` command from the previous step.

Once you confirm that, you can confidently run the correct `curl` command to get Waydroid installed!
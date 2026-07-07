---
created: 2026-05-28
tags: [personal]
type: reference
lang: en
status: draft
---

Since the Librem 5 runs a native desktop Linux operating system (PureOS) rather than Android, it cannot run Android applications directly out of the box.

To make this happen, the standard and most efficient way is to use **Waydroid**. It runs a full, containerized Android system directly on top of your Linux kernel, giving you near-native performance without the heavy resource drain of a traditional emulator.

Here is the exact workflow to get it running and start downloading apps:

## 1. Install Waydroid

First, you need to download and install the mobile-optimized Waydroid package for PureOS.

1. **Update system packages:** Requires terminal.
Open your terminal emulator and pull the latest system updates to make sure your package manager is ready:

```bash
sudo apt update && sudo apt full-upgrade

```


2. **Download the Librem 5 Waydroid package:** Fetch official CI artifact.
Purism maintains custom builds for the Librem 5. You can pull the package directly using `wget`:

```bash
wget https://source.puri.sm/Librem5/debs/waydroid/-/jobs/401129/artifacts/file/debian/output/waydroid_1.3.3-0pureos0+librem5ci79377.0353512_all.deb

```


3. **Install the package:** Handle local dependencies.
Use `apt` to install the local `.deb` file you just downloaded so it automatically grabs any underlying software it needs:

```bash
sudo apt install ./waydroid_1.3.3-0pureos0+librem5ci79377.0353512_all.deb

```


4. **Reboot your phone:** Finalize configuration.
Restart the Librem 5 to let the container hooks properly register with the system.


---

## 2. Initialize the Android Image

Once your phone boots back up, look for the **Waydroid** icon in your application drawer.

1. **Launch Waydroid:** Tapping the icon opens an initialization window asking you to download an Android system image.
2. **Choose your flavor:**
* **VANILLA:** A completely clean, open-source Android build with zero Google services.
* **GAPPS:** Includes Google Play Services. *(Note: If you choose GAPPS, you will need to manually register your Android device ID with Google to use the official Play Store).*


3. **Download:** Hit the download button, wait for it to extract, and tap **Done**.

The Android environment will now spin up in the background. *(Tip: Make sure to minimize or hide your virtual keyboard when first launching so Waydroid maps correctly to your full screen real estate).*

---

## 3. How to Download Apps Inside Waydroid

Because you are on a privacy-centric device, standard Google Play store usage can sometimes be limiting or go against the purpose of the hardware. Instead, you have a few practical ways to source your apps:

* **F-Droid:** If you chose the Vanilla image, your first step should be opening the Android browser, heading to the official F-Droid website, and downloading their APK. It is a brilliant repository of open-source, tracker-free Android apps.
* **Aurora Store:** If you need mainstream apps (like banking, transit, or proprietary messengers) but don't want to sign in with a tracking-heavy Google account, install the Aurora Store client via F-Droid. It acts as an anonymous frontend to the Google Play Store.
* **Manual APK sideloading:** You can download `.apk` files directly from trusted mirrors (like APKPure or APKMirror) through your host Linux browser, then push them straight into the running Waydroid container using the Linux terminal:
```bash

```



waydroid app install /path/to/downloaded_app.apk

```

> ⚠️ **A quick heads-up on hardware limits:** While app performance is smooth, Waydroid runs inside an isolated container. This means certain hardware pass-through functions—like giving an Android app direct access to your phone's native GPS, camera, or cell modem—can still be hit-or-miss depending on ongoing community driver updates.

<ElicitationsGroup message="Depending on what apps you need to run:">

  <Elicitation label="Configure display scaling for Android apps" query="How do I adjust the display resolution and scale settings for Waydroid on the Librem 5 so text isn't too small?"/>
  <Elicitation label="Fix Google Play Protect certification errors" query="How do I register my Waydroid device ID with Google to fix Device is not Play Protect certified errors?"/>
</ElicitationsGroup>

```
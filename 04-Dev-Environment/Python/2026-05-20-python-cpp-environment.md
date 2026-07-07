---
created: 2026-05-20
tags: [dev, python]
type: reference
lang: en
status: draft
---

Ah, the plot thickens! Welcome to the final boss of Windows Python development: **Compiling C/C++ dependencies from source.**

### What Went Wrong

Your terminal downloaded a source file (`pandas-2.1.1.tar.gz`) instead of a pre-built package. Because it’s a raw code file, Python tried to compile it on your computer using a build system called Meson. Meson started looking around for Microsoft Visual Studio using a tool called `vswhere.exe`, got totally confused, and crashed because you don't have the heavy-duty C++ development tools installed on your system.

**Why did this happen?** Normally, `pip` downloads pre-compiled versions called "wheels" (`.whl`). It only falls back to raw source compilation if it can't find a wheel that matches your exact setup. This usually happens for one of three reasons:

1. Your version of `pip` is outdated and doesn't know how to look for the right wheel.
2. You are using a **32-bit version of Python** (Pandas dropped 32-bit precompiled wheels starting with version 2.1.1).
3. You are using a brand new version of Python (like Python 3.13), but trying to install an older version of Pandas (2.1.1) that doesn't have a pre-built wheel for that new Python version.

---

### How to Fix It (Ranked from Easiest to Hardest)

#### Option 1: Upgrade your core installer tools (Try this first!)

Sometimes your virtual environment's internal tools just need an update to recognize the right pre-compiled binary packages.

Run this command in your terminal:

```powershell
python -m pip install --upgrade pip setuptools wheel

```

After that completes, try running your original installation command again:

```powershell
pip install -r .\requirements.txt

```

#### Option 2: Loosen the Pandas version lock

If your Python version is too new for Pandas 2.1.1, telling `pip` to grab a newer version of Pandas will allow it to find a pre-compiled wheel.

1. Open `requirements.txt`.
2. Change `pandas==2.1.1` to either **`pandas>=2.1.1`** or just **`pandas`**.
3. Save the file and re-run:
```powershell
pip install -r .\requirements.txt

```



#### Option 3: Check your Python architecture (Crucial for Windows)

If the steps above still fail, let’s verify whether you accidentally installed 32-bit Python. Run this quick test in your terminal:

```powershell
python -c "import platform; print(platform.architecture()[0])"

```

* **If it prints `32bit`:** This is your culprit. Pandas 2.1.1 requires a backend that does not support 32-bit Windows. Your best bet here is to change your `requirements.txt` to use an older version of pandas that still supported 32-bit:
```text
pandas==2.0.3

```


*(Alternatively, you would need to uninstall Python and reinstall the 64-bit version).*
* **If it prints `64bit`:** Option 1 or 2 will definitely bypass the compilation error!
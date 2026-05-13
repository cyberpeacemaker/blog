### 1. The "Agentic" Upgrade (Beyond VS Code)

While VS Code is great, the current standard for AI researchers and devs has shifted toward **Agentic IDEs** that understand entire codebases rather than just the file you’re typing in.

* **Cursor / Windsurf:** These are forks of VS Code built with AI as a first-class citizen. They are significantly better at "reasoning" through complex AI research code or finding security flaws in your logic.
* **Zed:** If you value speed above all else. It's written in Rust and is incredibly fast, which is great for when you're jumping through large datasets or massive log files.

### 2. The C & Low-Level Stack

For cybersecurity and AI (especially performance-critical kernels), a robust C environment is essential.

* **Compilers:** Install the `build-essential` package in WSL (Kali/Ubuntu) for `gcc` and `g++`. For Windows-native C, **LLVM/Clang** is often preferred over MinGW in 2026 for its superior error messages and cross-compilation support.
* **CMake & Ninja:** Essential for managing complex C/C++ builds in AI libraries (like custom PyTorch operators).
* **GDB + GEF/Pwnbg:** Since you're in cybersecurity, don't just use standard GDB. Install the **GEF (GDB Enhanced Features)** or **Pwnbg** plugin inside your Kali WSL. It makes exploit development and memory analysis much more visual.

```bash
# In WSL (Kali/Ubuntu)
sudo apt update && sudo apt install -y build-essential cmake clang gdb git curl wget docker.io
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

- git, vscode (gitlens), pythons


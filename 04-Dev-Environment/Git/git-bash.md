---
created: 2026-05-21
tags: [dev, git]
type: reference
lang: en
status: draft
---

### Method 1: Using Git Bash (Recommended)

Since you are working inside a GitHub repository (`Malcolm_BEC`), you likely have **Git Bash** installed.

1. Open **Git Bash** on your computer.
2. Copy the **entire block of code** you provided exactly as it is.
3. Paste it directly into the Git Bash window and press **Enter**.

> 💡 *Note: Git Bash will handle the `cd c:\Users\...` path and cleanly feed the Python script directly into the Python interpreter line-by-line via that `EOF` tag.*

---

### Method 2: The Bulletproof Way (Any Terminal / VS Code)

If you are using the standard Windows Command Prompt, PowerShell, or the built-in terminal in VS Code, the `<< 'EOF'` trick will throw a syntax error. Instead, do it the traditional way:

#### Step 1: Navigate to your repository

Open your terminal (CMD or PowerShell) and run just the first part:

```cmd
cd c:\Users\ydnaa\Documents\Github\Malcolm_BEC

```

#### Step 2: Run the script via a temporary file

Instead of pasting the code directly into the command line, save it to a file.

1. Create a new file in that folder named `setup.py`.
2. Paste the Python code inside it:

```python
import os
import shutil
from pathlib import Path

repo_root = Path(".")
changes = []

# Define the required folder structure
required_dirs = [
    "config",
    "scripts",
    "notebooks", 
    "rules",
    "workflows",
    "data/raw",
    "data/processed",
    "data/reports",
    "docs"
]

# Create all required directories
for dir_path in required_dirs:
    full_path = repo_root / dir_path
    full_path.mkdir(parents=True, exist_ok=True)
    changes.append(f"✓ Created: {dir_path}")

print("=" * 60)
print("DIRECTORY STRUCTURE SETUP")
print("=" * 60)

# List current structure
print("\nCurrent structure created:")
for d in sorted(required_dirs):
    print(f"  ✓ {d}")

```

3. In your terminal, run the file:

```cmd
python setup.py

```

4. Feel free to delete `setup.py` when you are done!

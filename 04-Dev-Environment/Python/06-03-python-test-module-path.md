This is a classic—and incredibly frustrating—Python quirk! You definitely have a `scripts` folder, but Python is looking in the wrong place for it.

Here is exactly why this happens and how to fix it.

### Why This is Happening

When you run a Python file directly using `python .\tests\test_arkime_queries.py`, Python automatically sets the starting point for all its imports to **the folder where the script lives** (in this case, the `tests` folder).

It doesn't look at your current working directory (`Malcolm_BEC`). Because there is no `scripts` folder *inside* the `tests` folder, Python throws a `ModuleNotFoundError`.

---

### How to Fix It

Here are the best ways to fix this, ranked from easiest to most robust:

#### 1. The Easiest Fix: Use the `-m` flag (Run as a module)

Instead of running it as a file, run it as a module from your root directory. This tells Python to include your root `Malcolm_BEC` folder in its search path.

Run this exactly as written from your `Malcolm_BEC` folder:

```powershell
python -m tests.test_arkime_queries

```

*(Notice we drop the `.py` extension and the slashes become dots).*

#### 2. The Best Practice Fix: Use `pytest`

Since this is a test file, it's highly recommended to use a testing framework like `pytest`. Pytest is smart enough to automatically fix these path issues for you.

If you don't have it installed, run:

```powershell
pip install pytest

```

Then, just run the file like this:

```powershell
pytest .\tests\test_arkime_queries.py

```

#### 3. The Code Fix: Modify `sys.path` (The "Hack")

If you absolutely must run the script using `python .\tests\test_arkime_queries.py`, you have to manually tell Python to look one folder up. You can do this by adding these three lines to the **very top** of `test_arkime_queries.py` (before your `scripts` import):

```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils.arkime_queries import ( ... )

```

**Recommendation:** Stick to **Option 1** or **Option 2**. Modifying `sys.path` directly (Option 3) works, but it can make your code messy and harder to maintain long-term.
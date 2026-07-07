---
created: 2026-06-03
tags: [dev]
type: reference
lang: en
status: draft
---

If you are moving away from older files like `setup.py`, `setup.cfg`, or scattering settings across multiple configuration files, `pyproject.toml` is exactly what you need.

It is the modern, standardized way to configure Python projects. Instead of having one file for your build, one for your dependencies, and five different files for your formatting and testing tools, you put almost everything in `pyproject.toml`.

Here is a straightforward tutorial on how it works and how to set one up.

---

### 1. The Three Main Sections

A typical `pyproject.toml` file is broken down into three primary sections:

* **`[build-system]`**: Tells Python *how* to build your package (e.g., using Setuptools, Poetry, Hatch, or Flit).
* **`[project]`**: Contains your project's metadata (name, version, authors, dependencies).
* **`[tool.*]`**: Contains configurations for third-party tools (like the `pytest` config you were looking at earlier, or tools like Black, Ruff, and MyPy).

### 2. Step-by-Step Example

Let's build a clean, standard `pyproject.toml` file for a hypothetical project called `my_awesome_app`.

#### Step A: Define the Build System

Every `pyproject.toml` needs to tell Python what backend to use. We will use **Setuptools**, as it is the most common standard.

```toml
[build-system]
# This tells pip what libraries are needed to even begin building your app.
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

```

#### Step B: Define the Project Metadata

This replaces the old `setup() ` function in `setup.py`. It holds all your vital stats and dependencies. Notice how we use the `>=` bounds we discussed earlier for dependencies.

```toml
[project]
name = "my_awesome_app"
version = "1.0.0"
description = "A really great Python application."
readme = "README.md"
requires-python = ">=3.9"
authors = [
    { name = "Your Name", email = "you@example.com" }
]

# These are your production dependencies (replaces requirements.txt)
dependencies = [
    "requests>=2.28.0,<3.0.0",
    "opensearch-py>=2.3.1,<3.0.0" 
]

```

#### Step C: Add Optional Dependencies (like for testing)

You often need different packages for local development than you do for production.

```toml
[project.optional-dependencies]
# Install these by running: pip install .[dev]
dev = [
    "pytest>=7.0",
    "black>=23.0"
]

```

#### Step D: Configure Your Tools

Instead of having a `pytest.ini` and a `.black` file, you dump their settings right here.

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]

[tool.black]
line-length = 88
target-version = ['py39']

```

---

### 3. How to Use It

Once you have this file in the root of your repository (next to your `src/` or script folders), you can run standard Python commands against it:

* **To install your project and its dependencies:** Run `pip install .`
* **To install it in "editable" mode for development:** Run `pip install -e .` (Changes to your code apply immediately without reinstalling).
* **To install with your dev tools (pytest, etc.):** Run `pip install -e .[dev]`

By adopting this file, you centralize your entire project setup, making it much easier for other developers (or future you) to understand what the project needs and how it behaves.

---

Whether this specific `pyproject.toml` block is "necessary" depends entirely on how your project is structured and what kind of feedback you want when running your tests.

Here is a breakdown of what each part does and how necessary it actually is:

### 1. `pythonpath = ["."]` (Likely Necessary)

**Verdict:** **Necessary** (unless you change how your project is installed).

As the comment in your snippet mentions, if your test files try to import modules from the root of your repository (like `import scripts.something`), `pytest` won't know where to find them by default. It usually only adds the `tests/` directory to your Python path. By adding `pythonpath = ["."]`, you are forcing `pytest` to recognize the root folder, preventing `ModuleNotFoundError`.

* *Alternative:* You could make this unnecessary by structuring your project as an installable package with a `src/` layout and running `pip install -e .` before testing, but keeping this line is the easiest fix for simple scripts.

### 2. `testpaths = ["tests"]` (Highly Recommended)

**Verdict:** **Optional, but a very good idea.**

This tells `pytest` exactly which folder to look in for your tests. If you remove it, `pytest` will scan your entire repository looking for anything that starts with `test_`. While it might still work without this line, specifying the directory speeds up the test collection process and prevents `pytest` from accidentally trying to run tests hiding inside your virtual environment (`venv/`), build folders, or random scripts.

### 3. The `log_cli` Settings (Purely Optional)

**Verdict:** **Not necessary at all.**

```toml
log_cli = true
log_cli_level = "INFO"
log_cli_format = "%(message)s"

```

These lines are purely for **Developer Experience (DX)**. They force `pytest` to print any `logging.info()` statements live to your console as the tests run. If you remove these lines, your tests will still run and pass/fail exactly the same way; you just won't see the live log outputs on your screen (unless a test fails, in which case `pytest` usually shows captured logs anyway).

---

**Summary:** If you want to clean up the file, you can safely delete the `log_cli` lines if you don't care about live console logging. However, you should definitely keep the `pythonpath` and `testpaths` lines to ensure your imports work and your tests are discovered efficiently.

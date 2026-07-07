---
created: 2026-05-21
tags: [dev, python]
type: reference
lang: en
status: draft
---

That line is easy to miss because it sits after the bootstrap block (lines 9–12), not with the logging / runpy / sys imports at the top.

Why imports are split this way
The file runs in two steps:

Bootstrap (lines 9–12) — runs _repo_path.py, which adds the repo root to sys.path:
"""Add repository root to sys.path for `python scripts/<name>.py` invocations."""
import sys
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
Project import (line 14) — from scripts.utils.bec_session import ... only works once the repo root is on sys.path. If that import were at the very top (before runpy.run_path(...)), running python scripts/test_opensearch.py would often fail with ModuleNotFoundError: No module named 'scripts'.
So the order is intentional: bootstrap first, then scripts.* imports.
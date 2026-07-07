---
created: 2026-05-20
tags: [dev, python]
type: reference
lang: en
status: draft
---

## 1. What does `venv` actually do?

Think of `python -m venv venv` as creating an **isolated sandbox** or a **private bubble** inside your `Malcolm_BEC` folder.

* **Without a venv:** If you install packages globally on Windows, every Python project on your machine shares the exact same folder. If Project A needs an old version of a library and Project B needs a new one, they will overwrite each other and cause a total system crash.
* **With a venv:** Running `venv\Scripts\activate` tells your terminal: *"For now, ignore the rest of the computer. Only look inside this private bubble."* All those packages we just fought to install (`pandas`, `numpy`, `opensearch-py`) are tucked safely inside that local `venv` folder. They won’t mess with your computer, and your computer won't mess with them.

---

## 2. Do I have to do something to leave here?

Yes, but it is incredibly simple. When you are done working on this project and want to pop the bubble to return your terminal to normal, just type a single word into PowerShell and press **Enter**:

```powershell
deactivate

```

You will notice that the green `(venv)` prefix at the beginning of your command line disappears. This means you have safely stepped out of the sandbox. (Whenever you want to come back and work on the project again, you just run `.\venv\Scripts\activate` to step back in).

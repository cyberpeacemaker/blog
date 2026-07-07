---
created: 2026-05-25
tags: [dev]
type: reference
lang: en
status: draft
---

Exactly right. You've hit on a fundamental difference between traditional Windows software and Node.js development tools.

When you run `npm init playwright@latest`, you are **not** installing a system-wide application like Microsoft Word or Google Chrome. Instead, the installation is split into two parts:

### 1. The Playwright Framework (Per Workspace)

The actual testing code, the commands, and the framework itself are installed **strictly inside that specific project folder**.

* They live inside a hidden folder called `node_modules` within your project.
* **Why this is great:** You can have Project A running an older version of Playwright and Project B running a brand new version of Playwright at the exact same time. They are completely isolated from each other. If you delete the project folder, the Playwright framework is gone with it.

### 2. The Playwright Browsers (Global Windows Cache)

There is one exception to the rule above. When Playwright downloads the actual web browsers it needs to run tests (custom versions of Chromium, Firefox, and WebKit), it **does** store those centrally on your Windows machine.

* By default, it puts them in your user profile (usually around `C:\Users\YourName\AppData\Local\ms-playwright`).
* **Why it does this:** Browsers are huge files. If you have 5 different Playwright projects, you don't want to download 5 separate copies of Chromium and fill up your hard drive. Playwright keeps them in a central cache so all your local projects can share them.

### Summary

Think of it this way: **The tools to write and run the tests are local to your workspace. The heavy browser engines they use to execute the tests are shared across your Windows user account to save disk space.** You won't see Playwright listed in your Windows "Add or Remove Programs" menu!
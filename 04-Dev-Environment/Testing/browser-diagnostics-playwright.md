---
title: "Browser Diagnostics with Playwright"
description: "Explains how Playwright dependencies and test viewer scripts support automated browser diagnostics."
created: 2026-07-18
updated: 2026-07-18
tags: [dev]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[playwright]] · [[browser-diagnostics]]

Moving from manual browser diagnostics to **Playwright** is like upgrading from a magnifying glass to a fully automated laboratory.

When you see a project utilizing Playwright as a `devDependency` alongside a custom script like `npm run test:viewer`, you are looking at an automated browser testing setup. Here is exactly what those two components mean and how they work together.

### 1. Playwright as a `devDependency`

Playwright is a modern framework developed by Microsoft for End-to-End (E2E) and component testing. It programmatically launches actual browsers (Chromium, Firefox, and WebKit) to click buttons, fill out forms, and verify that your website behaves correctly.

It is installed as a **`devDependency`** (using `npm install -D @playwright/test`) because testing tools are only needed while you or a Continuous Integration (CI) pipeline are actively developing and validating the code. You don't want to bundle Playwright's heavy automation engines into the final production code that gets shipped to your actual users.

### 2. Decoding the `npm run test:viewer` Script

Because npm scripts are entirely customizable, the exact behavior of `npm run test:viewer` depends on how it was defined in your project's `package.json` file. However, in a Playwright environment, this script almost always points to one of three common diagnostic scenarios:

#### Scenario A: Opening the Playwright UI Mode (Most Likely)

If the script is mapped to `playwright test --ui`, running this command opens a local, interactive graphical interface.

- **What it does:** It allows you to visually step through your automated tests frame-by-frame. You can watch the browser execute actions, inspect the DOM at any exact millisecond, view network requests, and read console logs for that specific test run.
    

#### Scenario B: Opening the HTML Test Report / Trace Viewer

If the script is mapped to `playwright show-report`, it opens Playwright's native diagnostic reporter.

- **What it does:** If your tests ran in the background (headless mode) and something failed, Playwright generates a detailed post-mortem report. This viewer serves a local web page containing recorded videos of the failure, screenshots of the exact moment an error occurred, and full execution traces.
    

#### Scenario C: Running Tests Targeting a "Viewer" Feature

If your application features a specific component called a "Viewer" (such as a PDF viewer, 3D model viewer, or a dashboard viewer), the script might look like `playwright test tests/viewer.spec.ts`.

- **What it does:** It tells Playwright to skip the rest of the test suite and strictly run the automated browser diagnostics against that specific feature.
    

### How to check what yours does

To find out exactly which of these scenarios your project is using, open your **`package.json`** file and look inside the `"scripts"` object. You will see a line that looks something like this:

JSON

```
"scripts": {
  "test:viewer": "playwright test --ui" 
}
```

Which of those commands is your `test:viewer` script mapped to in your `package.json`?


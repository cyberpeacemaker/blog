---
created: 2026-05-27
tags: [dev, git]
type: reference
lang: en
status: draft
---

Here is how to navigate that menu and where to find the authentication token if you need one.

### How to Choose an Option

As the blue text in your screenshot hints (`[Use arrows to move...]`), you cannot use your mouse to click these options.

1. Use the **Up** and **Down arrow keys** on your keyboard to move the `>` cursor next to the option you want.
2. Press **Enter** to confirm your selection.

**Which should you pick?**

* **Login with a web browser:** Choose this! It is by far the easiest method. It will pop open a window in your web browser, ask you to click "Authorize," and log you in automatically.
* **Paste an authentication token:** Choose this only if you are working on a remote server without a screen (like via SSH) where a web browser cannot open, or if you want strict control over specific permissions.

---

### Where is the Authentication Token?

If you choose the "Paste an authentication token" option, you won't find this token anywhere on your computer by default. You have to manually generate a **Personal Access Token (PAT)** on the GitHub website.

Here is how to get one:

1. Log into **[GitHub.com](https://github.com/)** in your web browser.
2. Click your **profile photo** in the top right corner and select **Settings**.
3. Scroll all the way down the left sidebar and click **Developer settings**.
4. On the left, click **Personal access tokens**, then select **Tokens (classic)**.
5. Click the **Generate new token** drop-down and select **Generate new token (classic)**.
6. Give your token a note (e.g., "GitHub CLI Mac").
7. Select the recommended scopes (permissions) for the CLI. Usually, you will want to check:
* `repo` (Full control of private repositories)
* `read:org` (Read org and team membership)
* `admin:public_key` (Manage user keys)


8. Scroll to the bottom and click **Generate token**.
9. **Copy the token** (it usually starts with `ghp_`).
10. Go back to your terminal, select "Paste an authentication token," and paste it in.

> **Important:** GitHub will only show you this token once. If you lose it, you will have to delete it and generate a new one.
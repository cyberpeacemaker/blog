---
created: 2026-05-27
tags: [dev]
type: reference
lang: en
status: draft
---

**Prerequisites**
Make sure you have the official **GitHub Pull Requests and Issues** extension installed in VS Code and sign in to your GitHub account.

**Step 1: Start from a Clean Slate**
Before writing any code, ensure you are on your `main` branch and have the latest updates.

1. Open the Source Control panel in VS Code.
2. Click the branch name in the very bottom-left corner of your VS Code window. Select `main`.
3. Click the "Sync Changes" button to pull down any updates from GitHub.

**Step 2: Create Your Safe Space**
Now, let's create a feature branch.

1. Click the `main` text in the bottom left corner again.
2. Select **Create new branch**.
3. Name it descriptively, like `feature/dark-mode`, and hit Enter. VS Code will automatically switch you to this new branch.

**Step 3: Do the Work**
Code exactly like you normally would. Save your files, stage them, and write your commit messages. Your changes are completely isolated from `main`.

**Step 4: Publish and Open a PR**
Once your feature is complete and committed locally, it's time to send it to GitHub.

1. In the Source Control panel, click the **Publish Branch** button. This sends your new branch to GitHub.
2. A small notification will pop up in VS Code asking if you want to create a Pull Request. Click it! (Alternatively, go to the GitHub tab on your sidebar and click the "+" icon to create a PR).
3. Give your PR a title and description, and click **Create**.

**Step 5: Merge and Clean Up**
You can review your own PR right inside VS Code or on GitHub.com.

1. Once you are happy with the changes, click **Merge Pull Request**.
2. Switch your local VS Code branch back to `main` (using the bottom-left corner).
3. Click **Sync Changes** to download the new, updated `main` branch.
4. Delete your old feature branch.

You are now ready to start the cycle all over again with a perfectly clean repository!
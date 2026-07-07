---
created: 2026-06-03
tags: [dev, git]
type: reference
lang: en
status: draft
---

A **`.gitkeep`** file is a community convention used to force Git to track an otherwise empty directory.

Here is the breakdown of why it exists and how it works:

### The Problem it Solves

By design, **Git tracks files, not directories.** If you create an empty folder in your project and try to commit it, Git will completely ignore it.

However, sometimes you *need* an empty directory to exist in your repository—for example, a `logs/`, `uploads/`, or `temp/` folder that your application requires to run properly, even if there are no files in it initially.

### How `.gitkeep` Works

Because Git needs at least one file to track a directory, developers create a dummy file inside the empty folder.

* By naming it `.gitkeep`, it clearly communicates to other developers: *"This file is only here to keep this directory in Git."*
* **Important note:** Unlike `.gitignore`, the name `.gitkeep` has absolutely no special meaning to Git itself. You could name it `.keep`, `empty.txt`, or literally anything else, and it would do the exact same job.

### The Alternative: Using `.gitignore`

Sometimes, developers use a `.gitignore` file instead of a `.gitkeep` to achieve the same thing, while also preventing *other* files from being committed there.

If you want a folder to exist but want Git to ignore any files that get generated inside it (like log files), you can place a `.gitignore` inside that folder with these two lines:

```text
# Ignore everything in this directory
*
# Except this .gitignore file
!.gitignore

```
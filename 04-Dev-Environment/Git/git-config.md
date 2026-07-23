---
title: "Check Git Config User Identity"
description: "Lists quick Git config commands for verifying the configured user name and email."
created: 2026-07-22
updated: 2026-07-22
tags: [dev, git]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[git-best-practice]] · [[github-cli]]

You set those up perfectly! To quickly verify that Git saved your name and email correctly, run this command in your terminal:

Bash

```
git config --global --list
```

### Expected Output

You should see your updated credentials listed like this:

Plaintext

```
user.name=cyberpeacemaker
user.email=a47u0905@gmail.com
```

### Alternative Quick Checks

If you ever want to check an individual field on the fly, you can run:

- **Check Name:**
    
    Bash
    
    ```
    git config user.name
    ```
    
- **Check Email:**
    
    Bash
    
    ```
    git config user.email
    ```


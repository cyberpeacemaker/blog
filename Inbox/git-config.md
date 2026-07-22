---
created: 2026-07-22 11:07
updated: 2026-07-22 11:07
tags: []
type: reference
lang: en
status: draft
---
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


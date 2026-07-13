---
created: 2026-07-13 16:07
updated: 2026-07-13 16:07
tags: []
type: reference
lang: en
status: draft
---
When you duplicate the folder and change the remote, you are essentially telling Git: _"Hey, I love this entire history, but we have a new home now. Stop talking to the old GitHub project and start talking to this new one."_

Here is exactly what happens under the hood and the exact steps to do it safely for your `A1` to `B1` scenario.

## What Happens to the History and Folders?

- **Your History Stays Intact:** Because you copy the folder, the hidden `.git` folder moves with it. This means every single commit, branch, and tag from `A1` is perfectly preserved inside `B1`.
    
- **The Cord is Cut:** By changing the remote URL, folder `B1` completely forgets that GitHub project `A1` ever existed. It will now only push and pull from GitHub project `B1`.
    
- **Safety:** Your original folder `A1` and GitHub project `A1` remain completely untouched. They act as your safety net.
    

## Step-by-Step: Moving from A1 to B1

Here is the exact workflow developers use to achieve this:

### Step 1: Create the new GitHub Home

Go to GitHub and create a brand-new, **completely empty** repository named `B1`.

> ⚠️ **Important:** Do **NOT** check the boxes to add a README, `.gitignore`, or License. Leave it totally blank. If you initialize it with a README, Git will complain about "unrelated histories" when you try to push.

Copy the new repository URL (e.g., `[https://github.com/yourusername/B1.git](https://github.com/yourusername/B1.git)`).

### Step 2: Duplicate the Folder Locally

On your computer, copy your project folder `A1` and paste it as a new folder named `B1`.

### Step 3: Point Folder B1 to GitHub B1

Open your terminal, navigate into your **new `B1` folder**, and run these commands:

1. **Check where it currently points:**
    
    Bash
    
    ```
    git remote -v
    ```
    
    _(You will see it is still pointing to your old GitHub `A1` repo)._
    
2. **Change the URL to the new `B1` repository:**
    
    Bash
    
    ```
    git remote set-url origin https://github.com/yourusername/B1.git
    ```
    
3. **Verify the change:**
    
    Bash
    
    ```
    git remote -v
    ```
    
    _(It should now display your new `B1` GitHub URL)._
    

### Step 4: Push Everything to the New Repo

Now, you need to push your entire history and branches up to the new GitHub `B1` project. Run this command:

Bash

```
git push -u origin --all
```

_(Optional: If you have Git tags you want to bring over, also run `git push --tags`)._

## The End Result

You now have two completely separate universes:

1. **The `A1` Universe:** Your old local folder and old GitHub repo, frozen in time (or still active if you choose).
    
2. **The `B1` Universe:** Your new local folder and new GitHub repo, containing 100% of the history from `A1`, ready for you to start building V2.
    

Do you have multiple branches in `A1` that you need to make sure carry over to `B1`, or are you mostly worried about just the main branch?


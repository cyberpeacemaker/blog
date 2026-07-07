Here is the standard, step-by-step workflow for creating an open-source Pull Request using just your browser, the command line, and VS Code.

### Step 1: Fork the Repository (Browser)

Since you don't have direct write access to the main Arkime repository, you need your own copy (a fork) to make changes.

1. Go to the [Arkime GitHub page](https://github.com/arkime/arkime).
2. In the top-right corner, click the **Fork** button.
3. Leave the default settings and click **Create fork**. You now have a copy of the repo under your own GitHub account (`github.com/YOUR-USERNAME/arkime`).

### Step 2: Clone Your Fork (Command Line)

Now you need to download your fork to your local machine. Open your terminal (Cmd, PowerShell, or Git Bash) and run:

```bash
# Clone your specific fork down to your computer
git clone https://github.com/YOUR-USERNAME/arkime.git

# Move into the new directory
cd arkime

```

*(Make sure to replace `YOUR-USERNAME` with your actual GitHub username).*

### Step 3: Open in VS Code & Create a Branch

It is a golden rule of Git to never make changes directly to your `main` or `master` branch. You always want to create a specific branch for your fix.

1. Open the project in VS Code right from your command line:
```bash
code .

```


2. Once VS Code opens, you can use the **Integrated Terminal** inside VS Code (View > Terminal, or press `Ctrl + ``) for the rest of these commands.
3. Create and switch to a new branch for your fix:
```bash
git checkout -b fix-help-typo

```



### Step 4: Make the Fix (VS Code)

1. In VS Code's file explorer on the left, navigate to:
`viewer/vueapp/src/components/help/Help.vue`
2. Press `Ctrl + F` and search for `field1=value1`.
3. Add the missing equals sign so it reads `field1==value1`.
4. **Save** the file (`Ctrl + S`).

### Step 5: Stage and Commit Your Changes (Command Line)

Now you need to tell Git that you want to save this change.

```bash
# Check to see what files were modified (Help.vue should show in red)
git status

# Stage the file (tells Git to include it in the next commit)
git add viewer/vueapp/src/components/help/Help.vue

# Commit the change with a descriptive message
git commit -m "docs: fix typo in search grouping help text"

```

### Step 6: Push to Your Fork (Command Line)

Your changes are currently only saved on your local computer. You need to push this new branch up to your fork on GitHub.

```bash
git push origin fix-help-typo

```

### Step 7: Open the Pull Request (Browser)

1. Go back to your browser and navigate to either your fork or the main [Arkime repository](https://github.com/arkime/arkime).
2. GitHub is smart—it will see that you just pushed a new branch and display a green banner at the top that says **"Compare & pull request"**. Click that button.
3. Give your PR a clear title (e.g., `Fix missing equals sign typo in basic help docs`).
4. In the description box, briefly explain what you did. You can even mention that it brings the example in line with the rest of the documentation.
5. Click **Create pull request**.

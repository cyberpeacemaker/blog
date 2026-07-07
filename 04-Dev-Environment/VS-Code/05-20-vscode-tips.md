
## 1. "Set It and Forget It" Editor Settings

You can access these by pressing `Ctrl+,` to open the Settings UI, or by clicking the file icon in the top right of the Settings tab to open your `settings.json` file.

* **Format on Save (`"editor.formatOnSave": true`):** This is arguably the biggest time-saver. Every time you press `Ctrl+S`, VS Code will automatically run your default formatter (like Prettier or a language-specific formatter) and clean up your indentation and spacing.
* **Auto Save (`"files.autoSave"`):** Change this from `off` to `onFocusChange` or `afterDelay`. You'll rarely have to manually save again, and you'll never lose work if you accidentally close a window.
* **Bracket Pair Colorization (`"editor.bracketPairColorization.enabled": true`):** This color-codes matching brackets, braces, and parentheses. When you are deep inside nested JSON logs or complex functions, this makes it infinitely easier to see where blocks of code start and end.
* **Linked Editing (`"editor.linkedEditing": true`):** If you work with HTML or XML, this setting automatically updates the closing tag when you change the opening tag (and vice versa).

## 2. Optimize Search and Explorer

When working with large directories, your search results and file explorer can get cluttered with files you don't actually need to look at.

* **Exclude Clutter (`"files.exclude"` and `"search.exclude"`):** You can tell VS Code to completely ignore certain folders (like `.git`, `node_modules`, or compiled `.class` files). This makes your file tree much cleaner and makes global searches (`Ctrl+Shift+F`) lightning fast because it isn't scanning useless files.

## 3. Power-User Shortcuts

Memorizing a few core shortcuts transforms how you navigate your code.

* **Quick Open (`Ctrl+P`):** Stop clicking through the file explorer. Press `Ctrl+P`, start typing the name of the file you want, and press Enter to instantly jump to it.
* **Multi-Cursor Editing:** This feels like a superpower once you get used to it.
* Hold `Alt` and click in different places to place multiple cursors and type in multiple spots at once.
* Highlight a word and press `Ctrl+D` to select the *next* occurrence of that word. Press it a few times, and you can edit all of them simultaneously.


* **Toggle Panel (`Ctrl+` `):** Quickly show or hide your integrated terminal and output windows to get them out of your way when you are focusing on code.

## 4. Focus and Workspace

* **Zen Mode:** Press `Ctrl+K`, let go, and press `Z`. This hides the activity bar, the sidebar, the terminal, and makes your code full screen for pure, distraction-free work. Press `Esc` twice to exit.

---
title: "Moving Files Between Obsidian Vaults"
description: "Explains how to move notes, canvases, attachments, and settings between Obsidian vault folders safely."
created: 2026-07-09
updated: 2026-07-09
type: howto
lang: en
status: draft
tags: [obsidian, workflow]
---

> Related: [[07-Productivity-Work]] · [[obsidian-vault-layout]] · [[obsidian-supported-files]]

## Yes, absolutely!

One of Obsidian’s biggest strengths is that it doesn't trap your data in a proprietary cloud. An Obsidian vault is just a standard folder on your computer's hard drive, and your notes, canvases, and attachments are just regular files inside it.

Because of this, moving things between vaults is incredibly easy. Here is how to do it and what to keep in mind.

### How to Move Your Files

The safest and most efficient way to move files is through your computer's file manager (**File Explorer** on Windows or **Finder** on Mac), rather than inside the Obsidian app itself.

1. **Close Obsidian** (optional, but it prevents the app from glitching while indexing changes).
    
2. Open your system's file manager and locate **Vault A** (the source) and **Vault B** (the destination).
    
3. Select the files, folders, or `.canvas` files you want to move.
    
4. **Copy or drag** them directly into the folder of Vault B.
    
5. Reopen Obsidian. It will automatically detect the new files and index them.
    

### ⚠️ Crucial Things to Watch Out For

While the physical moving of files is seamless, Obsidian relies heavily on internal connections. Keep these three things in mind:

- **Broken Links:** If you move a note or a canvas that links to _other_ notes, those links will break in the new vault unless you also move the companion notes.
    
- **Canvas Images & Attachments:** Canvas files (`.canvas`) often embed images, PDFs, or other notes. If you move a canvas file alone, any embedded images or cards pointing to local notes will show up as blank or broken in the new vault. **Tip:** Make sure to grab the corresponding assets from your attachments folder too!
    
- **Settings and Plugins:** Moving a note doesn't move your custom fonts, plugins, or themes. If you want Vault B to look and act _exactly_ like Vault A, you need to copy the hidden `.obsidian` folder from the root of Vault A into Vault B. (You may need to press `Ctrl + Shift + .` on Windows or `Cmd + Shift + .` on Mac to see hidden folders).

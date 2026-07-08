---
created: 2026-07-08 20:07
tags: []
type: reference
lang:
status: draft
---
Here’s what **“Ctrl+N → Inbox/ with frontmatter”** means in VS Code/Cursor, and how you’d actually do it.

## What Obsidian does (reminder)

1. Creates a real file under `Inbox/`
2. Names it (or starts as Untitled, then you rename)
3. Injects YAML from Templater

VS Code’s default **`Ctrl+N`** only opens an **untitled buffer** — nothing is written to `Inbox/` and no frontmatter is added. So you replace that shortcut with “create a file from a template.”

---

## Option A — Snippet (paste YAML into an empty note)

A **snippet** is text you insert with a trigger (e.g. type `note` + Tab).

Example snippet body (same idea as your Obsidian template):

```json
{
  "New note frontmatter": {
    "prefix": "newnote",
    "body": [
      "---",
      "created: $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",
      "tags: []",
      "type: reference",
      "lang: en",
      "status: draft",
      "---",
      "",
      "$0"
    ],
    "description": "Vault default frontmatter"
  }
}
```

**How you’d use it**

1. Create `Inbox/my-topic.md` yourself (or Save As into `Inbox/`)
2. Type `newnote` → Tab  
3. Frontmatter appears with today’s date

**Pros:** Built-in, no extension, easy.  
**Cons:** Does **not** create the file or put it in `Inbox/` for you. Not a true `Ctrl+N` replacement.

---

## Option B — File Templates extension (closest to what you want)

Install something like **File Templates** (or **File Template**, “new file from template” style extensions).

You keep a template file, e.g.:

`00-Meta/templates/vscode-default-note.md` (or reuse a static copy of frontmatter)

Then the extension command is roughly:

> **New File from Template** → pick template → pick folder / name → writes `Inbox/<name>.md`

You bind that command to **`Ctrl+N`** (and unbind or move the default “New Untitled File”).

**Pros:** Creates a **real file** in `Inbox/` with YAML — most like Obsidian.  
**Cons:** Needs an extension; setup once in Settings / templates folder.

**Rough mental model**

```
Ctrl+N
  → extension: "New file from template"
  → template: frontmatter + empty body
  → location: Inbox/
  → result: Inbox/my-topic.md with created: 2026-07-08
```

Dates: many extensions support `${date}` / `${year}` etc., or you keep a simple static template and fill `created` manually once (or use a snippet inside the template workflow).

---

## Option C — Custom task / script (most control)

A small script or VS Code task:

1. Ask for a filename  
2. Write `Inbox/<name>.md` with today’s date in YAML  
3. Open that file  

Bind a key to “Run task” / “Run script”.

**Pros:** Exact control; matches your vault paths perfectly.  
**Cons:** You maintain the script; not click-and-go like Obsidian’s Templater UI.

Example idea (PowerShell):

```powershell
$name = Read-Host "Note name"
$date = Get-Date -Format "yyyy-MM-dd"
@"
---
created: $date
tags: []
type: reference
lang: en
status: draft
---

"@ | Set-Content "Inbox\$name.md"
code "Inbox\$name.md"   # or cursor ...
```

---

## Side-by-side

| Approach | Creates file in `Inbox/`? | Auto frontmatter? | Feels like Obsidian `Ctrl+N`? |
|----------|---------------------------|-------------------|------------------------------|
| **Snippet** | No | Yes (after you open a file) | Low |
| **File Templates extension** | Yes | Yes | High |
| **Custom script/task** | Yes | Yes | High (DIY) |

---

## Practical takeaway

- **Snippet** = “when I’m already in a markdown file, stamp the YAML.”  
- **File Templates / script** = “`Ctrl+N` means: create `Inbox/<name>.md` *with* YAML,” which is the Obsidian combo (location + template).

Obsidian needed **location (`Inbox`) + auto-template**. VS Code needs the same two ideas; they just aren’t built-in as one command unless you use an extension or a script.

If you want this in Cursor next, say **snippet only** or **File Templates + Ctrl+N rebinding** and we can wire it for this vault.

---

Yes, absolutely. While VS Code doesn't have an "Obsidian-style" template button right out of the box, you can achieve the exact same behavior using either **built-in file templates** or a **dedicated extension**.

Here are the two best ways to do it depending on how close to the "Obsidian vibe" you want to get.

### Method 1: The Built-In Way (File Template Snippets)

VS Code has a native feature called **File Templates** that allows you to fully populate a brand-new, empty file with a predefined structure using snippets.

1. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on Mac).
    
2. Type and select **Preferences: Configure User Snippets**.
    
3. Select **markdown** (or choose _New Global Snippets File_ if you want it to apply to multiple file types).
    
4. Paste a configuration like this inside the JSON object:
    

JSON

```
{
  "Daily Note Template": {
    "prefix": "daily-note",
    "body": [
      "# Journal: $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",
      "",
      "## Today's Focus",
      "- [ ] $1",
      "",
      "## Notes",
      "$0"
    ],
    "description": "Populates a standard daily note template",
    "isFileTemplate": true
  }
}
```

> **How to use it:** Create a brand new, empty `.md` file. Open the Command Palette, run **Snippets: Fill File with Snippet**, and select your template. Alternatively, you can just type your prefix (`daily-note`) in the blank file and hit `Tab`.

### Method 2: The Extension Way (Closest to Obsidian)

If you want a workflow that automatically handles note folders, dates, and frontmatter prompts just like Obsidian, extensions are your best bet.

- **VSNotes:** This is the closest 1:1 match to Obsidian's note system. It maps a specific folder for your notes, supports tokens like `{dt}` (date-time) or `{title}` for automatic file naming, and lets you trigger a `VSNotes: Create a New Note` command which prompts you to pick a template.
    
- **Foam:** If you are trying to turn VS Code into a complete Obsidian alternative (with backlinking, daily notes, and graph views), install **Foam**. It is a personal knowledge management ecosystem that relies heavily on note templating.
    
- **Create Files From Template (CFFT):** If you just want a generic utility where you can right-click any folder in your explorer sidebar and select "New From Template...", this extension is lightweight and perfect.
    

### Which one should you pick?

- If you want a fast, zero-extension setup to paste structures into empty files: **Use Method 1**.
    
- If you want a dedicated shortcut that creates the file, names it with today's date, and fills the template all in one click: **Install VSNotes**.

---

Here is the exact JSON object you need to paste into your `markdown.json` snippet file.

I’ve included VS Code's native date variables so the current date auto-fills perfectly, added the mandatory frontmatter fences (`---`), and set up tab-stops (`$1`, `$2`) so you can jump through fields instantly using the `Tab` key.

JSON

```
{
  "Markdown Post Template": {
    "prefix": "frontmatter",
    "body": [
      "---",
      "date: $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",
      "description: \"${1:A short, punchy summary for SEO and previews.}\"",
      "draft: false",
      "tags: [$2]",
      "---",
      "",
      "# ${3:Title}",
      "",
      "$0"
    ],
    "description": "Inserts a standard Markdown file template with YAML frontmatter",
    "isFileTemplate": true
  }
}
```

### How this works under the hood:

- **`$CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE`**: Automatically resolves to the exact date you create the file (e.g., `2026-07-08`).
    
- **`${1:A short...}`**: This is a placeholder. When the template generates, this text will be highlighted. You can immediately start typing to overwrite it, or hit `Tab` to keep it.
    
- **`[$2]`**: Your cursor will jump here second so you can type your tags.
    
- **`${3:Title}`**: Your cursor jumps here third to name your post.
    
- **`$0`**: This defines the _final_ position of your cursor after you're done tabbing through the fields.
    

### Quick Reminder on Usage

1. Create a new file and save it as `anything.md`.
    
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
    
3. Run **Snippets: Fill File with Snippet** and select your template.
    

_(Alternatively, just open the blank file, type `frontmatter`, and hit `Tab`!)_


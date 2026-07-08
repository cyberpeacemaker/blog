```dataview
LIST 
WHERE created = date(2026-07-07)
```

```dataview 
TABLE tags, type WHERE created = date(2026-06-18)
```

---

In Obsidian, since you have a custom date property explicitly named `created` (as shown in your `image_bc4f27.png`), you have a few excellent ways to pull up all files matching that specific day.

Even though the Obsidian UI displays the date format as `MM/DD/YYYY` (`06/18/2026`) based on your local display settings, under the hood, Obsidian stores and queries these properties using the standard ISO format (`YYYY-MM-DD`).

## Method 1: Using Obsidian's Built-In Search (Fastest)

You can search your properties directly using the global search bar (`Ctrl + Shift + F` on Windows/Linux or `Cmd + Shift + F` on macOS).

Use the bracket search syntax to isolate the property:

Plaintext

```
[created: 2026-06-18]
```

> 💡 **Tip:** If you want to embed this search directly into a note so it stays there as a permanent list, you can wrap it in a native query block:
> 
> ```query
> 
> [created: 2026-06-18]
> 
> ```

## Method 2: Using the Dataview Plugin (Best for Dynamic Lists)

If you use the popular **Dataview** community plugin, you can generate a live-updating list or table of those notes. Paste either of these code blocks into any markdown file:

### As a simple list:

Markdown

````
```dataview
LIST 
WHERE created = date(2026-06-18)
````

````

### As a structured table:
If you want a view that displays your other properties shown in `image_bc4f27.png` (like `tags` and `type`), you can display them as columns:
```markdown
```dataview
TABLE tags, type
WHERE created = date(2026-06-18)
````

````

---

## Method 3: Using System Metadata (Fallback)
If you ever forget to fill out the `created` property on a note but still want to find notes created on that day using the system's actual file properties, Dataview can look at the implicit file creation date (`file.cday`):

```markdown
```dataview
LIST
WHERE file.cday = date(2026-06-18)
````


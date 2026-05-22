### How to use inline referencing in Claude

* **The `@` Command:** Just like in Cursor, type `@` directly into the text input box (where it says "Type / for commands").
* **Autocomplete:** Start typing the name of a file in your project (e.g., `@convert_opensearch_query.py`). Claude will bring up an autocomplete dropdown. Hit `Tab` or `Enter` to select it.
* **What it does:** This instantly attaches the file to your prompt's context, allowing Claude to read and reference its exact contents when generating a response.

### Claude Desktop vs. Cursor: A Quick Comparison

While the `@` syntax is identical, the underlying mechanics differ slightly because of what each tool is built to do:

* **File-Level vs. Deep Integration:** In Claude's desktop app, `@` is primarily a lightning-fast way to attach local files to your chat context. Cursor, being a full-fledged IDE, indexes your entire codebase deeper, allowing its `@` menu to reference specific functions, codebase-wide semantic searches, Git commits, and terminal errors.
* **UI Alternatives:** If you don't want to use the `@` shortcut, Claude still supports traditional methods. You can click the `+` or paperclip icon (visible at the bottom left of your prompt bar) to browse for files, or simply drag and drop a file from your file explorer directly into the chat box.

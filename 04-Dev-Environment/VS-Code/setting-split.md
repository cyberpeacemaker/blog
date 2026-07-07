---
created: 2026-06-17
tags: [dev]
type: reference
lang: en
status: draft
---

### The Standard Convention

In most development environments, having a base configuration file and a local override is the best way to manage environment variables safely:

* **`settings.json`**: This file is typically tracked in version control (like Git) and shared with anyone working on the project. It should only contain non-sensitive, global configuration settings that every user needs.
* **`settings.local.json`**: This file should be added to your `.gitignore` file. It is designed to hold sensitive information—like personal API keys—and specific environment configurations strictly for your local machine.

### The Security Risk in Your Setup

While using two files is correct, **image_bf1945.jpg** shows that your `settings.json` contains a `VT_API_KEY` (likely a VirusTotal API key). If this file is ever pushed to a repository, your private key will be publicly exposed or shared with everyone who has access to the repo.

### Recommendation

Yes, keep both files, but consolidate your secrets:

1. Move the `VT_API_KEY` out of `settings.json`.
2. Place it into the `"env"` block within `settings.local.json`, right alongside your `MB_API_KEY`.
3. Ensure `settings.local.json` is explicitly listed in your `.gitignore` file.

Are both of these files currently being tracked by your version control system, or is the `.local` file correctly ignored?
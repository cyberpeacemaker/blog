---
title: "Reference and Input Folder Naming"
description: "Compares asset, data, reference, specs, inputs, raw, and provided folder names for project materials."
created: 2026-07-21
updated: 2026-07-21
tags: [dev, workflow]
type: reference
lang: en
status: draft
---

> Related: [[05-Software-Engineering]] · [[unsorted-folder-naming]] · [[folder-structure]]

Neither `asset` nor `data` is inherently wrong, but they both carry specific conventions in software development that might lead to confusion depending on what you're putting in there.

Here is a quick breakdown of how those terms are usually interpreted, followed by stronger alternatives based on your exact use case.

## The Issue with `asset` and `data`

- **`assets/` (or `asset/`):** In web and app development, `assets/` almost always means **production media**—images, fonts, icons, or audio files that are compiled and shipped directly into the final build. If this folder just contains reference files or task specs, calling it `assets/` might confuse future you or teammates expecting build dependencies.
    
- **`data/`:** Works well if the materials are strictly datasets (CSVs, JSONs, databases). However, if the materials include PDFs, wireframes, text briefs, or client guidelines, `data/` is a bit too generic or imprecise.
    

## Better Alternatives Based on File Type

### 1. If they are reference materials, specs, or task briefs

If someone handed you guidelines, PDFs, requirement docs, or mockups to work off of:

- **`reference/` (or `ref/`):** The standard choice for context, specs, or examples provided by stakeholders.
    
- **`docs/external/` or `docs/briefs/`:** Clean and self-explanatory if your repo already uses a `docs/` folder.
    
- **`specs/`:** Great if the materials are formal technical or design specifications.
    

### 2. If they are raw files meant to be processed by your code

If someone gave you raw files (data, images, audio) that your scripts need to import, clean, or transform:

- **`inputs/` or `input/`:** Makes it immediately obvious that these are incoming materials fed into your workflow/scripts.
    
- **`provided/`:** Clearly signals "this came from an external party/assigner."
    
- **`raw/` or `data/raw/`:** The gold standard in data engineering/science for unedited, original files received from outside sources.
    

## 💡 Pro Tip for Repositories

If these assigned materials are **large binaries** (e.g., large datasets, heavy design files) or **confidential client docs**, make sure to add them to your `.gitignore` file (or use Git LFS) so you don't bloat your Git history or leak sensitive information!

What specific types of files are you usually dropping into this folder (e.g., CSVs/datasets, PDFs/word docs, or media files)?


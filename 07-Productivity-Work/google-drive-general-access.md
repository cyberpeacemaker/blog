---
title: "Google Drive General Access and Ownership"
description: "Explains why organization-wide Google Drive edit access does not transfer ownership of uploaded files."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [workflow]
---

> Related: [[07-Productivity-Work]] · [[obsidian-supported-files]] · [[mail]]
This is a classic Google Drive permissions puzzle! It looks confusing at first glance, but there is a very logical reason why **史賀文** owns that file even though they aren't explicitly named in the folder's direct "People with access" list.

This happens due to two core Google Drive features working together:

### 1. The Google Drive File Ownership Rule

In Google Drive, **the person who creates or uploads a file is always its owner**, regardless of who owns the folder it lives in.

- When someone shares a "My Drive" folder with you and gives you editing permissions, you can upload files into it.
    
- However, any file you upload still belongs to _you_ (and uses _your_ storage space) until you explicitly transfer ownership to someone else.
    
- Therefore, because **史賀文** uploaded or created that specific file on July 7, they remain the owner of it.
    

### 2. General Organization-Wide Access (The "Missing" Member)

You might wonder: _If they aren't listed under "People with access," how did they get into the folder to upload the file in the first place?_

Take a look at the **General access** section at the bottom of your sharing dialog:

- It is set to **國家資通安全研究院** with **Editor** permissions ("Anyone in this group with the link can edit").
    
- Since **史賀文** is part of your organization, they don't need to be individually added by name to the "People with access" list. They simply accessed the folder via the organization-wide link, which gave them edit access.
    
- Once inside, they uploaded the file, making them the file's owner.
    

> 💡 **Quick Tip:** If you need the folder owner (**李亞軒**) to own absolutely everything inside this folder (for storage or administrative reasons), **史賀文** will need to open that specific file's share settings and manually transfer ownership to **李亞軒**. Moving a file into someone else's folder does not automatically transfer its ownership.


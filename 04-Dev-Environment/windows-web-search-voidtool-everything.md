---
title: "Disable Windows Web Search and Use Everything"
description: "Shows how to reduce Windows Start web results and use local file search tools such as Voidtools Everything."
created: 2026-07-17
updated: 2026-07-17
type: howto
lang: en
status: draft
tags: [dev]
---

> Related: [[MOC - Dev Environment]] · [[windows-search-voidtool-everything]] · [[microsoft-store]]
> **You are preaching to the choir!** There is nothing more frustrating than typing a very specific, local file name (like `report-nics-otex-exchange` in your screenshot) only for Windows to treat it like a search engine query and dump useless Bing suggestions on your screen. If you wanted to search the web, you would have opened Google Chrome or Microsoft Edge.

Fortunately, you can easily reclaim your Start Menu and force it to focus strictly on your local files.

## How to Turn Off Search on the Web

Depending on your region and Windows edition, there are a few ways to disable Bing search integration.

### Method 1: Check your Settings (If available in your region)

In some regions (especially the EU), Microsoft allows you to toggle this off directly:

1. Open **Settings** (`Win + I`).
    
2. Go to **Privacy & security** > **Search permissions**.
    
3. Scroll down and look for a setting under "More settings" to disable **Web search**.
    

_If you do not see this option, Microsoft has hidden it in your region. You will need to use one of the alternative methods below instead._

### Method 2: For Windows 11 Pro / Enterprise (Group Policy)

If you are running Windows Pro or Enterprise, the cleanest way to disable it is via Group Policy:

1. Press `Win + R`, type **`gpedit.msc`**, and press Enter to open the Local Group Policy Editor.
    
2. Navigate to: **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search**.
    
3. On the right, find and double-click **Do not allow web search**, set it to **Enabled**, and click OK.
    
4. Find and double-click **Don't search the web or display web results in Search**, set it to **Enabled**, and click OK.
    
5. Restart your computer.
    

### Method 3: For Windows 11 Home (Registry Editor)

If you are on Windows 11 Home, you can achieve the same result by tweaking the Registry:

1. Press `Win + R`, type **`regedit`**, and press Enter to open the Registry Editor.
    
2. Navigate to:
    
    `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows`
    
3. Look for a folder named **Explorer** under _Windows_. If it doesn't exist, right-click the **Windows** folder, select **New** > **Key**, and name it **Explorer**.
    
4. Right-click on the **Explorer** folder, select **New** > **DWORD (32-bit) Value**.
    
5. Name it exactly: **`DisableSearchBoxSuggestions`**.
    
6. Double-click `DisableSearchBoxSuggestions`, change the **Value data** from `0` to **`1`**, and click **OK**.
    
7. Close the Registry Editor and restart your computer to apply the changes.
    

## How to Find/Search for Files in Windows 11

Once you've disabled the web search clutter, your Start Menu search will instantly feel much cleaner. Here are the three best ways to search for files on your laptop:

### 1. Use the Search Menu Tabs (Quickest)

In your screenshot, notice the filter tabs right under your search bar: **All**, **Apps**, **Documents**, **Web**, **Settings**, **Folders**, **Photos**.

- If you click **Documents** or **Folders**, Windows will immediately narrow its focus to local files matching that name, ignoring apps and web results entirely.
    

### 2. Search via File Explorer (Thorough)

To search within specific folders or your entire system:

1. Open **File Explorer** (`Win + E`).
    
2. Navigate to **This PC** (to search your whole computer) or go directly into a specific folder (like _Documents_).
    
3. Click the **Search box** in the top-right corner and type your query.
    
    - **Pro-tip:** Use search syntax to filter. For example, typing `report type:pdf` will search only for PDF files containing the word "report."
        

### 3. The Power-User Secret: Use "Everything"

Windows search indexing can sometimes feel slow or fail to locate deeply hidden files. Most IT professionals use a free, lightweight, and incredibly fast third-party tool called **Everything** (by Voidtools).

- It indexes your entire drive in a couple of seconds and locates any file instantly as you type, with zero web bloat.
    

To see a step-by-step visual walkthrough on how to safely configure the registry to get rid of these web results, check out this [Windows 11 Web Search Disable Tutorial](https://www.youtube.com/watch?v=XaKd6On4L1M). This video is highly relevant because it guides you through creating the correct Registry Key so you can stop Bing results from hijacking your searches.


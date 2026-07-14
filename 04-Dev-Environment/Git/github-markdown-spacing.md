---
title: "GitHub Markdown Spacing and Code Fence Fix"
description: "Explains how non-standard spaces and list indentation can break GitHub Markdown code fences."
created: 2026-07-13
updated: 2026-07-13
type: howto
lang: zh
status: draft
tags: [dev, git, markdown]
---

> Related: [[MOC - Dev Environment]] · [[YAML-markdown]] · [[markdown-link-check-github-action]]

這個版面會跑掉，主要是因為 Markdown 的「隱形空白字元」和「清單縮排」在跟 GitHub 的解析器（Parser）鬧脾氣。

從你提供的截圖可以看到，後半段的 `### 產生的問題`、`### 建議修改` 甚至是底下的 ```bash 標籤，**通通都被吞進去變成了同一個程式碼區塊**（右上角還出現了複製按鈕，而且標題沒有成功變大）。

## 為什麼會這樣？

1. **複製到了「非標準空白」（如不換行空白 `\xa0`）**：
    
    在第一個 ````bash`和`git clone` 前面，有幾個隱形的空白字元。如果你這段文字是從 Notion、Mac 備忘錄或其他筆記軟體複製過來的，常常會夾帶這種特殊空白。Markdown 只認標準的半形空白（Space），遇到這種特殊空白會導致解析器錯亂。
    
2. **清單內的程式碼區塊沒有正確閉合**：
    
    當你在數字清單（`2.`）下面縮排寫程式碼時，GitHub 會預期你的結束標籤 ```` ` 也要有相對應的縮排。因為特殊空白的干擾加上縮排沒對齊，GitHub 認為你的程式碼區塊「根本還沒結束」，所以一路往下吞，把後面的大標題通通當成程式碼處理了。
    

## 解決方法：直接複製這段去貼

最快、最保險的修正方式，就是**把程式碼區塊跟清單「換行切開」，並且不要留任何前置空白**。你可以直接複製下方修正後的語法貼回 GitHub Issue：

Markdown

````
在閱讀 [ONBOARDING.md](https://github.com/nagameTW/otex-claw-devkit/blob/main/ONBOARDING.md) 時，發現前後章節的執行路徑邏輯有些衝突：

1. 在 **[§2 開發助理環境本-repo]** 中，操作結束後使用者的終端機路徑會停留在 `/otex-claw-devkit`。
2. 緊接著在 **[§3 開發助理環境本-repo]** 中，文件引導使用者執行新指令：

```bash
git clone git@github.com:nagameTW/otex-claw-devkit.git
````

### 產生的問題

如果使用者直接依序操作，會在 `/otex-claw-devkit` 目錄內「重複 clone 自身」，導致目錄結構出錯。

### 建議修改

建議在 §3 的 `git clone` 指令前，提示使用者先切換回上層目錄，或是直接在文件中加入 `cd ..` 的步驟。

例如：

Bash

```
cd ..
git clone git@github.com:nagameTW/otex-claw-devkit.git
```

```

---

### 💡 修改小訣竅
* **前後留空行**：在清單文字與 ````bash` 之間多留一條空行，並且讓 ```` ` 靠左對齊不縮排，這樣能保證程式碼區塊乾淨獨立。
* **標題前不要有縮排**：確保 `### 產生的問題` 前後都有空行且完全靠左，GitHub 才會知道它是個大標題，而不是程式碼的一部分。

更新完語法後，重新看一下 GitHub 的 Preview（預覽），大標題和程式碼區塊有各就各位了嗎？
```


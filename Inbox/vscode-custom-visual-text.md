---
created: 2026-07-16 20:07
updated: 2026-07-16 20:07
tags: []
type: reference
lang: en
status: draft
---
答案是**絕對可以**！VS Code 的自訂彈性非常強大。

針對 Text（一般文字）與 Markdown，調整視覺效果通常可以分為兩個方向：**「編輯器本體（你打字時的畫面）」**與**「Markdown 預覽畫面（渲染後的畫面）」**。

以下為你整理最實用的自訂方法與步驟：

## 一、自訂「編輯器本體」的文字視覺效果

如果你想改變打字時的字體、大小，或是讓 Markdown 的語法標記（如標題、粗體、斜體）在編輯時呈現不同顏色，可以透過修改 `settings.json` 來達成。

### 1. 基本字型與間距設定

打開 VS Code 的設定（`Ctrl + ,` 或 `Cmd + ,`），點擊右上角的「開啟設定 (JSON)」圖示，加入以下設定：

JSON

```
{
  "editor.fontSize": 16,               // 字型大小
  "editor.lineHeight": 28,             // 行高（閱讀起來更舒服）
  "editor.letterSpacing": 0.5,         // 字距
  "editor.fontFamily": "'Fira Code', 'PingFang TC', sans-serif", // 自訂字型
  "editor.fontLigatures": true         // 啟用字體連字效果（若字型支援）
}
```

### 2. 自訂 Markdown 語法顏色 (Syntax Highlighting)

如果你不滿意目前的佈景主題對 Markdown 標題、粗體或連結的配色，可以利用 `editor.tokenColorCustomizations` 進行微調：

JSON

```
{
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": "markup.heading", // 針對所有 Markdown 標題
        "settings": {
          "foreground": "#FF8C00", // 改變顏色為橘色
          "fontStyle": "bold"      // 加粗
        }
      },
      {
        "scope": "markup.underline.link", // 針對連結
        "settings": {
          "foreground": "#1E90FF"
        }
      },
      {
        "scope": "markup.bold", // 針對粗體
        "settings": {
          "foreground": "#FF1493"
        }
      }
    ]
  }
}
```

## 二、自訂「Markdown 預覽畫面」的視覺效果

VS Code 內建的 Markdown 預覽（`Ctrl + Shift + V` 或 `Cmd + Shift + V`）可以完全透過 **CSS** 來自訂。

### 1. 建立你的專屬 CSS 檔案

在電腦裡找個地方（例如專案根目錄，或某個固定的資料夾），建立一個名為 `markdown-style.css` 的檔案，並寫入你想套用的樣式：

CSS

```
/* markdown-style.css */
body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    color: #333333;
    line-height: 1.8;
    background-color: #f9f9f9;
}

h1, h2, h3 {
    color: #2c3e50;
    border-bottom: 2px solid #34495e;
    padding-bottom: 5px;
}

code {
    background-color: #ffe6e6;
    color: #c0392b;
    padding: 2px 6px;
    border-radius: 4px;
}
```

### 2. 在 VS Code 設定中載入此 CSS

打開 `settings.json`，將該 CSS 檔案的路徑加到 `"markdown.styles"` 中：

JSON

```
{
  "markdown.styles": [
    "C:/Users/YourName/Documents/markdown-style.css" // Windows 路徑範例
    // 或 "/Users/YourName/Documents/markdown-style.css" (macOS 範例)
  ]
}
```

存檔後，重新打開 Markdown 預覽，你就會發現套用了全新的視覺設計！

## 三、神級輔助套件推薦

如果你不想手寫一堆設定，也可以直接用社群開發的強大套件：

1. **Markdown Preview Enhanced (MPE)**
    
    - **功能**：VS Code 最強的 Markdown 預覽套件。支援自訂 CSS 樣式表、導出 PDF/HTML、甚至能直接在 Markdown 裡跑程式碼和畫流程圖（Mermaid）。
        
2. **Markdown All in One**
    
    - **功能**：提供 Markdown 快捷鍵、自動目錄產生（TOC）、即時預覽等，大幅提升編輯體驗。
        
3. **Custom CSS and JS Loader** (進階玩家)
    
    - **功能**：如果你想**徹底改變 VS Code 編輯器本身的 UI 視覺效果**（例如讓字體發光、加上毛玻璃背景），這個套件可以幫你強制注入全域的 CSS 到 VS Code 本體中。
        

你是希望微調**寫字時的編輯器語法顏色**，還是想設計**匯出/預覽 Markdown 時的排版外觀**呢？


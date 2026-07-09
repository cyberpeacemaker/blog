---
title: "MCP Vision Bridge vs Local Image Recognition"
description: "Compares MCP-style image handoff to Claude with local computer vision inference for image recognition workflows."
created: 2026-07-09
updated: 2026-07-09
type: reference
lang: zh
status: draft
tags: [ai, agents]
---

> Related: [[MOC - AI Agents]] · [[edge-ai-terms]] · [[local-cv-yolo-vs-cloud-vision]]

Python

```
import urllib.request
import json
import base64

url = "https://api.github.com/repos/nagameTW/mcp-server-malcolm/readme"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        if 'content' in data:
            readme_content = base64.b64decode(data['content']).decode('utf-8')
            print(readme_content[:1500])
        else:
            print("No content found.")
except Exception as e:
    print(f"Error: {e}")

```

Code output

```
Error: <urlopen error [Errno -3] Temporary failure in name resolution>

```

你的觀察非常敏銳！你如果在 Repo 裡面沒有看到傳統的「圖像識別」程式碼（例如載入 OpenCV、PyTorch 模型，或是大篇幅的 AI 運算邏輯），這是**非常正常**的現象。

這其實跟 **MCP (Model Context Protocol)** 的架構設計有很大的關係。通常這類標榜支援「視覺」或「圖像識別」的 MCP Server，背後的運作邏輯如下：

### 1. 真正的「大腦」是 LLM，MCP Server 只是「搬運工」

在 MCP 的生態系中，Server 的角色是幫 AI（例如 Claude）準備好需要的素材。

當這個專案提到「圖像識別」時，它本身**並不負責**去分析圖片裡有什麼，而是把這個工作交給了前端具備強大 Vision 能力的模型（如 Claude 3.5 Sonnet）。

它的實際運作流程通常是這樣：

1. **獲取圖像：** 透過系統指令截圖、讀取本地端的圖片檔、或是透過瀏覽器自動化工具（如 Puppeteer/Playwright）抓取網頁畫面。
    
2. **轉碼打包：** 程式碼會將這張圖片轉換成 `Base64` 編碼格式。
    
3. **回傳給 Client：** 透過 MCP 協議，把這個 Base64 的圖片資料丟回給 Claude Desktop 等客戶端。
    
4. **LLM 進行識別：** Claude 看到圖片後，會用它內建的視覺模型進行圖像識別，並回答使用者的問題。
    

### 2. 在這個 Repo 裡，你實際上應該找什麼 Code？

既然沒有 AI 識別的演算法，如果你想看它是怎麼實作這個功能的，可以去翻翻看它 `src` 目錄下的程式碼（通常是 TypeScript 或 Python），尋找以下幾個特徵：

- **讀取或截取畫面的邏輯：** 找看看有沒有讀取檔案（如 `fs.readFile`）或是擷取螢幕/網頁的程式碼。
    
- **Base64 轉換：** 找看看有沒有把圖片轉成字串的邏輯，例如 `.toString('base64')`。
    
- **回傳特定格式的 JSON（這是最關鍵的）：** 根據 MCP 協議的標準，要讓 LLM 看到圖片，Server 定義的 Tool（工具）執行完畢後，必須回傳包含 `image` type 的結構。你應該會看到類似這樣的 Code：
    

JavaScript

```
// MCP 標準的回傳圖片格式
return {
  content: [
    {
      type: "image",
      data: "iVBORw0KGgoAAAANSUhEUgAA...", // 這裡放轉換後的 Base64 圖片數據
      mimeType: "image/png"
    }
  ]
};
```

### 3. 另一種可能：單純呼叫外部 API

如果它不是把圖片交給 Claude，另一種可能就是它在程式碼裡寫了一支簡單的 `fetch` 或 `axios`，把圖片直接 POST 給第三方 API（例如 OpenAI Vision API 或 Google Vision API）。這種寫法看起來就像是一般的網路請求，所以你也不會看到什麼「像是在做圖像識別」的複雜演算法代碼。

**總結來說：**

你看到的這類 MCP 專案，說的「圖像識別」其實是指「具備將圖像餵給 AI 進行識別的能力」。真正的識別引擎都在大語言模型內部，所以你在 Repo 裡面只會看到把圖片轉成 Base64 並丟出去的「橋接」程式碼！

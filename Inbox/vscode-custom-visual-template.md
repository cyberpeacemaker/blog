---
created: 2026-07-16 20:07
updated: 2026-07-16 20:07
tags: []
type: reference
lang: en
status: draft
---
答案是：**完全可以，而且設定後的視覺區隔效果非常棒！**

雖然一般文字檔（Text, `.txt`）本質上沒有像 Markdown 那樣的「語法結構」（例如標題、粗體、連結），但我們可以透過 VS Code 的「語言專屬設定（Language-Specific Settings）」與 **`textMateRules`**，將兩者打造成完全不同的風格。

這裡為你設計一套「現代排版（Markdown） vs. 復古打字機（Plain Text）」的雙視覺方案。

## 🎨 視覺設計概念

- **Markdown (`.md`) ——「現代數位出版風格」**
    
    - **字型**：現代、乾淨的無襯線字體（如微軟正黑體、PingFang），適合結構化閱讀。
        
    - **介面**：保留行號、縮圖（Minimap），方便大範圍跳轉。
        
    - **色彩**：高對比。標題是亮橘色、連結是亮藍色、粗體是亮粉色，結構一眼看穿。
        
- **一般文字 (`.txt`) ——「極簡復古打字機」**
    
    - **字型**：經典的等寬打字機字型（`Courier New`），有創作草稿的儀式感。
        
    - **介面**：**隱藏行號、隱藏縮圖、隱藏對齊線**。整個畫面變成一張乾淨的白紙/黑紙，讓你專注在文字輸入。
        
    - **色彩**：極致單純。將文字統一強制降噪為溫和的「鉛筆灰」，不帶任何雜色。
        

## 🛠️ 一鍵套用設定（`settings.json`）

請打開 VS Code 的 `settings.json` 檔案（按下 `Ctrl + Shift + P` 或 `Cmd + Shift + P`，輸入 `Preferences: Open User Settings (JSON)`），並將以下設定貼入最外層的大括號 `{}` 中：

JSON

```
{
  // ==========================================
  // 1. 語言專屬排版與字型設定（建立空間區隔）
  // ==========================================

  // 【一般文字檔 (.txt) 專屬設定】 -> 打造極簡、無干擾的寫作沙盒
  "[plaintext]": {
    "editor.fontFamily": "'Courier New', 'Georgia', serif", // 復古打字機/襯線字體
    "editor.fontSize": 15,
    "editor.lineHeight": 30,             // 寬鬆寬敞的行高
    "editor.lineNumbers": "off",         // 隱藏行號，假裝是一張紙
    "editor.minimap.enabled": false,     // 隱藏右側縮圖，減少視覺干擾
    "editor.wordWrap": "on",             // 自動換行
    "editor.guides.indentation": false,  // 隱藏縮排輔助線
    "editor.occurrencesHighlight": "off" // 關閉點擊單字時的重複高亮
  },

  // 【Markdown 檔 (.md) 專屬設定】 -> 打造現代、結構清晰的排版編輯器
  "[markdown]": {
    "editor.fontFamily": "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang TC', 'Microsoft JhengHei', sans-serif", // 現代無襯線字體
    "editor.fontSize": 16,
    "editor.lineHeight": 28,
    "editor.lineNumbers": "on",          // 顯示行號，方便定位
    "editor.minimap.enabled": true,      // 顯示縮圖，方便長文章導覽
    "editor.wordWrap": "on"
  },

  // ==========================================
  // 2. 顏色微調設定（建立色彩區隔）
  // ==========================================
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      // --- 【一般文字檔 (.txt) 專用色彩】 ---
      {
        "scope": "text.plain",
        "settings": {
          "foreground": "#A7A7A7" // 溫和的鉛筆灰（在暗色主題下不刺眼，跟 Markdown 預設的亮白產生區隔）
        }
      },

      // --- 【Markdown (.md) 專用語法色彩】 ---
      {
        "scope": "markup.heading", // Markdown 標題
        "settings": {
          "foreground": "#FF8C00", // 鮮明橘色
          "fontStyle": "bold"
        }
      },
      {
        "scope": "markup.underline.link", // 超連結
        "settings": {
          "foreground": "#4fc3f7" // 天空藍
        }
      },
      {
        "scope": "markup.bold", // 粗體
        "settings": {
          "foreground": "#ff4081", // 亮粉色
          "fontStyle": "bold"
        }
      },
      {
        "scope": "markup.quote", // 引用區塊 (> 語法)
        "settings": {
          "foreground": "#81c784", // 柔和綠色
          "fontStyle": "italic"
        }
      },
      {
        "scope": "markup.inline.raw", // 行內程式碼 (`code`)
        "settings": {
          "foreground": "#ffeb3b" // 顯眼黃色
        }
      }
    ]
  }
}
```

## 💡 這樣設定後的效果：

1. **當你打開 `.txt` 檔案**：畫面會瞬間變得極度乾淨。行號消失了，字型變成了帶有文藝氣息的打字機等寬體，顏色是淡淡的灰色，沒有任何高亮，就像在用經典的實體記事本。
    
2. **當你打開 `.md` 檔案**：介面會恢復成專業的編輯器外觀。各級標題、粗體、連結都有鮮豔且層次分明的顏色，字型也是易於閱讀的現代黑體，一目了然。


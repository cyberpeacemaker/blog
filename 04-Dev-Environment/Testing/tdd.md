---
title: "TDD Coverage Requirement"
description: "Clarifies that an 80 percent line-coverage target measures test execution of new code, not whether AI can write code."
created: 2026-07-23
updated: 2026-07-23
tags: [dev]
type: concept
lang: zh
status: draft
---

> Related: [[MOC - Dev Environment]] · [[dry-run-pytest]] · [[boundary-edge]]

完全**不是**「不能用 AI 寫程式」的意思！別擔心，AI 依然是你的好夥伴。

這句話指的是軟體開發中的 **「測試覆蓋率（Code / Line Coverage）」**。

## 什麼是「新程式碼自身的行數大概要打到 80%」？

在 TDD（測試驅動開發）與自動化測試的語境下，「打到」是口語說法，意思是「達到 / 涵蓋到」。這句話的意思是：**你這次新增或修改的程式碼，至少要有 80% 的行數（Lines of Code）被單元測試執行（測試）過。**

### 舉個簡單例子：

- 假設你這次新增了一個 Python 函式，總共有 **100 行** 程式碼。
    
- 當你執行 `pytest` 並搭配測試覆蓋率檢查時：
    
    - 如果你的測試只測了主流程，只執行到了其中的 **50 行** 程式碼，那你的測試覆蓋率只有 **50%**（未達標 ❌）。
        
    - 如果你寫了更完整的測試（包含邊界條件、例外處理），讓跑測試時有 **80 行以上** 的程式碼被實際執行過，覆蓋率就達到了 **80%**（成功通關 ✅）。
        

## 那跟 AI 有關係嗎？

**完全無關。**

- **程式碼是誰寫的不重要**：不管是你自己一行一行敲出來的，還是請 AI 幫你生成的，系統只看**測試結果**與**涵蓋率**。
    
- **AI 甚至能幫你達標**：你可以把新寫好的程式碼丟給 AI，跟它說：「_請幫我針對這段程式碼寫 pytest 單元測試，注意要涵蓋到各種邊界狀況與 exception，測試覆蓋率要達到 80% 以上。_」
    

> **一句話總結**：這是一條**要求測試品質**的規定（程式碼要測滿 80% 的行數），而不是**限制工具**的規定（不限制能不能用 AI）。


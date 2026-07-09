---
created: 2026-07-09 20:07
updated: 2026-07-09 20:07
tags: []
type: reference
lang: en
status: draft
---
這條鐵則簡直是**軟體工程最佳實踐（Best Practice）的教科書範本**！

如果每個開發團隊都能嚴格執行這三點，世界上大概可以減少 80% 因為「在我的電腦上明明可以跑」而引發的工程師內鬨。這不是吹毛求疵，而是真正痛過的人才會寫出來的智慧結晶。

## 為什麼這條鐵則我給 100 分？

- **「永不用 system Python」是保命符：**
    
    動到作業系統（特別是 macOS 或 Linux）自帶的 Python，輕則套件版本衝突，重則直接讓系統工具罷工。把開發環境跟系統環境完全隔離，是專業開發者的基本素養。
    
- **點名 `conda run` 是老司機的做法：**
    
    很多人只知道 `conda activate`，但在寫自動化腳本、Cron job 或是 CI/CD 流程時，還要先想辦法在 Shell 裡啟動環境常常會卡住。這時候直接用 `conda run -n otex-claw <command>` 乾淨俐落，非常專業。
    
- **「立刻更新 `environment.yml`」是負責任的表現：**
    
    這走的是「基礎設施即程式碼（Infrastructure as Code）」的概念。新增依賴不立刻記錄，等過兩週別人拉下程式碼噴錯時，你早就忘記自己偷偷裝了什麼。立刻更新能確保團隊的協作順暢。
    

> 💡 **身為工程師隊友，我的一點小優化建議：**
> 
> 在更新 `environment.yml` 時，建議儘量只紀錄**核心依賴（Top-level dependencies）**，或者利用 `conda env export --from-history` 來匯出。如果把所有套件的詳細子版本號（甚至是特定的組建編號 build number）通通寫死，有時候在跨平台（例如 Windows 搬到 Linux，或 Intel 搬到 Apple Silicon）時反而會引發安裝災難。

這條規則立得非常精準。不過「鐵則」最大的敵人通常不是技術，而是**人性的懶惰**。

這套規則目前在你們團隊執行得順利嗎？大家有沒有常常因為忘記更新 `environment.yml` 而被檢討？


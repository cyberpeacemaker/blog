---
title: "GitHub Actions Sensitive Patterns"
description: "Explains how CI can scan with sensitive-pattern rules via GitHub Secrets and the associated trust tradeoffs."
created: 2026-07-14 17:07
updated: 2026-07-14 17:07
tags: [dev, git, workflow]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Dev Environment]] · [[github-action-flaws]] · [[github-action-workflows]]

簡單直接的答案：**是的，GitHub CI 絕對需要這份 sensitive patterns 才能做檢查。**

  

這裡的意思是，雖然這份檔案「不能推進 Git 倉庫（Repo）裡」，但 GitHub CI 在運作時，依然必須要有這份規則才能幫忙抓出有沒有人犯錯。

  

為了同時滿足「CI 要檢查」**和**「內容要保密」這兩個衝突的條件，這個專案採用了 **GitHub Secrets** 的機制。以下是它背後的運作邏輯與設計含意：

  

---

  

### 1. 它是怎麼在不進 Repo 的情況下讓 CI 檢查的？

  

運作流程是這樣的：

  

1. **Owner 手動設定：** 專案負責人（Owner）把本機那份敏感字串清單複製起來，貼進 GitHub 專案設定裡的 `Settings -> Secrets and variables -> Actions`，命名為 `SENSITIVE_PATTERNS`。

2. **CI 執行時動態載入：** 當你開 PR 或 push 時，GitHub Actions 啟動，CI 腳本會動態把這個 Secret 的內容抓出來，在記憶體中（或暫存檔）還原成那份清單。

3. **進行掃描：** CI 用這份還原的清單去掃描你這次改動的程式碼（Diff）。

4. **結束抹除：** 檢查完後，虛擬機直接銷毀，這份清單不會留下任何痕跡，也不會進到 Git 歷史紀錄裡。

  

---

  

### 2. 「Secret 沒設 → CI 直接紅」是什麼意思？

  

這是一種 **「安全失敗（Fail-Secure）」** 的防禦性程式設計思維。

  

假設今天某個新管理者不小心把 GitHub 裡的 `SENSITIVE_PATTERNS` Secret 刪掉了，或者改名字了：

  

* **不安全的設計：** CI 找不到清單，就當作「沒規則要檢查」，直接顯示綠燈（Pass）。結果就是接下來所有包含真實 IP、真實 Token 的危險代碼全部被直接合進 main。

* **本專案的設計（直接紅）：** CI 腳本一啟動，發現「根本拿不到 `SENSITIVE_PATTERNS` 的內容（缺失或空白）」，CI 就**強行中止並直接報錯流產（變紅燈）**。

  

> 💡 **核心邏輯：** 寧可因為沒設定好而防衛性地卡死所有人（直接紅），也絕對不允許在「沒有保護盾」的情況下讓程式碼盲目通關。

  

---

  

### 總結

  

GitHub CI **需要**這份資料。文中所說的，是提醒維護者（Owner）如果在 GitHub 那邊忘記設定這個祕密變數（Secret），CI 就會整條壞掉變紅燈，用這種強硬的方式逼管理者一定要把安全機制設好。

  

---

  

你非常敏閱！這直接點破了近代 CI/CD（持續整合/部署）安全性中最核心的 **「信任邊界」與「資安權衡（Trade-off）」** 問題。

  

直覺上，把號稱機密的檔案傳到 GitHub 的伺服器上，確實讓人心驚肉跳。但實務上，這個設計在「自動化檢查的便利性」與「機密性」之間，透過幾道技術與管理機制做了妥協。

  

我們可以從以下三個維度來剖析：為什麼它沒有「完全失去機密性」，以及它真正的風險在哪裡。

  

---

  

## 1. GitHub Secrets 的加密機制（技術防禦）

  

GitHub Actions 的 Secrets 不是以明文存放在 GitHub 的資料庫裡，也不是隨便一個能進 Repo 的人都能點開來看。

  

* **單向加密（Write-Only）：** 當 Owner 把 `sensitive-patterns` 貼進 GitHub Secrets 後，任何人都**無法再從網頁介面上點開、編輯或複製它**。它被以非對稱加密（NaCl sealed boxes）鎖死，只有當 CI 虛擬機啟動、執行那段特定的掃描腳本時，才會在記憶體中短暫解密。

* **自動遮罩（Masking）：** GitHub Actions 如果在 log 中偵測到 Secret 的內容，會自動把它變成 `***`。

  

---

  

## 2. 為什麼你的擔憂是對的？（真正的攻擊面）

  

你的直覺完全正確：**只要資料離開了本機、上了雲端，就有被竊取的風險。**

  

在 CI/CD 安全中，有一種經典的攻擊叫 **「Secret Exfiltration（憑證外洩）」**。如果專案允許任何人自由開 PR，壞人可以寫一個惡意的 CI 腳本（例如：`cat $SENSITIVE_PATTERNS | base64` 或把內容用 `curl` 傳到外部伺服器），這樣就能把 Secret 偷走。

  

為了防範這個漏洞，這份 Devkit 在前幾段其實埋了對應的**硬性防線**（見 §1、§7、§10）：

  

* **Private Repo 且禁止 Fork：** 這排除了外部陌生人隨意開 PR 來「投毒」執行惡意腳本的可能。

* **嚴格的 Branch Protection（分支保護）：** `main` 分支不能直接 push，所有 PR 必須經過至少 1 個成員 Review。如果有人意圖修改 `.github/workflows/ci.yml` 去偷看這個 Secret，Reviewer 在審查程式碼時就會立刻發現。

* **GitHub 預設防禦：** GitHub 預設不會把 Secrets 傳給來自 Fork 倉庫的 PR 工作流（雖然此專案已明令禁止 Fork）。

  

---

  

## 3. 內容屬性的差異：Regex vs. 真正密碼

  

這份檔案之所以敢放 GitHub Secrets，是因為它裝的是 **「Regex（正規表達式規則）」**，而不是 `.env` 裡面的「真實帳號密碼/Token」。

  

* **`.env`（絕對不能上雲）：** 裡面是合法的 API Key，拿到就能立刻控制系統。

* **`sensitive-patterns`（相對機密）：** 裡面是 `172.16\.\d+\.\d+` 或 `.*-prod-db.*` 這類的特徵。雖然它洩漏了公司的「內網架構、主機命名慣例」（所以也是機密），但它本身**不是直接進入系統的鑰匙**。

  

---

  

## 評估與總結

  

這是一個**資安的權衡**：

  

> **如果不放 GitHub CI：** 萬一某個成員繞過本機 Hook（例如用了 `git push --no-verify`），或者用手機在網頁端直接改 Code，敏感字串就會**直接被推上 main 分支，永久留在 Git 歷史紀錄中**。這對公司的災難更大。

> **如果放 GitHub CI：** 我們承擔了「信任 GitHub 平台」以及「防止內賊改 CI 腳本」的風險，但換來了 100% 擋下敏感資料進 Repo 的絕對防禦。

  

在目前的軟體工程中，只要搭配好**分支保護（Branch Protection）**與**程式碼審查（Code Review）**，使用 GitHub Secrets 被視為符合業界標準的資安實踐。

  

既然這個安全機制非常依賴「程式碼審查」，你覺得這份 Devkit 中設計的兩個內建評審工具（`.claude/agents/` 裡的 `code-reviewer.md`）是否足夠在自動化階段就幫忙把關這類惡意的 PR 變更？


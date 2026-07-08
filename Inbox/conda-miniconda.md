---
created: 2026-07-08 19:07
tags: []
type: reference
lang:
status: draft
---
沒問題！既然你已經在 Windows 11 上裝好了，接下來我們就來聊聊這個在 Data Science（資料科學）和 AI 領域幾乎人手一套的工具。

簡單來說，**Conda 是「本體（核心引擎）」，而 Miniconda 是「輕量化包裝」**。

## 概念釐清：Conda、Miniconda、Anaconda 的關係

你可以用「買車」來比喻這三者的關係：

- **Conda（引擎）**：它是一個**套件管理**與**虛擬環境管理**的系統。它不只管 Python，還能管 C/C++ 函式庫、甚至是 Node.js 套件。
    
- **Miniconda（陽春版空車）**：只包含 Conda 核心、Python 以及極少數基礎套件。體積小（約 100 MB 內），**你想裝什麼再自己裝，最推薦開發者使用**。
    
- **Anaconda（豪華全配版 SUV）**：包含 Conda、Python，並**預裝了上千個**資料科學、機器學習常用的套件（如 NumPy, Pandas, Jupyter Notebook）。體積龐大（3 GB 以上），很多套件你一輩子可能都用不到。
    

## Conda 的優點與缺點 (Pros & Cons)

### 優點 (Pros)

1. **強大的環境隔離**：專案 A 需要 Python 3.8，專案 B 需要 Python 3.11？Conda 可以幫你各建一個獨立房間（虛擬環境），兩邊老死不相往來，絕不打架。
    
2. **搞定複雜的二進位依賴（底層 C/C++ 庫）**：這也是它完勝 Python 原生 `pip` 的地方。像 PyTorch、TensorFlow 等 AI 套件，底層需要複雜的 C++ 或是 NVIDIA CUDA 驅動支援。用 `pip` 常裝到崩潰，用 `conda` 通常一條指令就幫你把底層全部配好。
    
3. **跨語言管理**：不只能裝 Python 套件，連非 Python 的工具（例如特定的 C 語言編譯器、甚至 Node.js）都能直接裝在虛擬環境裡。
    
4. **不需要系統管理員權限**：它完全安裝在你的使用者資料夾下，不會弄髒 Windows 的系統環境變數。
    

### 缺點 (Cons)

1. **分析依賴時間較長**：當你環境裡套件愈裝愈多，Conda 在安裝新套件時會花比較多時間去「計算」各套件版本有沒有衝突（不過近年引進 libmamba 引擎後已大幅改善）。
    
2. **佔用硬碟空間**：因為每個虛擬環境都是完全獨立的拷貝，如果建很多環境，硬碟空間會吃得比較快。
    
3. **與 `pip` 混用可能會有小衝突**：有時在 Conda 環境裡用 `pip install` 裝套件，可能會讓 Conda 暫時失去對該套件的版本控制。
    

## 什麼時候該用 Conda？(使用時機)

- **該用 Conda 的時機**：
    
    - 你要玩 **AI、機器學習、深度學習**（需要用到 PyTorch, TensorFlow, Scikit-learn）。
        
    - 你要做 **資料分析**（NumPy, Pandas, Matplotlib）。
        
    - 你的多個專案需要**不同的 Python 版本**切換。
        
- **不一定要用 Conda 的時機（可以用原生 `venv` + `pip`）**：
    
    - 純寫網頁後端（如 Django, Flask, Fastapi）或寫簡單的自動化爬蟲腳本。這些專案不需要底層複雜的 C 語言庫，用 Python 內建的 `venv` 更輕量快速。
        

## Conda 實用指令懶人包（每天都會用到）

請在你的 PowerShell 中玩玩看以下指令：

### 1. 建立新的虛擬環境

建立一個名字叫 `myenv`，且指定 Python 版本為 3.10 的環境：

PowerShell

```
conda create --name myenv python=3.10
```

### 2. 切換/啟動環境

要進入剛剛建好的房間：

PowerShell

```
conda activate myenv
```

_(啟動後，你會發現命令列最前方的 `(base)` 變成了 `(myenv)`)_

### 3. 在環境中安裝套件

進入環境後，就可以安裝你需要用的工具（例如安裝資料分析必備的 pandas）：

PowerShell

```
conda install pandas
```

### 4. 離開目前環境

工作結束了，想回到外面的世界（base 環境）：

PowerShell

```
conda deactivate
```

### 5. 查看目前有哪些環境

忘記自己建過哪些房間了？

PowerShell

```
conda env list
```

### 6. 刪除環境

這個專案結束了，想把房間拆掉省空間：

PowerShell

```
conda env remove --name myenv
```

有了 Miniconda 之後，你就可以針對每個不同的專案建立乾淨、獨立的開發環境了。你接下來是打算開發什麼樣的專案呢（例如：AI 模型、網頁開發、還是特定的前端/後端整合）？


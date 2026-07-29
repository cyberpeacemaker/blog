---
title: "AI Knowledge Compression Terms"
description: "Organizes English terms for condensing, pruning, mining, embedding, and structuring knowledge in AI contexts."
created: 2026-07-28
updated: 2026-07-28
tags: [ai]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - AI Agents]] · [[edge-ai-terms]] · [[context-management]]

原來你是在找更多關於「知識提煉、萃取、濃縮」相關的英文技術詞彙！

在 AI、機器學習與資料科學中，除了 Distill、Extract、Core、CapNet 之外，還有許多精準描述「將雜亂/龐大的資訊或模型，結晶為高價值精華」的關鍵詞。我幫你按技術情境分類整理如下：

### 一、模型與知識的「精煉與濃縮」（Refinement & Compression）

- **Condense / Condensation（濃縮）**
    
    - **代表詞**：Dataset Condensation（資料集濃縮）、Knowledge Condensation
        
    - **含意**：將原本數 GB 的巨量資料集，資訊「濃縮」成極少量的合成資料點（Synthetic Data），但能訓練出效果幾乎相同的模型。
        
- **Prune / Pruning（剪枝）**
    
    - **代表詞**：Model Pruning（模型剪枝）
        
    - **含意**：將模型中不重要、冗餘的神經元或權重剔除，就像修剪樹枝一樣，只保留最核心的推理神經網路。
        
- **Quantize / Quantization（量化）**
    
    - **代表詞**：Weight Quantization
        
    - **含意**：將高精度的模型參數（如 FP32）壓縮成低精度（如 INT4/INT8），在幾乎不損失智力的前提下大幅縮小體積，將知識結晶為極輕量的形式。
        
- **Synthesize / Synthesis（合成/提煉）**
    
    - **代表詞**：Knowledge Synthesis（知識合成）
        
    - **含意**：不只是複製原始資訊，而是將多方知識融合後「合成」出更高密度的知識摘要或高品質訓練資料。
        

### 二、資料與事實的「挖掘與收割」（Mining & Harvesting）

- **Mine / Mining（探勘/挖掘）**
    
    - **代表詞**：Text Mining（文本探勘）、Data Mining、Opinion Mining
        
    - **含意**：就像採礦一樣，從海量的無結構資料噪訊（Noise）中，挖掘出具有價值的隱含規律或黃金知識（Knowledge Gold）。
        
- **Harvest / Harvesting（收割/採集）**
    
    - **代表詞**：Knowledge Harvesting（知識收割）
        
    - **含意**：指自動化地從網頁、文件或論壇中「採集」專家知識並整理成結構化資料庫的過程。
        
- **Parse / Parsing（解析/剖析）**
    
    - **代表詞**：Dependency Parsing（句法剖析）、AST Parsing
        
    - **含意**：將雜亂無章的字串解構，按照語法或邏輯規則剔除贅詞，結晶出最底層的樹狀邏輯結構。
        

### 三、概念與語意的「抽象化與向量結晶」（Abstraction & Representation）

- **Abstract / Abstraction（抽象化）**
    
    - **代表詞**：Feature Abstraction（特徵抽象）、Abstractive Summarization（抽象式摘要）
        
    - **含意**：從具體的低階細節（如影像像素、文章字詞）中，提煉出高階的高維概念或主旨。
        
- **Embed / Embedding（嵌入/向量化）**
    
    - **代表詞**：Text Embedding、Graph Embedding
        
    - **含意**：將複雜的文本、實體或知識關係，壓縮並「結晶」為高維空間中的一個數學向量，把語意資訊高度濃縮在幾百個數字中。
        
- **Disentangle / Disentanglement（解耦/解纏）**
    
    - **代表詞**：Disentangled Representation（解耦特徵表徵）
        
    - **含意**：將交織在一起的複雜概念拆解開來。例如將一張照片結晶為獨立的「姿勢」、「表情」、「光影」三個獨立維度，各司其職。
        
- **Ontology（本體論/知識本體）**
    
    - **代表詞**：Ontology Building（本體建構）
        
    - **含意**：將某個領域的所有知識概念、分類與相互關係，定義成一套標準的階層結構，是知識庫結晶的最高形式之一。
        

### 快速對照總結

|**詞彙 (Term)**|**動作隱喻**|**結晶後的產物**|
|---|---|---|
|**Condense**|將大體積壓縮為小體積|高密度濃縮資料/知識|
|**Prune**|剪掉樹枝只留主幹|輕量化神經網路|
|**Mine / Harvest**|採礦與收割|關鍵情報、實體資料|
|**Embed**|將萬物轉化為高維點|語意向量 (Vector)|
|**Disentangle**|整理打結的線團|獨立且清晰的概念維度|
|**Ontology**|建造知識的大廈骨架|結構化的知識本體|

這些詞彙中，有哪一個方向（例如模型輕量化、資料採集、或是概念向量化）最貼近你目前的想法呢？


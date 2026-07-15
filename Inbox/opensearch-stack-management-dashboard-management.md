---
created: 2026-07-15 14:07
updated: 2026-07-15 14:07
tags: []
type: reference
lang: en
status: draft
---
在 OpenSearch 中，由於它是從 Elasticsearch/Kibana（7.10.2 版本）分支（Fork）獨立出來的項目，因此介面上的**專有名詞與 Kibana 有所不同**：

- **Kibana 的舊/新路徑**：`Stack Management` ➡️ `Data Views`（或 Index Patterns）
    
- **OpenSearch 的對應路徑**：`Dashboards Management`（或 `Management`） ➡️ **`Index Patterns`（索引模式）**
    

以下為您詳細整理在 OpenSearch 中「進入、建立與管理」此功能的操作步驟與核心重點：

## 1. 如何進入 OpenSearch 的 Index Patterns 頁面

請依照以下路徑在 OpenSearch Dashboards（網頁介面）中找到該功能：

1. **開啟側邊選單**：點擊左上角的「主選單」按鈕（三條橫線的圖示 `☰`）。
    
2. **尋找管理功能**：滑到選單最下方，點擊 **Management**（管理）區塊底下的 **Dashboards Management**。
    
3. **進入索引模式**：在左側選單中點擊 **Index Patterns**。
    
    > _註：在某些 OpenSearch 版本中，選單結構可能簡化為直觀的 `Management` ➡️ `Index Patterns`。_
    

## 2. 如何建立新的 Index Pattern（Data View）

進入該頁面後，若要讓 OpenSearch 可以搜尋並呈現您的資料，必須建立一個 Index Pattern：

### 步驟一：定義索引模式（Define Index Pattern）

- 點擊右上角的 **Create index pattern** 按鈕。
    
- 在 **Index pattern name** 輸入框中輸入要匹配的索引名稱。
    
    - **實用技巧**：通常會搭配萬用字元 `*`。例如，若您的索引依日期命名為 `logs-2026-07-14`、`logs-2026-07-15`，請輸入 `logs-*`，即可一次比對並彙整所有相關索引。
        
- 輸入後，系統會自動在下方顯示成功匹配的索引。確認無誤後，點擊 **Next step**。
    

### 步驟二：配置時間篩選（Configure Settings）

- **Time field**（時間欄位）：從下拉選單中選擇要作為時間過濾依據的欄位（最常見的是 `@timestamp`）。
    
    - _注意：如果您的資料沒有時間軸，可以選擇 "I don't want to use the time filter"，但這會導致您在 Discover（探索）功能中無法使用右上角的時間範圍篩選器。_
        
- 點擊 **Create index pattern** 完成。
    

## 3. Index Pattern 介面功能詳細拆解

建立完成後，您會進入該 Index Pattern 的管理後台，這裡包含三個主要的頁籤：

|**頁籤名稱**|**說明**|**常用情境**|
|---|---|---|
|**Fields** (欄位列表)|顯示此模式下所有被索引的欄位、資料型態（Type）以及是否可搜尋（Searchable）/ 彙整（Aggregatable）。|確認特定欄位是否被正確解析成 `date`、`number` 或 `string`（如 `<field>.keyword`）。|
|**Scripted fields** (腳本欄位)|允許您使用 Painless 腳本在查詢時動態計算出新欄位。|例如：將 `first_name` 和 `last_name` 欄位在呈現時合併為 `full_name`。|
|**Source filters** (來源過濾器)|允許您在 Discover 載入資料時，過濾掉不需要的大型欄位以提升效能。|排除某些極大、平常不用於視覺化分析的原始 JSON 欄位（如 `raw_payload`）。|

## 💡 實用維護小秘訣

> ⚠️ **寫入新資料後，欄位沒有出現在 Dashboards 中？**
> 
> 如果您事後往 OpenSearch 寫入了新欄位，但在 Discover 搜尋不到，**請不要刪除重新建立 Index Pattern**。
> 
> 您只需進入該 Index Pattern 的詳細管理頁面，點擊右上角的 **「重新整理（Refresh field list）」循環箭頭圖示**，系統就會自動同步並更新最新的 Mapping 結構！

> 🌟 **設定預設 Index Pattern**
> 
> 如果您建立了多組模式，可以點擊右上角的 **「星星」圖示**（Set as default index pattern）將其設為預設。這樣每次點開 `Discover` 頁面時，系統就會優先載入該組資料。

您目前是準備在 OpenSearch 中為新寫入的 Log 資料建立檢視，還是遇到了欄位類型（例如 `text` 與 `keyword`）無法正確顯示或進行彙整的問題呢？


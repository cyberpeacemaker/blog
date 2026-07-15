---
created: 2026-07-15 09:07
updated: 2026-07-15 09:07
tags: []
type: reference
lang: en
status: draft
---
這個「重組（Reassembly）」機制是 Wireshark 解析應用層協定（如 HTTP、HTTPS、FTP、gRPC 等）時最核心、也最強大的功能之一。

當我們在傳輸大檔案、長 JSON 字串或大張圖片時，應用層的資料（如 HTTP Response）往往會超過乙太網路的 **MTU（最大傳輸單元，通常是 1500 位元組）**。因此，TCP 協定在傳輸時，必須把這段大資料拆成好幾個 **TCP Segments（分段）** 發送。

以下為你深度拆解 Wireshark 在背後偷偷幫你做的「重組魔法」，以及你該如何善用它：

## 🛠️ 運作原理：誰是「重組發起者」與「最後完成者」？

在 TCP 傳輸中，Wireshark 是這樣默默工作的：

### 1. 「工具人」封包與「收割者」封包

- **工具人封包（例如 Frame 8）：**
    
    當收到前段資料時，Wireshark 知道這段資料還沒完（它會去計算 TCP Sequence Number 和 HTTP 的 `Content-Length`）。這時，Wireshark 在主畫面的 `Protocol` 欄位通常只會顯示 **`TCP`**，而 `Info` 欄位會標示：
    
    > `[TCP segment of a reassembled PDU]`（重組協定資料單元中的一個 TCP 分段）
    > 
    > 這代表此封包只是「拼圖的其中一塊」，Wireshark 此時還無法解析出完整的 HTTP 內容。
    
- **收割者封包（例如 Frame 9）：**
    
    當最後一個分段抵達，拼圖終於完整了。Wireshark 會把這個封包的 `Protocol` 標示為 **`HTTP`**（或對應的應用層協定）。
    
    **重組的完整資料，會被統一掛載在「這最後一個封包」身上。** 這就是為什麼你在選取 Frame 9 時，才能在 Detail 面板看到那行 `[2 Reassembled TCP Segments]`。
    

## 💻 隱藏細節：Packet Bytes 面板的「頁籤（Tabs）」

當你選取 Frame 9（最後一個封包）時，請看 Wireshark 介面**最下方**的十六進位檢視區（Packet Bytes 面板）。你會發現它多了好幾個分頁標籤可以切換：

- **`Frame` 頁籤：**
    
    只顯示 Frame 9 **這一個封包實際在網路上傳輸的原始資料**（不包含 Frame 8 的部分）。
    
- **`Reassembled TCP` 頁籤：**
    
    這是 Wireshark 幫你把 Frame 8 和 Frame 9 的 Payload 拼接好之後的**完整合成資料**。你在 Follow Stream 裡面看到的乾淨資料，就是從這個頁籤來的。
    

## ⚙️ 核心設定：如何開啟或關閉這個功能？

有時候，身為網路工程師，你可能會想看到「最原始、沒被重組過」的 TCP 樣貌，這時你可以手動控制這個功能。

1. 在 Wireshark 選單中點擊：**Edit** -> **Preferences**（偏好設定）。
    
2. 在左側展開 **Protocols**，找到 **TCP**。
    
3. 在 TCP 的設定頁面中，你會看到這兩個關鍵核取方塊：
    
    - **`Allow subdissector to reassemble TCP streams`**（允許子解析器重組 TCP 串流）：
        
        這是總開關。如果取消勾選，Wireshark 就不會幫你把多個 TCP 包拼起來，你將看不到 `[Reassembled TCP Segments]` 的超連結。
        
4. 同理，在 Protocols 裡面找到 **HTTP**，也有相關的設定：
    
    - **`Reassemble HTTP headers spanning multiple TCP segments`**
        
    - **`Reassemble HTTP bodies spanning multiple TCP segments`**
        

> **💡 實戰建議：**
> 
> 平常請務必保持**開啟**（預設也是開啟的），這能極大程度地幫你省下人工比對 Sequence Number、手動拼接 Hex 值的痛苦時間。

## ⚠️ 避坑指南：TCP 重組（Reassembly）vs IP 分片（Fragmentation）

很多人常把這兩者搞混，但在 Wireshark 裡它們代表完全不同的事：

|**比較項目**|**TCP Reassembly (重組)**|**IP Fragmentation (分片)**|
|---|---|---|
|**發生層級**|**Layer 4（傳輸層）** / **Layer 7（應用層）**|**Layer 3（網路層）**|
|**原因**|應用層資料太大，TCP 貼心地在主機端主動拆分。|封包大於實體路徑上某台路由器的 MTU，在傳輸途中被路由器強行切碎。|
|**Wireshark 標示**|`[Reassembled TCP Segments]`|`[Reassembled IPv4 fragments]`|

你在截圖中看到的是 **TCP Reassembly**，這是最健康、最常見的狀態。

你想進一步了解當網路發生「丟包（Packet Loss）」或「亂序（Out-of-Order）」時，Wireshark 的重組機制會如何呈現，還是你想實際操作一次如何把重組後的完整檔案（例如圖片或 PDF）直接從 Wireshark 匯出保存呢？


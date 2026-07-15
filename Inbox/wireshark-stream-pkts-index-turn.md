---
created: 2026-07-15 09:07
updated: 2026-07-15 09:07
tags: []
type: reference
lang: en
status: draft
---
這是一個非常經典且重要的 Wireshark 觀念問題！這涉及到「底層網路傳輸」**與**「上層應用程式解讀」之間的差別。

以下為你詳細解析這兩個疑問：

## 1. `pkts` 與 `packets` 的關係是什麼？

- **它們是同一個詞！**
    
    `pkts` 單純只是 `packets`（封包）的**英文簡寫**（Abbreviation）。
    
    因此，`17 client pkts` 與 `17 client packets` 代表的是完全一樣的意思。
    

## 2. 為什麼主介面有 172 個封包，但追蹤視窗裡只有 33 個（17 + 16）？

你開啟的視窗標題是 **「Follow HTTP Stream」**（追蹤 HTTP 資料流）。Wireshark 在這個模式下，看的是「重組後的應用層（HTTP）資料」，而不是「網路上跑的所有原始 TCP 封包」。

導致數量對不上的主要原因有以下三個：

### ① 過濾掉了「不含資料」的 TCP 控制封包

在 TCP 連線中，有大量的封包**不攜帶任何實際的 HTTP 資料**，它們只負責維持連線的狀態。在「Follow Stream」視窗中，這些沒有 Payload（承載資料）的封包會被直接過濾掉、不計入統計。

- **連線建立**：三次握手（Three-way Handshake）的 `SYN`、`SYN-ACK`、`ACK`。
    
- **純確認封包（Pure ACKs）**：當 A 端傳資料給 B 端後，B 端回傳一個沒有資料的 `ACK` 封包來報平安。
    
- **連線中斷**：結束連線時的 `FIN`、`RST` 封包。
    

> 在你主畫面的 172 個封包中，很大一部分只是這類「不帶資料的工具包」。

### ② TCP 的重組（Reassembly）機制

- 網路傳輸有最大傳輸單元（MTU，通常為 1500 位元組）的限制。
    
- 如果伺服器要回傳一個 16 KB 的 HTTP 網頁資料（如你選單顯示的 Entire conversation 16 kB），它**無法**塞進單一個 TCP 封包裡，而是會被拆成大約 11~12 個獨立的 TCP 封包傳送。
    
- Wireshark 在呈現 「Follow HTTP Stream」時，會貼心地把這 12 個分段封包**重組（Reassemble）還原成 1 個完整的 HTTP 回應**。在 Follow 統計中，這 12 個原始封包就會被合併計算為 **1 個 server pkt**。
    

## 3. 從你的 YAML 截圖中尋找鐵證 🔍

如果你仔細觀察截圖中 YAML 格式的 `packet` 序號，就會發現它們是**跳號**的：

YAML

```
- packet: 1   # 用戶端傳送的第一個「有資料」的封包 (peer: 0)
- packet: 4   # 中間的 packet 2、3 沒出現（因為它們是沒有資料的純 ACK 或控制封包）
- packet: 9   # 伺服器端回傳的第一個「有資料」的封包 (peer: 1)
- packet: 15  # 下一個... 中間的 10~14 被重組或過濾掉了
```

這非常清楚地說明了兩者的差別：

> - **主視窗顯示的 172 packets**：是網路上跑的**所有原始 TCP 封包**（包含握手、純 ACK、被拆散的分段封包）。
>     
> - **底部的 33 pkts（17 client + 16 server）**：是 Wireshark 幫你過濾與重組後，**真正含有 HTTP 應用層資料的「對話次數」**。
>


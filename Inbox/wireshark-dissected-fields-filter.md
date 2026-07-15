---
created: 2026-07-15 09:07
updated: 2026-07-15 09:07
tags: []
type: reference
lang: en
status: draft
---
答案是：**不行，這個 `index` 沒有辦法直接設成 Wireshark 的過濾器（Display Filter）。**

這背後有一個非常重要的 Wireshark 運作邏輯，理解它之後，你對 Wireshark 的掌控度會再提升一個檔次！

## 為什麼不能設成過濾器？

在 Wireshark 中，**不是所有出現在螢幕上的字都能拿來當過濾器**。

### 1. 過濾器只能過濾「解析欄位（Dissected Fields）」

Wireshark 的過濾器（例如 `ip.src == 192.168.1.1` 或 `tcp.port == 80`）是建立在封包解碼器（Dissector）**之上的。只有當欄位存在於封包本身的表頭（Header）、Payload，或者是 Wireshark 解碼後顯示在**左下角「Packet Details（封包細節）」面板裡的欄位，才能被當作過濾器。

### 2. `index` 是「匯出格式專屬的虛擬欄位」

這個 `index` 是你在使用 "Follow Stream" 視窗並選擇「YAML 格式」時，Wireshark 的**匯出引擎臨時產生出來的「虛擬計數器」**。

- 它用來記錄「這是該發言者（Peer）在這次對話中**發送的第幾次資料塊**」（例如 Client 第一次發送是 `index: 0`，第二次發送是 `index: 1`）。
    
- 這個數值**不存在於實際的網路封包中**，Wireshark 的 Packet Details 面板裡也沒有這個欄位，因此過濾器引擎根本不認識 `index` 這個字。
    

## 💡 替代方案：如何用其他過濾器達到「精確定位」的目的？

雖然不能過濾 `index`，但既然你的目標是「在茫茫封包海中，快速找出對應的封包」，你可以使用以下三種超實用的過濾器替代方案：

### 方案 A：直接過濾「封包編號」（最快、最直覺）

在 YAML 中，`index` 的上方一定會配一個 `packet`。這個 `packet: 9` 代表的就是原始封包編號（Frame Number）。

- **過濾器語法：**
    
    Plaintext
    
    ```
    frame.number == 9
    ```
    
    _(這會讓 Wireshark 畫面只顯示第 9 號封包。)_
    

### 方案 B：過濾「特定方向的對話（peer）」

如果你想在主畫面中，只看 Client 發出的訊息（對應 `peer: 0`），或是只看 Server 回應的訊息（對應 `peer: 1`）：

- **過濾 Client 發送的封包（假設 Stream 編號是 0）：**
    
    Plaintext
    
    ```
    tcp.stream == 0 && ip.src == 192.168.65.69
    ```
    
- **過濾 Server 回應的封包：**
    
    Plaintext
    
    ```
    tcp.stream == 0 && ip.src == 10.99.40.20
    ```
    

### 方案 C：過濾「含有特定資料」的封包

如果你知道 `index: 0` 的那段 `data` 裡含有某些特定字串（例如 `POST /beacon` 或是 Base64 的開頭 `eyJ`），你可以直接過濾 Payload 內容：

- **過濾 TCP 內容含有特定字串的封包：**
    
    Plaintext
    
    ```
    tcp.payload contains "eyJ"
    ```
    
- **如果是 HTTP 協定，過濾 HTTP 內容：**
    
    Plaintext
    
    ```
    http contains "beacon"
    ```


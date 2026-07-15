---
created: 2026-07-15 08:07
updated: 2026-07-15 08:07
tags: []
type: reference
lang: en
status: draft
---
**沒錯，你完全抓到最核心的關鍵了！**

你看到的「重組（Reassembly）」，本質上就是因為資料**已經超過了 TCP 封包的單次傳輸限制**，在發送端被強行拆成了多個 TCP 封包，而 Wireshark 只是在接收端幫你把這些碎片「還原」而已。

為了讓你更清楚這個過程，我們來拆解一下這個「拆分與重組」的幕後機制。

## 📏 限制的源頭：為什麼會被拆？（MTU 與 MSS）

在網路上，TCP 絕對不可能一次傳送無限大的資料（例如一個 10MB 的檔案或 5KB 的 JSON）。它受到以下兩個嚴格的物理與協定限制：

1. **MTU（最大傳輸單元，Maximum Transmission Unit）：**
    
    這是實體網路（如乙太網路）的限制，通常是 **1500 位元組（Bytes）**。任何超過這個大小的 IP 封包都無法在網路上傳輸。
    
2. **MSS（最大分段大小，Maximum Segment Size）：**
    
    這是 TCP 協定扣除標頭後，**單一封包真正能裝載應用層資料（Payload）的最大容量**。
    
    - 計算公式很簡單：`MTU (1500) - IP 標頭 (20) - TCP 標頭 (20) = 1460 位元組`。
        

> 💡 **結論：** 只要你傳送的應用層資料（如 HTTP Response）**大於 1460 位元組**，就必定會被 TCP 拆編成多個封包發送。

## 🎬 實戰模擬：5000 位元組的 HTTP 回應是如何被拆與組的？

假設 Server 要傳給 Client 一個 **5000 位元組** 的 HTTP 網頁資料，TCP 運作流程如下：

### 1. 發送端（Server）強行拆分：

TCP 發現 5000 遠大於 MSS（1460），於是開始切蛋糕：

- **第一個 TCP 封包**：裝載 1460 載荷（Payload）
    
- **第二個 TCP 封包**：裝載 1460 載荷
    
- **第三個 TCP 封包**：裝載 1460 載荷
    
- **第四個 TCP 封包**：裝載剩餘的 620 載荷
    

這 4 個 TCP 封包會在網路上獨立傳輸。

### 2. 接收端（Wireshark）默默重組：

當這 4 個封包抵達並被 Wireshark 捕獲時，它們在軟體中會呈現為 4 個獨立的 **Frame（幀/封包）**：

- **Frame 1, 2, 3**：Wireshark 的 Protocol 欄位只會顯示 `TCP`，因為它們只是「不完整的碎片」。
    
- **Frame 4**：當最後一個碎片抵達，Wireshark 終於能完整拼出那 5000 位元組的 HTTP 回應了！
    
- 此時，Wireshark 會將 **Frame 4** 的 Protocol 標示為 `HTTP`，並在細節面板（Packet Details）寫上：
    
    > `[4 Reassembled TCP Segments (5000 bytes): #1(1460), #2(1460), #3(1460), #4(620)]`
    

這也就是為什麼你點擊最後一個 Frame，就能透過超連結反向看到前面那 3 個幫忙載運資料的「工具人」封包。

## 📦 釐清名詞：Frame（幀）與 Packet（封包）的套娃關係

你提到「這只是 frame 的重組」，這在網路層級上是非常精準的說法。我們常說的 Frame、Packet、Segment 其實是像俄羅斯套娃一樣包在一起的：

$$\text{Frame (資料連結層)} \supset \text{Packet (網路層/IP)} \supset \text{Segment (傳輸層/TCP)} \supset \text{Data (應用層/HTTP)}$$

Wireshark 抓到的是最外層的 **Frame**，而它透過解析裡面的 TCP **Segment** 的序號（Sequence Number），幫你拼回最核心的 **HTTP Data**。

既然知道了重組的原理，你是否想了解如果傳輸過程中不幸發生了「丟包（Packet Loss）」或「延遲」，Wireshark 會在重組時呈現什麼樣的錯誤標示（例如 TCP ACKed unseen segment 或 Dup ACK）？


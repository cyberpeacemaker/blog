---
title: "Wireshark TCP Reassembly"
description: "Explains Wireshark TCP reassembly, reassembled PDU packets, and the distinction from IP fragmentation."
created: 2026-07-15 09:07
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [nsm, wireshark, malcolm]
---

> Related: [[MOC - Malcolm & NSM]] · [[wireshark-contain]] · [[ip-fragmentation-evasion]]

# Wireshark TCP Reassembly
## Source: `Inbox/wireshark-tcp-reaseembly-ip-fragmentation.md`

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

## Source: `Inbox/reassembled-tcp-segments.md`

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

## Source: `Inbox/wireshark-stitch-up-tcp-session.md`

The process behind this "magic" is called **TCP Reassembly** (or desegmentation). It is a collaborative effort between Wireshark’s TCP analysis engine and the application-layer parser (called a "dissector").

Here is exactly how Wireshark stitches those frames together step-by-step:

## Step 1: Grouping the Conversation (The 4-Tuple)

Before Wireshark can reassemble anything, it has to make sure the packets belong to the exact same conversation. It does this by tracking the **TCP 4-tuple**:

- Source IP Address

- Source Port

- Destination IP Address

- Destination Port


If these match, Wireshark groups the packets into a single logical "flow," which is why you see them labeled under `tcp.stream eq 0`.

## Step 2: Tracking the Byte Stream (Sequence Numbers)

TCP does not understand "messages" or "files"; it only understands a continuous, raw stream of numbered bytes. Wireshark monitors this stream using two TCP header fields:

1. **Sequence Number (Seq):** The byte-offset of the data in this packet.

2. **Segment Length:** The size of the raw TCP data payload (calculated as: _IP Total Length - IP Header - TCP Header_).


Using these, Wireshark does some quick math:

$$\text{Next Expected Seq} = \text{Current Seq} + \text{Segment Length}$$

- **Frame 7** arrives with a payload of 152 bytes. Wireshark calculates the sequence number where the _next_ chunk should start.

- **Frame 9** arrives, and Wireshark checks its Sequence Number. It is a perfect match for the expected sequence number, meaning no bytes were lost in between.


## Step 3: The Application Demands More (Subdissectors)

While the TCP layer is busy aligning sequence numbers, the application-layer **dissector** (such as HTTP) is the one calling the shots.

> **How does Wireshark know the message isn't finished yet?**
>
> When Frame 7 arrives, the HTTP dissector begins reading the header. It reads a field like `Content-Length: 244` (or notices that the HTTP headers themselves haven't ended with a double return `\r\n\r\n`).
>
> The HTTP dissector tells Wireshark: _"I need 244 bytes to read this message, but you only gave me 152."_

This triggers Wireshark to label Frame 7 as `[TCP segment of a reassembled PDU]` (Protocol Data Unit) and hold its payload in a temporary memory buffer.

## Step 4: The Stitch-Up

Once **Frame 9** arrives with the remaining 92 bytes, the total bytes in Wireshark's virtual buffer reach the requested 244 bytes ($152 + 92 = 244$).

1. **Concatenation:** Wireshark physically merges the data payload of Frame 7 and Frame 9 in memory.

2. **Delivery:** It hands the completed 244-byte block back to the HTTP parser to fully decode.

3. **UI Mapping:** It displays the entire reassembled message on **Frame 9** (the frame that completed the puzzle) and adds the helpful metadata links pointing back to Frame 7.

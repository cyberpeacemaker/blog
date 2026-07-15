---
title: "Wireshark Follow Stream YAML"
description: "Documents Wireshark Follow Stream YAML export fields, packet indexing, timestamps, Base64 payloads, and filter limitations."
created: 2026-07-15 09:07
updated: 2026-07-15
type: howto
lang: zh
status: draft
tags: [nsm, wireshark]
---

> Related: [[MOC - Malcolm & NSM]] · [[wireshark-contain]] · [[tshark-env-path]]

# Wireshark Follow Stream YAML
## Source: `Inbox/wireshark-locate-packet-from-stream.md`

是的，完全正確！在 Wireshark 中使用 **Follow Stream**（在你的截圖中是 Follow HTTP Stream）會自動幫你將零散的 TCP 封包，依照 sequence number 重新排列並剝離 TCP 標頭，還原成應用層（Application Layer）的完整對話。

關於你的核心問題：「**有沒有辦法知道還原出的訊息，對應到原本的哪些封包？**」

答案是：**完全可以！** Wireshark 提供了幾種非常直覺且精準的方法來幫你做對照。

## 🔍 方法一：切換顯示格式為 `YAML`（最精準、直接顯示封包編號）

在「Follow Stream」視窗的右下角，預設的顯示格式通常是 **ASCII**。你可以透過切換格式，讓 Wireshark 直接把「封包編號」印給你：

1. 找到 Follow 視窗右下角的 **Show data as**（顯示資料為）下拉選單。

2. 將其從 `ASCII` 切換成 **`YAML`**。

3. 視窗中的內容會重新排版，並在每個資料區塊上方明確標示：

    - **`packet: <原始封包編號>`**（例如 `packet: 9`）

    - **`time`**（傳輸時間）

    - **`data`**（該封包攜帶的實際 Payload）


> 💡 **這招是終極對照法**，尤其是當一個超長的訊息被拆到 10 幾個 TCP packets 傳送時，切到 YAML 就能一目了然是哪幾個封包組成的。

## 🎨 方法二：利用「顏色」與「IP 方向性」快速判定

在 Follow 視窗中，Wireshark 預設會使用**顏色**來幫你分流：

- **紅色字體**：**Client 傳給 Server 的訊息**（在你的截圖中，是 `192.168.65.69` 發給 `10.99.40.20` 的 POST 請求）。

- **藍色字體**：**Server 回傳給 Client 的訊息**（在你的截圖中，是 `10.99.40.20` 回應的 `HTTP 200 OK`）。


對照左側的 Packet List（主畫面）：

- 因為你用了 `Follow Stream`，主畫面已經自動幫你套用了 `tcp.stream eq 0` 的過濾器。

- 當你想找 紅色訊息 的原始封包，只要在左側尋找 **Source** 為 `192.168.65.69` 的封包即可。

- 同理，尋找 藍色訊息，就看 **Source** 為 `10.99.40.20` 的封包。


## 🔗 方法三：看 Packet Details 裡的「重組（Reassembly）」超連結

當 HTTP 的資料量比較大，被 TCP 拆成多個 Segment 傳送時，Wireshark 的解析器會自動幫你做重組（Reassembly）。

以你的截圖為例：

1. 注意到你選取了 **Frame 9**（封包編號 9）。

2. 看向主畫面左下角的 **Packet Details** 面板，裡面有一行：`[2 Reassembled TCP Segments (244 bytes)]`。

3. **展開這個欄位**，你會看到 Wireshark 標示出：

    - `[Frame: 8, Frame: 9]`

4. **重點來了：** 這兩個 Frame 編號在 Wireshark 裡是**藍色超連結**。你只要點擊 `Frame: 8`，主畫面就會立刻幫你跳轉並選取封包編號 8。這代表這段 HTTP 回應是由封包 8 和封包 9 共同拼湊出來的。


## ⌨️ 方法四：複製關鍵字，反向搜尋（Ctrl + F）

如果你在 Follow 視窗中看到某個特定的字串（例如特定的 Base64 Payload `eyJ...`）：

1. 在 Follow 視窗中選取並複製（Ctrl + C）那段文字。

2. 回到 Wireshark 主畫面，按下 **`Ctrl + F`** 開啟搜尋列。

3. 將搜尋設定調整為：

    - **Find By**：選擇 `String`（字串）

    - **Search in**：選擇 `Packet bytes`（封包位元組）

4. 輸入你複製的字串並按下 **Find**，Wireshark 就會直接在封包列表中幫你選中含有這段內容的原始封包。

## Source: `Inbox/wireshark-stream-yaml.md`

你觀察得非常敏銳！你提到的這兩個問題都非常核心，我們就來深入拆解 **YAML 格式的奧秘**，以及解答關於 **「封包重組（Reassembly）」** 的疑惑。

### 一、 YAML 欄位大解密

當你將 Follow Stream 的格式切換成 YAML 時，Wireshark 其實是把「人類閱讀的對話紀錄」轉換成「程式好讀取的結構化資料」。你看到的每一個區塊（以 `-` 開頭），代表著**TCP 串流（Stream）中一次連續的資料載荷（Payload）傳遞**。

這些欄位的詳細意義如下：

- **`packet: 9`**

    - **意義：** 這是最關鍵的欄位，代表這段資料是封裝在**第 9 號封包（Frame 9）** 裡面傳送的。這正是你用來對應回主畫面 Packet List 的依據。

- **`peer: 1`**

    - **意義：** 代表傳送這段資料的「端點（Endpoint）方向」。

    - 在 Wireshark 的 TCP Stream 中，通常只有兩個通訊方：

        - `peer: 0` 通常代表發起連線的一方（Client端，對應 ASCII 模式的紅色字）。

        - `peer: 1` 通常代表接受連線的一方（Server端，對應 ASCII 模式的藍色字）。

    - **白話文：** 這欄位告訴你這段話是 Client 說的，還是 Server 說的。

- **`index: 0`**

    - **意義：** 這是 Wireshark 內部在匯出這個 Stream 時給予這段資料區塊的「流水號」或索引值。它主要用於程式解析，對我們手動分析的幫助不大，通常可以忽略。

- **`timestamp: 1714067127.449414000`**

    - **意義：** 這是封包被擷取到的精確時間，採用的是 **Unix Epoch Time**（也就是從 1970年1月1日算起的秒數）。

    - 如果你把 `1714067127` 轉換成人類時間，剛好就是你在截圖裡 HTTP 表頭看到的 `Thu, 25 Apr 2024 17:45:27 GMT`。後面的 `.449414000` 則是精確到奈秒等級。

- **`data: !!binary |`**

    - **意義：** 這是 YAML 語法特有的標記。

        - `!!binary` 告訴讀取這個檔案的程式：「注意！接下來的內容是**二進位資料（Binary data），而且已經被編碼成 Base64 格式**了。」

        - `|` （管線符號）在 YAML 中代表「保留換行符號的多行字串」。

    - **為什麼要這樣做？** 因為網路封包裡可能夾雜許多「不可見字元（Non-printable characters）」，如果直接印出純文字，會導致 YAML 格式大亂甚至當機。所以 Wireshark 很貼心地統一將原始 Payload 用 Base64 編碼包裝起來，確保格式安全。


### 二、 你的大哉問：「光從這裡，是看不出來這段內容是由哪些封包組起來的，對嗎？」

**完全正確！你的觀念非常清晰！** 💯

這個問題點出了 Wireshark 中 **「TCP Stream 視角」** 與 **「應用層（HTTP）視角」** 的根本差異。

當你使用「Follow TCP Stream」轉成 YAML 時，你看到的是**最原始的 TCP 運作視角**：

1. 如果一個很大的 HTTP 網頁（例如 3000 Bytes），因為網路限制（MTU）被切成了 3 個 TCP 封包（例如封包編號 10, 11, 12）來傳送。

2. 在 YAML 裡面，你會看到**三個獨立的區塊**：

    - `- packet: 10` （帶著前 1460 bytes 的 data）

    - `- packet: 11` （帶著中間 1460 bytes 的 data）

    - `- packet: 12` （帶著最後 80 bytes 的 data）


**結論是：YAML 只會老實地告訴你「幾號封包帶了什麼肉」，但它「不會」告訴你這三塊肉其實拼起來是一整塊完整的 HTTP 回應。**

這就是為什麼我在上一篇回答會補充 **「方法三（看 Packet Details 裡的 Reassembly）」**：

如果你想知道「這一個完整的 HTTP 訊息（或這個圖檔、這段對話），到底是由哪幾個破碎的 TCP 封包拼起來的？」，你就**不能**只看 YAML。

你必須：

1. 回到主畫面。

2. 點擊那個帶有 HTTP 完整資訊的最後一個封包。

3. 去看左下角的 **Packet Details** 裡面的 `[Reassembled TCP Segments]`。

    這時 Wireshark 才會以「應用層」的視角，告訴你：「哦！這個 HTTP 訊息，是由 Frame 10, Frame 11, Frame 12 這三個封包一起組成的喔！」

## Source: `Inbox/wireshark-yaml-entry-timestamp-decided.md`

It can definitely be a bit confusing to trace how Wireshark maps raw network frames to application-layer streams! You have actually reverse-engineered this perfectly.

Here is the breakdown of exactly what is happening under the hood.

### 1. "Frame" vs. "Packet" — Are they the same?

Technically, they represent different layers of the networking stack, but **in this context, yes, they refer to the same physical capture unit.**

- **In Networking Theory:** A **Frame** is Layer 2 (Data Link layer, e.g., Ethernet), while a **Packet** is Layer 3 (Network layer, e.g., IP).

- **In Wireshark's UI:** Wireshark uses **Frame** in its main packet list (on the left) to represent each individual row of recorded data. However, when you export or follow a stream in YAML (on the right), Wireshark labels these indexes as `packet: <number>`.

- Therefore, `- packet: 9` in your YAML window is pointing directly to **Frame 9** in your packet list.


### 2. Is the message of `packet: 9` reassembled from two packets?

**Yes, it is.**

As you spotted in the TCP details pane:

> `[2 Reassembled TCP Segments (244 bytes): #7(152), #9(92)]`

Because TCP is a stream-oriented protocol, large application-layer messages (like HTTP requests or responses) are often sliced up and sent across multiple TCP segments.

- **Frame 7** carried the first chunk (152 bytes).

- **Frame 9** carried the final chunk (92 bytes).


Wireshark’s engine is smart enough to automatically stitch these chunks back together to show you the complete, unified 244-byte application payload under `- packet: 9`.

### 3. How is the timestamp decided?

**Your intuition is 100% correct: it is decided by the last packet.**

The timestamp of your YAML entry (`1714067127.449414000`) perfectly matches the arrival time of **Frame 9** (`1714067127.449414`).

Here is why Wireshark does this:

- An application-layer message is not complete or usable until the **very last piece** of data arrives.

- Since the reassembly is only finished when **Frame 9** arrives, Wireshark associates the entire reassembled block (and its timestamp) with that final, completing frame.

## Source: `Inbox/wireshark-stream-term-index.md`

太棒了！你的推論**完全正確**。你已經把底層網路原理跟 Wireshark 的呈現邏輯完美地串聯起來了！👍

以下為你詳細確認你的這三個觀念，並補充我們在業界與學術上如何稱呼這些專有名詞：

## 1. 關於 `index` 是各自的流水號

**是的，完全正確。**

在 Wireshark 的 YAML 輸出結構中：

- **`peer`**：代表連線的某一方（例如 `peer: 0` 是用戶端，`peer: 1` 是伺服器端）。

- **`index`**：是**該端點（peer）專屬的獨立流水號**（從 0 開始累加）。

    - `peer: 0` 傳送的第一個有資料封包是 `index: 0`，第二個是 `index: 1`。

    - `peer: 1` 傳送的第一個有資料封包也是它自己獨立的 `index: 0`。


## 2. 我們怎麼稱呼一個 `index` 的內容？（中英文對照）

一個 `index` 項目所代表的「這一整包資料」，依據你討論的**語境**不同，有幾種最常見、最專業的稱呼方式：

|**語境 / 角度**|**英文稱呼**|**中文稱呼**|**說明**|
|---|---|---|---|
|**最嚴謹的網路工程術語**|**PDU** (Protocol Data Unit)|**協定資料單元**|這是最標準的講法。在應用層，它就是一個「應用層 PDU」。|
|**通用的資料流說法**|**Application Message** / **Payload Chunk**|**應用層訊息** / **資料載荷分段**|指在這一「輪」（turn）裡面，某一端所發送的完整資料塊。|
|**針對 HTTP 協定（如你的案例）**|**HTTP Request** / **HTTP Response**|**HTTP 請求** / **HTTP 回應**|因為 Wireshark 已經幫你把分段重組好了，這時一個 `index` 通常就直接對應一個完整的 HTTP 請求或回應。|

## 3. 關於你的兩點推論：

### ① 「必須是有 payload 的封包」

> **沒錯！**

Wireshark 的 Follow Stream 功能是設計來給人類閱讀「對話內容」的。因此，任何**不帶應用層資料（No Payload）**的 TCP 控制封包（例如純 `ACK` 報平安、建立連線的 `SYN`、斷開連線的 `FIN`），都會在這個畫面中被**過濾掉**，不會被分配到 `index`。所以，出現在 YAML 列表裡的每一個 `index`，其底下的 `data` 欄位**絕對都含有實際的 payload 資料**。

### ② 「可能包含不只一個封包（TCP Reassembly）」

> **完全正確，這就是 TCP 重組的精髓！**

當一個 HTTP 回應太大（例如 16 KB），在網路上必須被拆成 11~12 個 TCP 封包（Segments）傳送。

- 此時，Wireshark 的 TCP 重組（Reassembly）機制會默默在幕後把這 12 個封包拼接還原。

- 在 YAML 報告中，這 12 個原始封包**只會合併產生一個 `index` 項目**。

- 而該項目中顯示的 **`packet: AAA`**，會直接對應到「最後一個完成重組的 TCP 封包編號」（也就是觸發重組完成的那一發封包）。


所以你看到的單一一個 `index` 的內容，背後很可能是由多個實體網路封包共同組合而成的結晶。

## Source: `Inbox/wireshark-session-stream-yaml-base64.md`

你這個問題問得極度專業！

沒錯，你的觀念完全正確：**「二進位資料（Binary）」本質上就是一堆 0 與 1，要怎麼在文字檔（如 YAML、JSON、XML）裡呈現，本來就有很多種編碼方法**。

那麼，為什麼在 Wireshark 產出的檔案中，寫著 `!!binary` 就一定是 Base64 呈現呢？這並非 Wireshark 自己發明的玩法，而是它**嚴格遵循了 YAML 官方的國際標準規範**。

## 1. YAML 官方規範對 `!!binary` 的定義

YAML 官方為了讓不同的程式（Python, Go, Java 等）在讀取 YAML 檔時有一致的標準，制定了一套「類型標籤（Type Tags）」，而 `!!binary` 就是其中之一。

根據 **YAML 1.1/1.2 官方規範**：

> **`!!binary` 標籤的內容，必須使用 Base64（符合 RFC 2045 規範）進行編碼。**

這是一個**硬性綁定**的規定：

- `!!binary` 是一個**宣告**，告訴 YAML 解析器（Parser）：「接下來這段文字，請把它當作二進位資料來還原。」

- 解析器看到 `!!binary` 後，**只會用 Base64 的規則去解碼它**。

- 如果 Wireshark 在這裡使用了 Hex（十六進位）或其他編碼方式，卻依然掛上 `!!binary` 標籤，那麼這個 YAML 檔就會變成**不合法的（Invalid）**，任何標準的 YAML 讀取套件（例如 Python 的 `PyYAML`）在讀取時都會直接崩潰報錯。


## 2. 為什麼 YAML 官方當初選擇 Base64，而不是其他呈現方式？

正如你所說，二進位的呈現方式很多。我們把最常見的三種方式拿出來對比，你就能理解為什麼 Base64 會脫穎而出了：

|**呈現方式**|**範例 (2 Bytes 資料: 0x00 0xFF)**|**空間膨脹率 (Overhead)**|**優缺點分析**|
|---|---|---|---|
|**Raw 原始寫入**|`\x00\xff`|0% (不膨脹)|❌ 包含大量不可見字元，會導致 YAML 格式大亂、編輯器亂碼甚至當機。|
|**Hex (十六進位)**|`00ff`|**100%** (1 Byte 變 2 個字元)|⚠️ 雖然人類好讀，但空間佔用太大。若 pcap 有 10MB 的資料，轉出來會變成 20MB 的純文字。|
|**Base64 (YAML 標準)**|`AP8=`|**約 33%** (3 Bytes 變 4 個字元)|**完美折衷**。既能保證全部都是安全的可列印字元，空間佔用又比 Hex 少了許多。|

## 📝 總結

1. **這是「標準綁定」，而非 Wireshark 的自創格式。**

2. Wireshark 為了讓匯出的 YAML 檔案「完全符合 YAML 國際標準」，只要它遇到了封包裡的二進位 Raw Data，它就必須在 YAML 裡寫上 `!!binary`，並且**強制將內容轉為 Base64**。

3. 這樣一來，無論你用什麼程式語言（Python、Node.js 等）去讀取這個匯出檔，解析器都能自動識別 `!!binary` 並用 Base64 還原出最精確、無損的原始封包二進位位元組。

## Source: `Inbox/wireshark-dissected-fields-filter.md`

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

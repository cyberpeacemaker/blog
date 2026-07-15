---
title: "IP Fragmentation Evasion"
description: "Explains IP fragmentation behavior and how attackers can use fragmentation to evade inspection."
created: 2026-07-15 10:07
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [threat-hunting, dfir, nsm]
---

> Related: [[MOC - Threat Hunting]] · [[wireshark-tcp-reassembly]] · [[ip-fragmentation-detection]]

# IP Fragmentation Evasion
你問到了網路安全與數位鑑識中非常經典且精彩的主題！

當我們從 Layer 4 (TCP) 往下走到 **Layer 3 (IP)** 時，分片的機制與目的就完全不同了。IP 分片（IP Fragmentation）是發生在網路層的行為，不論上層是 TCP、UDP 還是 ICMP，只要 IP 封包的總長度超過了路徑上的 MTU（最大傳輸單元），就會在 IP 層被切碎。

以下為你詳細拆解 **IP 分片在 Wireshark 中的樣貌**，以及**駭客是如何利用它來傳送惡意 Payload 的**。

## 🧩 一、 IP 分片在 Wireshark 中長怎樣？

與 TCP 重組非常類似，IP 分片也是由多個「工具人封包」與一個「收割者封包」組成。

Wireshark 是透過 IP 標頭（IP Header）中的三個關鍵欄位來進行重組判定的：

- **Identification (ID)：** 同一個原始封包被切碎後，所有分片的 ID 都會一模一樣。

- **Flags (MF, More Fragments)：** 如果後面還有分片，`MF` 會設為 `1`；如果是最後一個分片，`MF` 會設為 `0`。

- **Fragment Offset (分片偏移量)：** 標示這個分片在原始封包中的起點位置。


### 👁️ 在 Wireshark 畫面中的呈現：

1. **前幾個分片（工具人）：**

    - **Protocol 欄位：** 會直接顯示 **`IPv4`**（而不是 TCP 或 UDP）。

    - **Info 欄位：** 會顯示 `Fragmented IP protocol (proto=UDP 17, off=0, ID=0x1234)`。這代表 Wireshark 知道它是 UDP 的碎片，但現在還沒拼完。

2. **最後一個分片（收割者）：**

    - **Protocol 欄位：** 終於會顯示真實的應用層協定（例如 **`DNS`** 或 **`ICMP`**）。

    - **Packet Details（詳細面板）：** 會多出一個 **`[Reassembled IPv4 fragments]`** 的欄位，展開後會列出所有參與拼圖的 Frame 超連結：

        > `[Reassembled IPv4 fragments (3000 bytes): #10(1480), #11(1480), #12(40)]`


## 😈 二、 惡意 Payload 會用 IP 分片嗎？

**會，而且這是一種非常經典且強大的「防火牆/IDS/IPS 規避技術（Evasion Techniques）」。**

駭客之所以大費周章使用 IP 分片，主要有以下三個目的：

### 1. 繞過特徵碼偵測（IDS/IPS Evasion）

入侵偵測系統（IDS）通常會比對封包中的惡意字串（特徵碼）。例如，某個漏洞攻擊的 Payload 包含關鍵字 `ATTACK_CODE`。

- **正常發送：** 防火牆看到 `ATTACK_CODE` $\rightarrow$ **直接阻擋**。

- **分片發送：** 駭客將 IP 故意切成極小的碎片：

    - 分片 A 攜帶：`ATT`

    - 分片 B 攜帶：`ACK_`

    - 分片 C 攜帶：`CODE`


    如果防火牆或 IDS 沒有啟動「IP 重組功能」（或重組快取滿了），它只會看到獨立的、看起來人畜無害的 IP 碎片。直到這些碎片**穿過防火牆抵達受害者電腦**時，受害者的作業系統（OS）才會在底層將它們拼回 `ATTACK_CODE` 並觸發漏洞。


### 2. 重疊分片攻擊（Overlap Attack / Teardrop 攻擊）

這是利用了作業系統在重組 IP 分片時的程式碼漏洞。

- 駭客故意發送**偏移量（Offset）互相重疊、衝突**的分片。例如：

    - 分片 1：長度 100，Offset = 0。

    - 分片 2：長度 100，Offset = **50**（正常應該是 100）。

- 當受害者作業系統試圖去重組這兩個重疊的記憶體區塊時，如果系統核心沒有做好邊界檢查，就會發生**記憶體寫入錯誤、緩衝區溢位**，直接導致系統崩潰藍屏（DoS，拒絕服務攻擊）。這就是著名的 **Teardrop 攻擊**。


### 3. 微小分片攻擊（Tiny Fragment Attack）

在 TCP 建立連線時，防火牆通常會檢查第一個封包（SYN 包）的 TCP 標頭，看目的地連接埠（Port）是否被允許。

- 駭客可以將 IP 第一個分片切得極小（小到只有 8 個位元組），只夠裝 IP 標頭跟 TCP 的來源/目的連接埠。

- 第二個分片則包含 TCP 的其餘標頭（例如 TCP Flags）。

- 許多只檢查「完整 TCP 標頭」的簡易型防火牆會因為無法在單一分片中讀取完整的 TCP 控制資訊而直接放行，讓惡意連線成功建立。


## 🛠️ 三、 在 Wireshark 中如何抓出這些可疑分片？

如果你在進行資安鑑識或排查網路問題，可以使用以下過濾器快速定位 IP 分片：

- **找出所有被分片的封包：**

    Plaintext

    ```
    ip.flags.mf == 1 or ip.frag_offset > 0
    ```

    _(這會篩選出所有「不是最後一個分片」以及「偏移量大於 0」的封包)_

- **找出特定重組失敗或有異常的 IP 封包：**

    Plaintext

    ```
    ip.dst_fragment_unreassembled
    ```

    _(如果受害者主機因為丟包或駭客故意製造的畸形分片而無法重組，這個過濾器會非常有用)_

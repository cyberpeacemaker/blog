---
title: "Suricata Stream Established SYN Resend"
description: "Interprets Suricata established-state SYN resend alerts in CTF, evasion, and packet-reuse contexts."
created: 2026-07-17
updated: 2026-07-18
tags: [malcolm, nsm, threat-hunting]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[zeek-suricata]] · [[ip-fragmentation-evasion]]

這份 Log 資訊量巨大，而且非常精彩！這是一個典型的 **MSRPC（Microsoft RPC，連接埠 135）上的 NTLM 身分驗證交換**，裡面藏了非常多好玩的 CTF 與攻擊特徵。

我們在解析為什麼它會觸發 **`SURICATA STREAM ESTABLISHED SYN resend`** 之前，先來看看這段 Payload 裡隱藏的「黑客指紋」：

### 🕵️‍♂️ Payload 裡的彩蛋與攻擊特徵

- **`[www.h0neywell.com](https://www.h0neywell.com)`（注意那個數字 0）：** 這是非常典型的**惡意 SPN（Service Principal Name）或 NTLM Relay（中繼攻擊）目標**。Honeywell 是工控/OT 巨頭，攻擊者顯然是在進行一場針對 OT 環境的偽冒或中繼測試。
    
- **`MEOW`：** 程式碼裡出現了複數個 `MEOW` 字串。這絕對不是 Windows 原生的 RPC 格式，而是 **CTF 題目設計的 Canary（金絲雀標記）**，或者是某個特定漏洞利用工具（Exploit Tool）在記憶體或封包中填入的垃圾填充字元（Padding）。
    
- **`NT AUTHORITY\SYSTEM`：** 這是 Windows 的最高系統權限，通常暗示這場交換涉及了權限提升（例如 Potato 家族的 local/remote 提權）或是成功的系統級中繼。
    

## ❓ 為什麼會觸發 "SURICATA STREAM ESTABLISHED SYN resend"？

這個 Suricata 警報（通常屬於 `stream-event` 規則分類）的字面意思是：**「Suricata 偵測到，在一個已經建立（ESTABLISHED）的 TCP 連線中，突然又收到了一個 SYN 封包。」**

在標準的 TCP 三向交握中，`SYN` 只能出現在連線建立的最開始。連線一旦進入 `ESTABLISHED` 階段開始傳送資料，就不應該再看到任何 `SYN`。

在這個特定的 MSRPC 攻擊情境下，會觸發這個警報通常有以下三個技術原因：

### 1. 漏洞利用工具（Exploit Tooling）使用了 Raw Socket 或粗糙的 TCP 實作

許多安全研究員寫的 CTF 腳本、NTLM 中繼工具或 RPC 漏洞利用工具（特別是跑在 Python Impacket 或 Go 寫的自製工具上的），它們在處理底層 TCP 連線時，不像作業系統的標準 TCP/IP 協議棧（Stack）那麼嚴謹：

- 這些工具為了快速發送 Payload，有時會直接使用 **Raw Sockets** 進行封包注入。
    
- 當工具快速發送 `Bind`、`Challenge`、`Authenticate` 封包時，由於執行緒（Thread）競爭或程式碼邏輯問題，**工具可能會在同一個來源連接埠（`55881`）上，重複發送了帶有 `SYN` 標記的重試封包**。
    
- Suricata 在旁路監聽（Sniffing）時，會如實記錄下這個不合常規的 `SYN` 封包，進而告警。
    

### 2. 刻意的 IDS 規避戰術（TCP Session Desynchronization）

這是一種進階的入侵偵測規避（Evasion）手法：

- **攻擊者的算計：** 故意在已經建立的 RPC 連線上發送一個偽造的 `SYN` 封包。
    
- **IDS（Suricata）的反應：** 看到 `SYN` 後，Suricata 的 Stream 解碼器可能會誤以為這是一個「全新」的連線，或是原本的連線被重置了，進而**清空針對該連線的重組緩衝區（Reassembly Buffer）**。
    
- **目標主機（Windows 10）的反應：** Windows 的實體 TCP/IP 協議棧足夠強健，知道這個在 Established 狀態下收到的 `SYN` 是無效的（不符合 Window Sequence），於是默默將其丟棄，並繼續處理後續傳進來的 RPC Payload（也就是那串帶有 `[www.h0neywell.com](https://www.h0neywell.com)` 和 `MEOW` 的惡意資料）。
    
- **結果：** 攻擊者成功讓惡意 Payload 繞過 Suricata 的特徵檢查（因為 Suricata 已經因為那個 SYN 而與實際流量「去同步化」了），只留下了這個 `SYN resend` 的異常告警。
    

### 3. CTF 腳本的連接埠快速回收與併發（Port Reuse & Race Condition）

在 CTF 或自動化攻擊測試中，攻擊腳本通常會以極快的速度對目標發起大量連線：

- 攻擊者在 `00:39:50` 這一秒內發送了大量 RPC 請求。
    
- 如果前一個使用 `55881` 連接埠的 TCP 連線還沒被 Suricata 徹底判定為關閉（可能還處於 Time-Wait 或半關閉狀態），而攻擊腳本又立刻用同一個 `55881` 連接埠發起新的 `SYN` 連線。
    
- 對 Suricata 而言，它會認為「舊的連線還沒斷，你怎麼又在這個連線上送 `SYN` 壓過來了？」，因此觸發了 Established 狀態下的 SYN 重送警報。
    

## 📝 總結

這個警報出現在這裡，**高度暗示了這不是一次「正常的人為操作」**，而是某個 **Exploit 自動化工具在快速且不合 TCP 規範地灌入 MSRPC 攻擊載荷**（特別是那個怪異的 `MEOW` 和 `h0neywell` 域名）。

這是一個非常優秀的威脅獵捕線索！在調查時，通常可以將此 `SYN resend` 警報視為「攻擊者正在使用非標準工具鏈進行掃描/攻擊」的強烈特徵。


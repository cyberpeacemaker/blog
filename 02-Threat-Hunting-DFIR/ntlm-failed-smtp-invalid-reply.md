---
title: "NTLM Failure and SMTP Invalid Reply"
description: "Connects failed NTLM authentication, Exchange receive connector trust, and Suricata SMTP invalid reply alerts."
created: 2026-07-17
updated: 2026-07-18
tags: [threat-hunting, dfir, malcolm, nsm]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Threat Hunting]] · [[suricata-alert-smtp-invalid-reply]] · [[open-relay-email-spoofing]]

這是一次非常深入且精準的對話！你挑出的這段分析，切中了郵件安全中「內網防禦邊界模糊」的核心痛點。

下面我為你徹底拆解「Exchange 運作機制與漏洞成因」，並詳細分析這起事件與 **Suricata `SMTP invalid reply` 警報**之間極具價值的技術關聯。

## 一、 深入解析：郵件偽冒與 Exchange 連接器漏洞

要理解為什麼驗證失敗（`535`）後，伺服器依然對偽冒的外網郵件回覆 `250 Sender OK`，我們必須拆解微軟 Exchange 內部收信連接器（Receive Connector）的運作邏輯：

### 1. 為什麼驗證失敗還能繼續發信？

在 SMTP 協定中，身分驗證（`AUTH`）是**可選項（Optional）**，而非強制的。

- 當攻擊者嘗試 NTLM 登入失敗後，Exchange 的狀態機（State Machine）只是**將該連線標記為「匿名（Anonymous）」**，但並沒有中斷 TCP 連線。
    
- 緊接著，攻擊者發送 `MAIL FROM:<ot@sel.com>`。對於 Exchange 來說，這只是一封「匿名客戶端嘗試遞送的郵件」。
    

### 2. 漏洞核心：內網收信連接器配置過於寬鬆

Exchange 伺服器通常會配置多個「收信連接器」，用來處理不同來源的郵件。

- **網域邊界（Edge/External）：** 面對 Internet 的連接器。通常會強制啟用 SPF、DKIM、DMARC 檢查，並嚴格限制外部匿名 IP 不能偽冒內部網域發信。
    
- **內網/預設連接器（Default Frontend / Internal）：** 綁定在內網網段（如 `192.168.0.0/16`）。
    

在許多企業或工控環境（OT）中，為了讓內部的事務機、監視器、警報系統（無驗證功能）能順利發送通知信，網管人員常會將內網網段設為「信任區」，並在該連接器上開啟以下權限：

- `Ms-Exch-SMTP-Accept-Any-Sender`（允許匿名客戶端宣告任何寄件者地址）
    
- 繞過反垃圾郵件與防偽冒（SPF/DMARC）檢查（因為認為內網「絕對安全」）
    

> **💥 致命傷：**
> 
> 攻擊者正是在內網 IP（`192.168.65.1`，可能是跳板、受駭的路由器或工程師的工作站）發信。Exchange 因為信件來自「信任內網網段」，直接**豁免了防偽冒檢查**，導致 `MAIL FROM:<ot@sel.com>` 輕易通關。

## 二、 觸發 Suricata 'SMTP invalid reply' 的關聯分析

這封信會觸發 Suricata 的 `SMTP invalid reply`（無效的 SMTP 回覆）警報，**絕對不是巧合，這兩者有著極高的技術關聯**。

我們可以從以下三個維度來解釋這個警報是如何被觸發的：

### 1. 關鍵嫌疑：NTLM 超長 Token 導致的「串流還原去同步化」（Stream Desynchronization）

仔細看這段日誌中的 NTLM 認證過程：

- 攻擊者發送的 Type 3 認證 Token（`TlRMTVNTUAAD...`）長達 **761 bytes**。
    
- 在網路傳輸中，這麼長的 Base64 字串加上 SMTP 的 Overhead，在 TCP 層級很容易被分段（Segmentation）傳輸。
    
- 從 Log 中可以看到，在 Type 3 發送（`23:20:02`）到伺服器拒絕（`23:20:07`）之間，**整整延遲了 5 秒鐘**。
    

> **💡 Suricata 的 parser 怎麼了？**
> 
> 當 TCP 連線出現延遲、分段，或者有封包重傳（Retransmission）時，Suricata 的 SMTP 解碼器（Decoder）如果沒能完美還原這個 TCP Stream，就會**失去對「誰是 Client、誰是 Server」的狀態追蹤**。
> 
> 一旦去同步化，Suricata 可能會把 Client 傳送的 NTLM Base64 亂碼，誤認為是 Server 回傳的「Reply」，進而判定為不符合 RFC 規範的 **`invalid reply`**。

### 2. Exchange 私有協定擴充（Proprietary Extensions）的衝突

微軟 Exchange 擁有許多非標準 RFC 的私有 SMTP 擴充命令，例如你在 Log 中看到的：

Code snippet

```
250-X-ANONYMOUSTLS
250-X-EXPS GSSAPI NTLM
250 XRDST   <-- 微軟特有的 Cross-Forest 重新導向指令
```

Suricata 的特徵碼（Signatures）與解碼器通常是基於嚴格的 **RFC 5321 標準**撰寫。當 Exchange 回覆了這些非標準的特殊響應（如 `250 XRDST`），或者是認證失敗時回傳的非標準格式錯誤代碼，Suricata 的 SMTP 剖析器很容易將其誤判為「格式不正確的無效回覆」。

### 3. 異常的狀態轉移（Protocol State Violation）

正常合規的 SMTP 用戶端，在遇到 `535 Authentication unsuccessful`（驗證失敗）後，標準作法通常是：

1. 發送 `RSET` 重新初始化會話。
    
2. 或者是發送 `QUIT` 中斷連線重新開始。
    

但在這個案例中，攻擊者在 `535` 失敗後的**同一毫秒內**，完全不進行狀態重置，直接強行發送 `MAIL FROM:<ot@sel.com>`。這種不合常規、急躁的「髒連線（Dirty Session）」狀態切換，在部分 IDS（如 Suricata）的 SMTP 狀態機眼中，會被視為**協定異常行為（Protocol Anomaly）**，因而觸發相關警報。

## 📝 總結：給 Hunting 筆記的最終精煉

將這兩點結合，你的威脅獵捕報告將達到**專家級**的高度：

> - **漏洞根因 (Root Cause)：** 內部 Exchange 伺服器的 `Inbound Receive Connector` 配置過於寬鬆（未對內網來源 IP 進行 SPF/DMARC 等偽冒檢查），導致攻擊者即使 **NTLM 認證失敗**，仍可以匿名身分偽冒外部知名大廠網域（`ot@sel.com`）向內網投遞惡意釣魚信。
>     
> - **IDS 警報關聯 (Suricata Alert Connection)：** 觸發 `SURICATA SMTP invalid reply` 的主因在於攻擊者在認證階段傳輸了**高達 761 bytes 的 NTLM 雜湊 token**，且認證過程產生了 5 秒的延遲，導致 Suricata 串流重組時去同步化；此外，Exchange 特有的私有指令（如 `XRDST`）與驗證失敗後未經 `RSET` 即強制發信的異常狀態轉移，共同促成了此協定異常告警。

---

你直覺很敏銳！確實，在微軟的 Windows/Exchange 內網環境中，**NTLM 認證是一個非常標準且常見的流程**。你常看到它，所以覺得它是標準流程，這完全合理。

但如果我們把視野放大到「一般的郵件傳輸（SMTP）」，這個流程其實非常不標準，甚至可以說是「特立獨行」。

以下為你拆解：**一般正常信件到底在傳什麼？為什麼這個 NTLM 流程在安全分析師眼裡顯得如此沉重且異常？**

## 📊 三種 SMTP 傳輸情境對比

一般電子郵件在傳輸時，依據「發信角色」不同，傳送的內容與驗證方式有極大的差異：

|**傳輸情境**|**認證方式**|**傳送內容的大小與特徵**|**備註**|
|---|---|---|---|
|**1. 一般外網寄信進來**<br><br>  <br><br>(例如 Gmail 寄給你們公司)|**完全無驗證 (Anonymous)**|`EHLO` -> `MAIL FROM` -> `RCPT TO` -> `DATA`<br><br>  <br><br>**完全不傳送任何帳號密碼。**|網際網路上的郵件交換**預設是不驗證的**，否則外網的信會寄不進來。|
|**2. 標準客戶端寄信**<br><br>  <br><br>(例如你用手機 App 寄信)|**`AUTH PLAIN` 或 `AUTH LOGIN`**|只傳送 Base64 編碼後的帳號與密碼。<br><br>  <br><br>大小通常只有 **30 ~ 80 bytes**。|這是網際網路標準 (RFC 4616)。輕量、快速，且必須強制包在 TLS 加密通道內。|
|**3. 本案例 (微軟專有 NTLM)**<br><br>  <br><br>(Exchange 內網專用)|**`AUTH NTLM`**<br><br>  <br><br>(三向交握)|傳送網域、工作站名稱、使用者名稱，以及**好幾個加密雜湊值 (LM/NTLMv2 Response)**。<br><br>  <br><br>大小高達 **700 ~ 1000+ bytes**。|這是微軟私有的擴充協定。雖然在 Exchange 內網很常見，但在標準 SMTP 宇宙中是個「大胖子」。|

## ⏳ 為什麼認證過程會產生「5 秒延遲」？（這絕對不標準）

在一般的網路環境下，即便使用 NTLM 認證，整個交握過程通常也在 **幾毫秒 (milliseconds)** 內就會完成。**延遲整整 5 秒鐘，在網路協定中是一個巨大的紅色警訊（Anomaly）。**

這 5 秒鐘的延遲，暴露了 Exchange 幕後正在發生的「內部拉鋸戰」：

1. **Active Directory (AD) 查無此人：**
    
    當 Exchange 收到這個 Type 3 驗證請求時，它自己無法驗證，必須把這串 761 bytes 的 Token 丟給後台的**網域控制站 (Domain Controller, DC)** 去比對。
    
2. **逾時 (Timeout) 機制被觸發：**
    
    因為攻擊者輸入的是一個瞎編的網域與帳號（`DESKTOP-8COJGKO\Patrici A Dminister`）。DC 在收到請求後：
    
    - 嘗試在本地資料庫搜尋這個帳號（找不到）。
        
    - 嘗試解析 `DESKTOP-8COJGKO` 這個工作站的 NetBIOS 名稱或 DNS（找不到，開始等待回應）。
        
    - **Windows 預設的名稱解析或 LDAP 查詢逾時通常就是 5 秒鐘。**
        

這就是為什麼日誌中，從攻擊者送出 Token（`23:20:02`）到伺服器無情拒絕（`23:20:07`），不多不少剛好卡了 5 秒。

## 🎯 為什麼這會觸發 Suricata 警報？

站在 Suricata（入侵偵測系統）的角度：

1. **它預期看到的 SMTP：** 快速、輕量的文字指令交換。
    
2. **它實際看到的狀況：**
    
    - 用戶端突然塞了一大串長達 761 序列、看似亂碼的 Base64 資料（NTLM Token）。
        
    - 接著，整個 TCP 連線**瞬間安靜了 5 秒鐘**。
        
    - 5 秒後，伺服器突然拋出一個 `535` 拒絕回應，而用戶端連「重置（RSET）」都省了，直接在同一毫秒內強行塞入 `MAIL FROM`。
        

這種「大封包 + 異常延遲 + 違背 RFC 狀態機」的行為，在 Suricata 的剖析器（Parser）眼裡，就像是 TCP 串流已經損毀、去同步（Desynchronized），或是有人在利用 SMTP 漏洞進行緩衝區溢位攻擊，因此才決定大聲呼叫：**`SMTP invalid reply`（無效的 SMTP 回覆/狀態異常）**！


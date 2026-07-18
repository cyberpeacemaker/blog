---
title: "Suricata SMTP Invalid Reply Alert"
description: "Explains the Suricata smtp.invalid_reply event and how to triage protocol anomalies."
created: 2026-07-17
updated: 2026-07-18
tags: [malcolm, nsm, threat-hunting]
type: howto
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[MOC - Threat Hunting]] · [[malcolm-threat-hunting-poi]]

### **`SURICATA SMTP invalid reply` 警報解析**

這個警報是由 Suricata 的 **應用層解碼器（App-layer decoder）** 所觸發的內建事件。當 Suricata 監控網路流量時，發現某個 **SMTP 伺服器回傳給用戶端（Client）的響應（Reply）不符合 SMTP 協定標準**，就會觸發此警報。

在預設的規則庫中，該警報的特徵碼定義通常如下（對應 SID `2220000`）：

> `alert smtp any any -> any any (msg:"SURICATA SMTP invalid reply"; flow:established,to_client; app-layer-event:smtp.invalid_reply; flowint:smtp.anomaly.count,+,1; classtype:protocol-command-decode; sid:2220000; rev:1;)`

### **為什麼會觸發？協定層面的原因**

根據郵件傳輸協定 **RFC 5321** 的標準規範，SMTP 伺服器回傳的響應（Reply）必須嚴格遵守特定的格式。一個標準的 SMTP 響應是由 **3 位數字的狀態碼（Status Code）**、**分隔符** 以及 **文字說明** 組成，且每一行都必須以 `<CRLF>`（即 `\r\n`）結尾。

#### 標準與異常的 SMTP 響應對比：

|**狀態類型**|**範例格式**|**說明**|
|---|---|---|
|**標準單行響應**|`220 mail.example.com ESMTP\r\n`|3 位數字 + 空格 + 說明 + CRLF|
|**標準多行響應**|`250-First line\r\n`<br><br>  <br><br>`250-Second line\r\n`<br><br>  <br><br>`250 Last line\r\n`|前幾行用 `-` 分隔，最後一行用空格，皆以 CRLF 結尾|
|**異常（觸發警報）**|`220mail.example.com`|狀態碼與說明之間缺少空格或 `-`|
|**異常（觸發警報）**|`250 OK\n`|結尾只使用 `\n` (LF) 而非 `\r\n` (CRLF)|
|**異常（觸發警報）**|`HELLO`|響應開頭完全沒有 3 位數字的狀態碼|

當 Suricata 在已建立的 TCP 連線中（方向為 `to_client`，即伺服器到用戶端），解析到不符合上述規範的字元或格式時，就會判定為 `smtp.invalid_reply`。

### **常見的觸發場景**

1. **伺服器協定實作不標準（RFC Non-compliance）**
    
    - **這是最常見的原因。** 許多自製的發信腳本、物聯網（IoT）設備、事務機（如掃描傳送郵件）、舊型內部系統，其內建的簡易 SMTP 伺服器在撰寫時並未完全遵守協定規範（例如忘記加上 `\r`，或多行響應格式錯亂）。
        
2. **TLS/STARTTLS 加密辨識失敗**
    
    - 當郵件連線使用 `STARTTLS` 準備將明文連線升級為加密連線時，如果網路發生掉包，導致 Suricata 沒能偵測到加密交握的起點，Suricata 就會繼續嘗試以明文解析隨後的加密流量。這會導致它將「加密的二進位資料」誤判為「格式混亂的明文 SMTP 響應」。
        
3. **網路封包重組失敗（Packet Fragmentation）**
    
    - 當網路發生嚴重擁塞、封包遺失或重組錯誤時，Suricata 拼接出來的 TCP 串流可能會有資料殘缺，進而導致剖析器（Parser）解讀出錯誤的協定格式。
        
4. **惡意行為或漏洞攻擊**
    
    - 攻擊者可能故意向郵件用戶端發送畸形的 SMTP 響應，意圖觸發郵件軟體（如 Outlook、Thunderbird）的緩衝區溢位（Buffer Overflow）或解析漏洞。或者是惡意軟體在非標準埠上使用自訂的通訊協定，卻被 Suricata 誤認為是 SMTP 流量。
        

### **如何調查與處置？**

- **步驟一：確認來源與目的 IP 屬性**
    
    - **外部知名伺服器**：如果 `Source IP` 是 Google、Microsoft 等大型郵件商，且使用 25/587/465 埠，這高機率是 **STARTTLS 加密識別失敗** 或 **網路掉包** 引起的誤報（False Positive）。
        
    - **內部主機**：如果 `Source IP` 是內部的某台特定伺服器或設備，請檢查該設備上的發信程式、印表機或系統排程，通常是這些系統的發信程式碼寫得不夠嚴謹。
        
- **步驟二：分析 PCAP（封包側錄）**
    
    - 若有開啟側錄，可以在 Wireshark 中追蹤該連線的 **TCP Stream**，切換至 Hex（十六進位）模式，檢查伺服器回傳內容的結尾是否確實為 `0d 0a`（即 `\r\n`）。
        
- **步驟三：評估是否需要過濾警報**
    
    - 這類警報通常屬於協議合規性（Anomaly Detection）檢查，而非立即性的惡意攻擊。
        
    - 如果確認是內部 legacy 系統或正常業務流量造成的誤報，且不影響郵件收發，建議在 `threshold.config` 中將此警報進行**過濾（Suppress）**，或者在 `disable.conf` 中直接禁用此內建事件規則（SID `2220000`），以避免日誌充斥無用訊息。

---

Starting threat hunting with Suricata alerts is an **excellent** choice—but with one massive, candid caveat.

If you simply sit in front of a dashboard, wait for Suricata to fire an alert, and then look up what that alert means, you aren't actually threat hunting; you are doing **Alert Triage** (reactive).

True **Threat Hunting** is proactive and hypothesis-driven. Instead of waiting for an alert to turn red, you ask a question like: _"Is there any internal host making DNS requests for weird Top-Level Domains (TLDs) like `.top` or `.xyz`?"_

That being said, Suricata is a goldmine for hunting because of its high-performance protocol parsers and its highly detailed `eve.json` log file. It doesn't just generate alerts; it extracts HTTP, DNS, TLS, SMTP, and Flow metadata.

## Guidelines for Utilizing Suricata for Threat Hunting

To transition from a passive alert-watcher to an active network hunter, use this framework:

|**Phase**|**Action**|**Why it Matters**|
|---|---|---|
|**1. The Pivot**|Never look at an alert in isolation. Use the `flow_id` in Suricata's JSON output.|Allows you to reconstruct the entire session. If you see an alert, find the corresponding DNS or HTTP log to see what the machine did _right before_ the alert.|
|**2. Baselining**|Group alerts by Signature ID (SID) or Message over a 30-day period.|Identify the top 5 loudest alerts. These are almost always noisy false positives. Tune them out so you can spot the quiet, dangerous signals.|
|**3. Focus on Anomalies**|Look for application-layer decoder events (like the SMTP one you found).|Attackers often violate RFC protocols to tunnel Command and Control (C2) traffic or bypass standard network filters.|

## Deep Dive: `"SURICATA SMTP invalid reply"`

Let's dissect the specific alert you asked about.

### 1. What is the Signature?

This is a built-in Suricata application-layer rule (SID: `2220000`):

Code snippet

```
alert smtp any any -> any any (
    msg:"SURICATA SMTP invalid reply"; 
    flow:established,to_client; 
    app-layer-event:smtp.invalid_reply; 
    flowint:smtp.anomaly.count,+,1; 
    classtype:protocol-command-decode; 
    sid:2220000; 
    rev:1;
)
```

### 2. What Triggers It?

Suricata's SMTP parser actively monitors TCP streams identified as SMTP (typically port 25, 587, or 465).

According to the official SMTP specification (RFC 5321), every server reply _must_ start with a **three-digit numeric code** (like `220` for ready, `250` for OK, or `550` for error) followed by a space or a hyphen, and end with a Carriage Return + Line Feed (`<CRLF>`).

If Suricata observes traffic from the "server" to the "client" on an SMTP stream, and the server's reply **does not conform** to this structure (e.g., it contains random text without a 3-digit code, binary data, or missing line terminators), Suricata logs an `smtp.invalid_reply` event.

### 3. Triage & Investigation Plan (How to Hunt This)

When investigating this alert, you want to differentiate between administrative mistakes, network interference, and actual attacker behavior:

- **Scenario A: The "Middlebox" Interference (Most Common - False Positive)**
    
    - _What happens:_ Many modern firewalls and security gateways use "SMTP Deep Packet Inspection" features. Often, these middleboxes silently strip commands, rewrite headers, or inject error messages to block threats. In doing so, they sometimes format the packet incorrectly, causing Suricata's strict protocol parser to trigger.
        
    - _How to spot:_ Look at the destination or source IP. Is it your corporate firewall, mail gateway, or proxy?
        
- **Scenario B: Protocol Tunneling (High Severity - True Positive)**
    
    - _What happens:_ Attackers know that port 25 is often left open on firewalls to let mail flow. To sneak data out of the network, they might tunnel an entirely different protocol (like SSH, custom HTTP-like traffic, or reverse shell commands) over port 25. Because their custom Command & Control server isn't sending real SMTP replies, Suricata's parser breaks and fires this alert.
        
    - _How to spot:_ Pivot to the flow logs and check the payload or PCAP. If you see raw encrypted binary data, SSH banners (`SSH-2.0...`), or shell commands instead of email headers, you've found an active compromise.
        
- **Scenario C: Misconfigured Mail Server (Low Severity - False Positive)**
    
    - _What happens:_ A developer set up a custom notification script on an internal server to send emails, but the script's handshake or local mail daemon is broken, sending raw unformatted text rather than proper SMTP codes.
        

To help you get hands-on with this, **are you currently practicing with a homelab setup, analyzing a pre-captured PCAP file, or working in a production environment?**
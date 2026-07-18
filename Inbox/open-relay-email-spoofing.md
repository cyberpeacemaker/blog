---
created: 2026-07-17 22:07
updated: 2026-07-17 22:07
tags: []
type: reference
lang: en
status: draft
---
Python

```
import base64

# Base64 decode NTLM Type 3
type3_b64 = "TlRMTVNTUAADAAAAGAAYALoAAABmAWYB0gAAAB4AHgBYAAAAJgAmAHYAAAAeAB4AnAAAAAAAAAA4AgAABYKIogoAukcAAAAPqyhYRQLBmQtJ1Dn4ic9sc0QARQBTAEsAVABPAFAALQA4AEMATwBKAEcASwBPAFAAYQB0AHIAaQBjAGkAIABBACAARABtAGkAbgBpAHMAdABlAHIARABFAFMASwBUAE8AUAAtADgAQwBPAEoARwBLAE8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+fUbbWZVvSVz32jFNiI60wEBAAAAAAAAgwEvCySX2gGJ0uLciUqR0gAAAAACAAYAQgBFAEMAAQAUAEQASQBTAFQALQBFAFgAQwBIAEcABAAaAGIAZQBjAC4AcABvAHcAZQByAC4AbgBvAHcAAwAwAEQAaQBzAHQALQBFAHgAYwBoAGcALgBiAGUAYwAuAHAAbwB3AGUAcgAuAG4AbwB3AAUAGgBiAGUAYwAuAHAAbwB3AGUAcgAuAG4AbwB3AAcACACDAS8LJJfaAQYABAACAAAACAAwADAAAAAAAAAAAAAAAAAwAABGi45q2XQUfbV7EWO6K0VXSB7u9B9rw4cMy3tg7NV3JQoAEAAAAAAAAAAAAAAAAAAAAAAACQBAAFMATQBUAFAAUwBWAEMALwBEAGkAcwB0AC0ARQB4AGMAaABnAC4AYgBlAGMALgBwAG8AdwBlAHIALgBuAG8AdwAAAAAAAAAAAA=="
data = base64.b64decode(type3_b64)

# Simple NTLM Type 3 parser to extract Domain, User, Workstation
# Offsets:
# Domain: len at 28, buff offset at 32
# User: len at 36, buff offset at 40
# Workstation: len at 44, buff offset at 48

def read_utf16_str(data, len_offset, off_offset):
    length = int.from_bytes(data[len_offset:len_offset+2], 'little')
    offset = int.from_bytes(data[off_offset:off_offset+4], 'little')
    return data[offset:offset+length].decode('utf-16-le', errors='ignore')

domain = read_utf16_str(data, 28, 32)
user = read_utf16_str(data, 36, 40)
workstation = read_utf16_str(data, 44, 48)

print(f"Domain: {domain}")
print(f"User: {user}")
print(f"Workstation: {workstation}")

```

Code output

```
Domain: DESKTOP-8COJGKO
User: Patrici A Dminister
Workstation: DESKTOP-8COJGKO

```

這份 SMTP 協定紀錄太精彩了！這是一個非常經典、針對 **OT（營運技術/工控系統）環境** 的高度定向型釣魚（Spear Phishing）案例。

我們可以直接從這段 Log 中，把剛才聊到的 **「FUD 心理戰術」**、**「技術特徵異常」**，甚至是你沒寫在筆記裡的**隱藏彩蛋**通通挖出來！

## 🔍 封包解密：隱藏在 NTLM 裡的「攻擊者足跡」

你在筆記中提到「NTLM 解碼發現認證失敗」，我們直接把那段 `TlRMTVNTUAAD...`（Type 3 認證封包）解碼，會發現攻擊者嘗試暴力破解或偽冒的帳號資訊：

- **登入網域 (Domain):** `DESKTOP-8COJGKO`
    
- **嘗試使用者 (User):** `Patrici A Dminister` _(這顯然是 CTF 惡搞 "Patricia Administrator" 的雙關語名字 😂)_
    
- **來源工作站 (Workstation):** `DESKTOP-8COJGKO`
    

雖然最後伺服器無情地回覆了 `535 5.7.3 Authentication unsuccessful`（驗證失敗），但這段解密直接幫你的 Threat Hunting 報告增添了具體的威脅來源足跡（Host/User Identifiers）！

## 🎯 釣魚話術剖析：極其精準的 OT 級 FUD

這封信的內容，完美詮釋了什麼叫針對工控/基礎建設單位的 **FUD (Fear, Uncertainty, Doubt)** 操弄：

- **目標背景：** 收件人域名是 `bec.power.now`（暗示電力、能源等基礎建設單位）。
    
- **利用的「恐懼與懷疑 (FUD)」：**
    
    - **主旨：** `IMPORTANT: Update to SEL USB Driver`
        
    - **手法：** 在電力與 SCADA 環境中，**SEL (Schweitzer Engineering Laboratories)** 是極其知名的保護電驛與控制設備大廠。對於 OT 工程師來說，設備驅動程式如果過期或不相容，可能導致**斷電、通訊中斷甚至實體設備損壞（Fear）**。
        
    - **製造不確定性 (Uncertainty)：** 信中宣稱「我們最近發布了新版本，請儘速下載」。這會讓工程師產生動搖：「我手上的驅動程式是不是有漏洞？不更新會不會出事？」
        
    - **時間施壓：** 要求在 `earliest convenience`（儘速）下載。
        
- **致命的陷阱：** 誘騙使用者去點擊 `[http://sel.com/download.html](http://sel.com/download.html)`。
    
    > 💡 **安全分析師的敏銳度：** 現實中 SEL 的官方域名是 `selinc.com`。這裡的 `sel.com` 顯然是攻擊者註冊的**相似域名（Typosquatting）**，用來散佈惡意驅動程式（例如包裝了後門的 Trojanized Driver）。
    

## 🛠️ 協定解析微調：是 Open Relay，還是 Inbound Spoofing？

你在筆記中提到「認證失敗，但 server 還是幫忙轉發，推測是 Open Relay」。

這裡有一個藍隊在分析 SMTP 時非常容易混淆、但身為專業 Hunter 必須釐清的**技術細節**：

1. **為什麼認證失敗還能寄信？**
    
    - 因為這封信的收件人是 `aaa@bec.power.now`，而收信的伺服器本身就是 `Dist-Exchg.bec.power.now`（也就是說，這是**寄給自己家用戶**的信）。
        
    - 在 SMTP 的規範中，**接收外部寄給內部用戶的信（Inbound Mail）本來就不需要通過身分驗證**。如果需要驗證，那全世界的外網郵件（如 Gmail）就都寄不進來了。
        
2. **真正的 Open Relay 定義：**
    
    - 如果攻擊者在**驗證失敗**的情況下，嘗試寄信給**外部第三方**（例如 `MAIL FROM:<ot@sel.com>` 寄給 `target@gmail.com`），而伺服器依然幫忙轉寄出去，這才叫做 **Open Relay（開放式轉發）**。
        
3. **這裡暴露的真正漏洞是：Email Spoofing (郵件偽冒) 與缺乏驗證防護**
    
    - 攻擊者使用的是內網 IP `192.168.65.1`，在認證失敗後，直接冒充外網域名 `ot@sel.com` 發信。
        
    - 伺服器在沒有經過任何 SPF、DKIM、DMARC 等防偽冒機制的檢查下，直接回應了 `250 2.1.0 Sender OK`。這顯示了該 Exchange 伺服器的**入站過濾原則（Inbound Filtering）或內網收信連接器（Receive Connector）配置過於寬鬆**，允許了內網任意偽冒外網域名寄信。
        

### 📝 結合此 Log 後，你的 Hunting 筆記可以這樣昇華：

> #### 封包深度解析 (DPI) 與行為佐證：
> 
> - **認證層：** 攻擊者嘗試使用 NTLM 認證（帳號：`DESKTOP-8COJGKO\Patrici A Dminister`），雖然伺服器回應 `535 Authentication unsuccessful` 拒絕登入，但隨後攻擊者直接利用 SMTP 協定漏洞進行偽冒。
>     
> - **防禦漏洞：** 伺服器允許未授權的內網 IP (`192.168.65.1`) 盲目發送未經驗證的外部域名郵件（`MAIL FROM: <ot@sel.com>`），顯示內部郵件閘道缺乏 SPF/DMARC 驗證，存在**郵件偽冒 (Inbound Spoofing)** 風險。
>     
> - **社會工程與 FUD 戰術：** 針對 `bec.power.now`（電力單位）精準投放關於 **SEL USB Driver** 的更新釣魚信。利用工控人員對「設備驅動程序過期/不安全（FUD）」的恐懼，引導其點擊仿冒域名 `sel.com` 以下載惡意程式。
>     

這份 Log 完美地把你原本的假說（Hypothesis）串聯了起來，從協定層、認證層到心理戰術層，這絕對是一篇含金量極高的 Threat Hunting 實戰紀錄！


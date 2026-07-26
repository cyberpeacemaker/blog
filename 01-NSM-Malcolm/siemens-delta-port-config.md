---
title: "Siemens Delta Port Config"
description: "解釋 Siemens 與 Delta 工控演練箱網口配置可能相反的拓撲與設備原因。"
created: 2026-07-26
updated: 2026-07-26
tags: [malcolm, nsm]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[modbus-s7comm]] · [[ot-hmi-ews-plc-rtu]]

你**很可能沒有寫錯**。這兩個接法看起來相反，是因為**工業設備本身的網卡屬性**以及**演練箱內部的網路拓撲規劃**不同，工控領域並沒有「Port 1 必定是外網」這種統一規定。

會出現這種「相反」現象，主要有以下三個原因：

### 1. 演練箱的網路拓撲與防火牆規劃（最主要原因）

在工控演練箱（OT Lab Box）中，內部的網路安全模組（如工業防火牆、網關、路由器）都是由當初設計演練箱的人自訂 IP 網段與 VLAN 劃分：

- **西門子 (Siemens) 模組設定**：設計者將 Port 1 劃分為 WAN（對外），Port 2 劃劃為 LAN（供你的實體筆電存取或進行操作）。
    
- **台達 (Delta) 模組設定**：設計者可能將 Port 1 劃劃為內部 LAN（專門用來連接演練箱內建的 Ubuntu 控制機/攻擊機），而 Port 2 劃劃為對外網路（WAN）。
    

### 2. 「交換機模式」還是「路由器模式」

- **純 Switch 模式（二層 Bridging）**：如果該設備只是普通 PLC 的雙網口（如 PROFINET 雙孔）或工業交換機，Port 1 和 Port 2 內部其實是通的。這種情況下插哪一孔運作起來都一樣，筆記寫 Port 1 / Port 2 只是為了方便操作者統一線路走向。
    
- **Router / Firewall 模式（三層 Routing）**：如果該設備是工業路由器（例如 Siemens Scalance S615 或 Delta DX 系列），Port 1 與 Port 2 被綁定在不同的物理網卡與網段上（例如 Eth0 是 WAN，Eth1 是 LAN），這時就**絕對不能插反**，否則封包會被防火牆擋掉。
    

### 3. 廠商硬體預設介面順序不同

不同廠商的硬體介面編號（Port Index）與面板印刷順序不同：

- 西門子常將對外/上聯埠（Uplink / WAN）習慣放在 Port 1。
    
- 部分台達或其它台廠設備，可能將 Port 1 預設為內部管理埠（LAN），Port 2 作為對外通訊埠。
    

### 如何快速驗證有沒有插對？

你可以透過以下方式確認連線是否正確：

1. **檢查 IP 網段**：筆電與 Ubuntu 接上去後，執行 `ipconfig` (Windows) 或 `ifconfig / ip a` (Ubuntu)，確認拿到的 IP 是否屬於正確的 LAN 網段。
    
2. **Ping 測試**：試著從筆電/Ubuntu Ping 演練箱內的 PLC 或 Gateway IP。如果 Ping 不通，通常就是孔插反了（被 WAN/LAN 防火牆阻擋）。
    

你目前在進行的是哪一類型的公控演練（例如：PLC 階梯圖程式修補、OT 網絡流量分析，還是 ICS 滲透攻防）？如果能提供這兩台設備的具體型號（如 Siemens Scalance S615 / S7-1200，Delta DX-2000 等），我可以幫你精準確認它們的網口預設定義。

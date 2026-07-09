# otex-devkit
pr test + typo

# Bec ctf 完整報告
- 復現Malcolm GUI上的操作
- 解釋為什麼這樣操作
**細節**
- dhcp review
poi 這樣看起來很好，加上
對解法疑惑的點
Hares的點
Arkime似乎就夠，沒用到opensearch的優勢
- query hints > detailed/rich malcolm playbook (like ctf-walkthrough-maloclm)
- verdict : verify the result from query playbook, not just infer the result  

# Probationary
1. 順便整理repo (calander)
2. ICS_TA TODO 
	1. hardware expand
	2. animation fix
3. meeting-transcript TODO
4. arkime contribute

# YAML & OKF

automated updated with git control
add [doc,survey] 自動摘要yaml, kof

```yaml
---
title: "Clear, Semantic Title"
description: "Punchy SEO summary + core semantic intent for RAG/vector filtering."
created: YYYY-MM-DD
updated: YYYY-MM-DD        # Crucial for AI to know if the knowledge is stale
type: howto                # reference | howto | hub | concept — vital for MCP routers
lang: en
draft: true

# --- AI & Agent Enhanced Fields (Infer these where possible!) ---
domain: ""                 # e.g., tech/ai, life/health — narrows RAG search scope
relations: []              # [slug-of-parent, slug-of-related] — builds the AI graph
prerequisites: []          # What the human (or agent) needs to know before reading
visibility: "private"      # private | internal | public — guards against AI data leakage
tags: []                   # For hybrid (keyword + vector) RAG search
---
```

```plaintext
knowledge/
├── index.md             <-- The master map of your repo's knowledge
├── services/
│   ├── index.md         <-- Map of your services
│   ├── auth-api.md      <-- Concept file (Short frontmatter + body)
│   └── payment-gw.md    <-- Concept file
└── database/
    ├── index.md
    └── schema.md
```

# AI
- `finish-ai-task.sh`
- auto ai categorize 'blog' (fills tags/lang)
- atuo ai syn/commite/push 'github repo'
- cursor-setup
- cursor 使用 (至少先setting, 在automation)
- claude (基本功能看看)

# Obsidian
- obsidian vault merge
- [Obsidian+Claude](https://www.youtube.com/watch?v=_ERp82MIj9Q)
- daily note + calander

# Project Shepherd
- project-scaffold in @project-shepherd/docs | session in cursour/proeject-shepherd/Project   
Malcolm threat hunting methodology 
- lamb: 需要靠CTF題目引導 (CTF題目本身就是線索)
- rabbit: 基本調查能力 (MITRE框架, 兩種方式)
- 長耳兔: 進階調查能力 (擴充rabbit能力)
	- phising mail detection
	- beacon detection
- turtle: offline
- Nebula
- Goat
- 黑山羊

# BEC v2 後續收尾
- MSDefender , Cladue設置
- pivot issue fix:
	- we have fix the opensearch-arkime-pivot issue, which might be the reason why you can't correctly retrieve the raw packet. can you try again to see if you can solve 
	
---

# 暫時推遲的事情

- 耳提面目補充
- Google Threat Intelligence
	- 結合總監想做的示意圖？
	- m-trend
	-  https://cloud.google.com/security/resources/m-trends
	- https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/
	- https://www.levelblue.com/blogs/spiderlabs-blog/an-analysis-of-valleyrat-infection-campaigns-from-fake-installers-japanese-malicious-emails
- ICS Cyber Range Lecture PPT

###  OTEX 課程
- http://10.3.3.241/
- ICS300
- [ICS, Zeek, Suricata]_101
- Malcolm_101
- 
### Project Shepherd
- Porject_BEC_v3
- lm studio
### AI Learning
- Claude_101
- Claude design rule

---

# 不太重要
- 會議同意書 (經理遇到的問題)
- google ai studio
- claroty
- 我的第九周雙周會議？
- github/personal-misc TODO 轉移
- Google Note 轉移
- Google Drive 整理
- f0c2e947be21eb5a6588448f0408779c870f7b55e4ae74e3 ABUSE 
- Alto Harness?, Auto Harness?
- 開機startup檢查
- Slack+Asana+Jira的測試
- Github action
# Hacking AI
剛剛想到可以測試一下hacking類型的AI，不過帶出幾個話題
 - local llm
 - destiliate
 - mcp

---

# ICS CTF LAB 優化
- 首先 這裡我覺得很適合添加一個skill <module_create>
currently, there is one aggregated/incremented fact files. but i;d like to seperate them as different specific purpose/characteristic files.

# playbook的優化
### Format
- Design Philosophy section完全不用
- Final workflow 可以整合 EX:
```bash
python scripts/dpi.py    smb --dataset attack --pcap data/raw/OT_Attack.pcap (Optional: full reproduction from the raw capture)
python scripts/select.py     --dataset attack --field dpi.smb.native_os

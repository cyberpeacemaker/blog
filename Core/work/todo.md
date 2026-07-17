# Routine
- project-shepherd logo
- PR check
# Now
1樓 院長感謝卡
- nics claw 回復 (這是要回啥？是要我整理minute嗎?)
- 桃園meeting minutes
- bec ctf 完整報告 (unencrypted channel, dnp3異常覆現, cleartext category)
- 護照
- mdm 重開機測試
- 桃園出差結報
- vmware
- cursor-rule
- [git 101]([Introduction - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/intro-to-git/0-introduction))
- [claude 101](https://www.anthropic.com/learn)
- new project
	- claude
	- gitignore
- cycom


# Bec ctf 完整報告
我之前可能用不太適合的角度切入CTF，我偏向抑制/阻止去看明文資料，而是透過threat hunting methodology/encrypted traffic analytics/behavior analysis等角度去切入
不過實際上這個CTF，可能就是希望我去看C2明文指令，去了解基本的C2指令

```markdown
- 8 pcaps — no HTTP bodies carved (likely large tool-download pcaps with no small beacon bodies; several are byte-identical duplicates per `manifest.json`).
- 1 session (`JAS5fnkTcEVHjZ...`) — 9 bodies, all high-entropy binary (multipart upload chunks); no `decoded_text`, so omitted by design.
```
- 推估是temp?
- 復現Malcolm GUI上的操作, - 解釋為什麼這樣操作
- 調查完後 想聽別人解法
poi 這樣看起來很好，加上
- 對解法疑惑的點 (忘了這是什麼？)
- Hares的點 (太簡單，犯人自稱犯人)
- Arkime似乎就夠，沒用到opensearch的優勢
- query hints > detailed/rich malcolm playbook (like ctf-walkthrough-maloclm)
- verdict : verify the result from query playbook, not just infer the result  

# Probationary
1. 順便整理repo (calander)
2. bookmark
3. asana
4. ICS_TA TODO 
	1. hardware expand
	2. animation fix
5. meeting-transcript TODO
6. arkime contribute
7. 想工作
8. 承諾 三個月薪水 不是為了賺錢 
9. appendix

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
- obsidian vault organize
- obsidian vault merge
- [Obsidian+Claude](https://www.youtube.com/watch?v=_ERp82MIj9Q)
- daily note + calander
- frontmatter (OKF, AI, Automation)

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
- front matter tmeplate
- linter, git hhok

# BEC v2 後續收尾
- MSDefender , Cladue設置
- pivot issue fix:
	- we have fix the opensearch-arkime-pivot issue, which might be the reason why you can't correctly retrieve the raw packet. can you try again to see if you can solve 
	
---

# 暫時推遲的事情

- cisa派訓
- cyber storm cisa
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
- [gsap](https://gsap.com/docs/v3/Installation/)
- github profile [readme tool](https://www.readmecodegen.com)
- PI, Tau
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

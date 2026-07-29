# Routine
- project-shepherd logo
- PR check

# Threat hunting
- 自動threat hunting
- 自動產生ticket
- 自動產生資庫庫
# Probationary
- 字多詳細、提供技術細節、同時顧慮他人能看懂，描述背景、遇到什麼困難解決什麼問題、beforeafter 差異、做出什麼貢獻 完成
- -工作上面展現的貢獻
- 很會整理，到底貢獻在哪裡
- 發現有這問題 提出這個流程圖 希望可以讓學生更容易理解
-  有什麼貢獻

- 解惑那些題目
設備排解那些題目
協助未來備課更快速上手、協助學員理解，成為組內可參考教材
包含手冊
TRAPA回饋

因應維運AI驗證機構業務發展驗證方案之需求，研析ISO/IEC TR 24368:2022標準中，與5大自動化評測項目(可靠性、公平性、準確性、隱私及資安)有關之處建立技術要求，以利後續發展驗證方案中，對AI產品開發者提出之要求與規範，以隱私為例
114/7/8協助完成AIEC評價報告



協助辦理與TAIDE開發團隊交流會議
協助撰寫3次會議紀錄
發布1次會議通知
完成1次會議結報


收到的回饋，對於組內開發有什麼幫助

幫助組內情資產生
就算沒立刻使用，也可以成為組內備用量能，或是其他工具參考

價值、貢獻
對象是講給林副聽，不是給HR聽

研析導入工業標準
制定工作流程
之前沒有任何流程，因此我們兩人持續討論，去打造制度流程
之後執行就能更有效率、順利的
確保品質把關、合作減少衝突

---
- 醫院保密切結書 (四個單位)
- 拿貼紙
- ppt
	- 貢獻
	- 技術細節
- malcolm report
	- 目前最新技術在台鐵
	- 目前撰寫環境先回到(BEC_v2)，可能需要搬部分資料回來(nics-malcolm-bec)
	- 做完在搬遷到`nics-malcolm-bec`
	- hunt lead
	- 69跟AD互動 鎖定兩台受害者 是因為DNS反向查詢有回傳
- ppt rehersal
	- 中文題目link失效？
---
- 檔案文件大小 (font package) & links
- kpi-1.
- kpi-2-1. ta-cja: 80%
- kpi-2-2. ta-ics: 90%
- kpi-3. iii-interview: 90%
- kpi-4-1. nics-claw: 90%
- kpi-4-2. nics-anthropic: 90%
---
- shepherd

# Now

- new bec project standard of process
- nics-probationary
- bec report
- template (markdown, skill, minute additional instruction)

# 暫時推遲

- 測otex-claw 前端 + 現場
- 新光醫院保密，不用填申請日期
- 護照 > CISA(ESTA) > 開戶
- GTI CTF
- ac-hunter CTF
- git control for demo (different version)
- human agent audience doc


# frontmatter & OKF

- automated updated with git control
- add [doc,survey] 自動摘要yaml, kof

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
- 101 claude
- 101 cursor, vscode agent
- `finish-ai-task.sh`
- auto ai categorize 'blog' (fills tags/lang)
- atuo ai syn/commite/push 'github repo'
- cursor-setup
- cursor 使用 (至少先setting, 在automation)
- claude (基本功能看看)



# BEC v2 後續收尾
- malcolm 製作lab 製作封包 製作poc
- MSDefender , Cladue設置
- pivot issue fix:
	- we have fix the opensearch-arkime-pivot issue, which might be the reason why you can't correctly retrieve the raw packet. can you try again to see if you can solve 
	
---

# 暫時推遲的事情

- cursor-rule
- [AIxCC](https://aicyberchallenge.com/overview/)
- [git 101]([Introduction - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/intro-to-git/0-introduction))
- [claude 101](https://www.anthropic.com/learn)
- new project template
	- claude
	- gitignore

- opensearch api + agent skill
- 耳提面目補充
- cyber storm cisa
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
-  vmware
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
- -cycom
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

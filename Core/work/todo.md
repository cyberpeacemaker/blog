# Routine
- project-shepherd logo
- PR check


# Emergency

- ppt | 這三個月的整理(BEC , porject-shepherd, misc) | bookmark
	- meeting-note > nics-meeting-minute
- 出國準備
	- ESTA
	- 訂飯店
	- 行李箱
- 匯豐
	- 08/07(五)12:00開戶 (身分證、第二證件、印章)
	- 信用卡 + 附卡 (叫爸媽用)
	- 綁卡 (自動繳費)
	- 從別的帳戶轉錢
	- 別的銀行賣商品
- 訂生日蛋糕 (卡片)
- 回八里家參考個人事項

# Appending
- obsidian automaion
- obsidian 其他vault的整理
- daily auto git pr
- 整理repo (sync, gitignore)
- GTI CTF
- ac-hunter CTF
- git control for demo (different version)
- human agent audience doc
- new bec project standard of process
- asana
- template (markdown, skill, minute additional instruction)
- 玉山信用卡開卡、綁卡
- 看信
- 安全帽
# malcolm report
- 目前最新技術在台鐵
- 目前撰寫環境先回到(BEC_v2)，可能需要搬部分資料回來(nics-malcolm-bec)
- 做完在搬遷到`nics-malcolm-bec`
- hunt lead
- 69跟AD互動 鎖定兩台受害者 是因為DNS反向查詢有回傳
- 半年報告 AI

# BEC v2 後續收尾
- malcolm 製作lab 製作封包 製作poc
- MSDefender , Cladue設置
- pivot issue fix:
	- we have fix the opensearch-arkime-pivot issue, which might be the reason why you can't correctly retrieve the raw packet. can you try again to see if you can solve 
---

# AI
- 101 claude
- Claude design rule
- 101 cursor, vscode agent
- `finish-ai-task.sh`
- auto ai categorize 'blog' (fills tags/lang)
- atuo ai syn/commite/push 'github repo'
- cursor-setup
- cursor 使用 (至少先setting, 在automation)
- claude (基本功能看看)
- Hacking AI

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

我上次的meeting report放哪裡？怎麼會不再這個資料夾？怎麼會這樣！真的詩詩意了
好像真的睡覺太少，大腦無法最整理思考的內容
### Automation
- obsidian 日記整理
- git auto commit?
**some issue need to fix/discuss**
The working tree is clean on `cursor/daily-inbox-triage-9370`; the task’s triage prompt explicitly asks for an `automation/daily-inbox-triage-*` branch, so I’m creating today’s triage branch from the current checked-out state before editing.

The first staging command used explicit source paths after `git mv`, which Git no longer sees as filesystem files. I’m restaging the move phase with `git add -A` and committing the same move-only changes.

The finish script is present, but it performs `gh pr create` and `gh pr merge --admin`; I’m first completing safe verification and confirming the tree is clean before deciding how to handle that requested wrap-up under the environment’s GitHub write restrictions.

The rebuild succeeded but rewrote `Vault Map.canvas` again, which means the generated edge ordering is slightly nondeterministic. I’m committing the latest generated artifact so the finish step can start from a clean working tree.

The PR automation expects the platform-designated branch `cursor/daily-inbox-triage-9370`, while the task prompt asked for an `automation/*` branch. I’ve already pushed the `automation/*` branch, and I’m now copying the completed commits onto the expected Cursor branch so the configured PR tool can publish the work.

- - Ran requested finish script, but it failed with:
    - `Error: Refusing to finish unexpected branch: cursor/inbox-rule-application-efec`

### Git 101
預計上課考照
- 單純main
- branch, pr
- post-merge commit
- some git issue fix
- github action
- automaticlly cli verification
- ci/cd
- git squash 

# BEC CTF完整報告

我希望在周三產出BEC CTF完整報告
理想順序會是:
- 建構project-scaffold
- 使用project-scaffold打造新project
	- playbook-bec-v1
	- sn-01-rabbit-v1
- 打造sn-01-rabbit-v1 (基於Malcolm_BEC_v2 和 v3的想法)
	- 在製作CTF完整報告時，非現似乎有潛在非常大的進步空間
	- EX1: 判斷釣魚
	- EX2: 判斷C2
- 使用sn-01-rabbit-v1 挑戰 BEC ，並使用report，製作playbook-bec-v1
- 製作完playbook-bec-v1後，製作我的BEC完整報告

## Progress
- writeup範本
- 需要補足的知識
- 需要持續改寫的方向
- rabbit淺在可能很大的改進空間 (CTF太簡單)
- threat hunting tool 跟 CTF write up 分開

---

# CTF Playbook 
## 1
請根據下面的要求翻修/增加細節
- 推測作者用意。(EX:題目是123456789 * 999999，可以硬算，但作者可能希望你了解交換律，如果使用就可以解的很舒服)
- 說明解題策略。看到題目立刻想到什麼解法，在過程中可能因為遇到困難、或看到一些缺陷，又有了一些新法。一個問題通常不只有一種解法，從不同解法去驗證題目答案也是一種很好的方式。
- 說明解題思路。有了解題策略，請詳細解釋步驟過程。(EX:懷疑主機被控制:可能是觀測到前往過釣魚domain，然後觀測到這個時間點後有behavior split的狀況，前往從沒去過的ip，進一步觀測與該IP的連線，發現傳輸的檔案hash值有被標為已知惡意。整個過程都需要解釋使用什麼方式、驗證的)
- online驗證資訊。解題思路中用到的資訊，都必須online驗證。(EX: 使用filter得到的結果，確實跑過確認可以佐證解法。而不是推測這個filter可以拿到佐證解法而已)
- scope。也許透過後面得到的答案可以很輕鬆回推前面的答案，(EX:確定的C2 agent, Server IP, etc)，但請用題目順序獲得的資訊來解。
## 2
目前還是很不滿意，不過應該是往前進了，新的兩個方向
- 使用project的script/api (這其實不算壞事，應該是我沒指定清楚用意)
- 解法我一看就不滿意，j似乎無法套用到真實情況

# Obsidian 
剛剛立刻注意到一件事
personal [work, todo]雖然不算機密，不過感覺還是分開好了
blog還是篇比較公開，主要應該是demo展示的話，不會希望這個出現

驚喜
- git + obsidian sync
- MOC
- wikilink
- My Stack
- metadata
- **auto-update internal links** (obsidian setting)
- canvas
- plugin
	- obsidian git
	- tag wrangler
	- calendar
	- dataview
	- templater
	- canvas
- 挖掘obsidian其他功能
	- daily
	- https://www.youtube.com/watch?v=hdYzsdUZ9Jg

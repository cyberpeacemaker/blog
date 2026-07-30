
# 
- ax: 有必要做這個嗎、有價值嗎
- cp: 做的出來嗎？AI做不到啦
- xt: 表現好嗎？會有幻覺吧
- xd: 這困難嗎？這沒有技術含量

總監好，沒事沒有人欺負我，早上說難過只是時間這邊有點感受到挫折。我後來自己想了一下大概明白是類似這樣：假設我在開發一個工具，好比說計算機的時候，可能會頻繁受到質疑 
1. 做這東西有價值嗎？開發這工具的時間我已經算完好幾題目了！
2. (等這東西價值可能被認可後) 這東西做得出來嗎？如果沒辦法像我一樣很擅長快速心算，怎麼有辦法做出計算機？
3. (等這東西雛型開始出來後) 這東西準確率高嗎？這工具會出錯吧！
4. (等這東西逐漸完成後) 做這東西是不是很簡單？開發這東西沒有技術含量吧！
   
但我後來發現，其實這似乎蠻大一部分，是來自於可能目前有些人，本身對AI的排斥或質疑吧？所以內心就有好點，跟總監分享～

# 向 

Otex冷靜一下，目前頂多就是youtrack以前的例子沒那麼理想，對嗎？
- GTI是很寶貴的資源，如果我想，我完全可以用自己的方式來利用GTI
- YouTrack管理系統也還可以，頂多是目前使用的情況有點怪怪的？理論上每張ticket下，應該會根據GTI情資，產生多個hypothesis獵捕。目前卻是sub-tech ticket直接忽略，所有的都放在parent-tech ticket。
- 最慘烈的就是hypothesis的形成，跟GTI一點關係也沒有？
- 子霖的看起來很棒
# OTEX

## 流程開發/測試
做這種類似algo開發的工作，真的很有趣
目前來說
- 第一階段大體可以，剩下小細節的確認/調整/優化
- 第二階段，看起來總體也是可以，不過接下來大概就要想，怎麼規劃配置了。目前有種想法，目標是可以用在malcolm上調查的hypothesis/approach，然後應該會想確認隨著MITRE, GTI資訊增加，是否能生成更好的優化

## Repo 架構設計調整/整理
- 第一點，目前

# MISC
- 判定敏感資料確實有點不容易，目前我只是單純想走前半部理論上，理論上是絕對安全的公開情資處理，不過當我想要選擇一個範本來當作參考的時候，這個範本本身應該是敏感的？
- 我可能需要寫個script來(A無介入I)來脫敏
- hunt template (should propose couple hypothesis)
- 目前time window是個有點複雜的話題

---
會議記錄
- 散會時間 需要
- 內容 可以略

交通: 30km 應該是googlemap路程距離

國外出差
- 當地日期時間 (如果凌晨返台，就算隔天)
- 通常兩天會議，會是四天三夜行程
- 台灣去美國會當天到

統編名稱: 9個字，國家資通安全研究院

國外單據
梅統編 印出來簽名、蓋章

參考資料: https://ia.dgbas.gov.tw/

---

# AI
- "Agents rarely auto-discover templates unless told
- script-skill-rule-framework
- hook

# 國外出差
otex耳提面目標號跟nics不依樣
- todo:修改trip文件 (詳細指引，錯誤編號修改...)
- todo: 試算表自己不會加總錢？
- 請假日期到底是啥？飛機起訖日？
- 有空再來確認明細內容
---


nicscclaw第零次會議它儲存的位置並不好，照理說還沒有被分類的應該都被放在meeting-note

# 會議記錄
可以考慮會議範本
人事時地物
decision, action item

不過當時我的情況應該是正在打造Project-shepherd，而且應該說我
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

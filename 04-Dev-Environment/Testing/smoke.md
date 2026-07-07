---
created: 2026-05-25
tags: [dev]
type: reference
lang: en
status: draft
---

### 1. Smoke Run / Smoke Testing

A **smoke run** (more commonly called a **smoke test**) is a quick, preliminary test to see if a system, script, or application is fundamentally broken before you dive into deeper, more complex testing.

* **The Origin:** It comes from hardware engineering. If you plug in a new circuit board and literally see smoke coming out of it, the test is over—it failed. You don't bother checking if the software loads.
* **In CTFs / Security:** If you just wrote a custom Python exploit for a CTF, a "smoke run" means firing it against a local, dummy target or just running the basic syntax to see if it immediately throws a stack trace or syntax error. It answers the question: *“Does this script even run without immediately crashing?”*

### 2. Smokescreen

A **smokescreen** is a diversionary tactic. It is designed to distract the defenders (Blue Team) from what the attackers (Red Team) are actually doing.

* **In Security:** An attacker might launch a noisy, highly visible Distributed Denial of Service (DDoS) attack against a company's web server. While the security operations center (SOC) is panicking and focusing all their resources on stopping the DDoS, the attacker quietly slips in through a backdoor to steal the database. The DDoS was just a smokescreen.
* **In CTFs:** During Attack/Defense CTFs, a team might flood the network with noisy, fake exploit traffic to hide their real, working exploit so other teams can't easily capture their traffic and reverse-engineer it.

### 3. Smoke and Mirrors

This refers to deception, obfuscation, or things designed to look highly complex or intimidating but lacking real substance underneath.

* **In Security:** Malware authors use "smoke and mirrors" by packing, encrypting, or heavily obfuscating their malicious code to confuse reverse engineers and antivirus software.
* **In CTFs:** Challenge creators love smoke and mirrors. You might find a binary that generates thousands of lines of useless assembly code (junk code) just to hide the one simple function that actually checks your password. Honeypots (fake vulnerable servers designed to trap attackers) are also classic smoke and mirrors.

### 4. Smoking Gun

A **smoking gun** is irrefutable, undeniable evidence of an event, an intrusion, or a crime.

* **In Security / Forensics:** If an incident responder is investigating a data breach, finding a web access log that shows an external IP address injecting a SQL command and successfully downloading `/etc/shadow` is the smoking gun. It proves exactly how and when the breach happened.
* **In CTFs:** In Digital Forensics or Incident Response (DFIR) challenges, your goal is often to find the smoking gun. You are digging through memory dumps, Wireshark packet captures (PCAPs), or Windows event logs to find the exact moment the "attacker" compromised the machine.

### 5. Magic Smoke

This is a playful, older hacker term specifically related to hardware hacking, IoT security, or physical penetration testing.

* **The Joke:** Tech people joke that all electronic components operate on "magic smoke" trapped inside the chips.
* **In Practice:** If you wire something backward, short-circuit a motherboard, or push too much voltage into a router you are trying to extract firmware from, the component will physically burn out. When this happens, hackers say they **"let the magic smoke out,"** meaning the hardware is permanently dead.

---


### 1. Smoke Run / Smoke Testing (冒煙測試)

* **中文翻譯：** 冒煙測試
* **由來：** 這個詞的字面意思非常直白，最早源自於**硬體工程與水管維修**。在硬體領域，當工程師組裝好一塊新的電路板並第一次接上電源時，如果看到「冒煙」了，就代表發生了嚴重的短路，測試直接宣告失敗，根本不需要進行後續的進階功能檢查。同樣地，水管工也會將煙霧灌入管道中，如果看到煙霧從縫隙漏出來，就知道哪裡破了。
* **延伸：** 後來軟體開發和資安領域借用了這個概念，用來指代「最基本、最粗略的初步運行檢查」。

### 2. Smokescreen (煙霧彈 / 障眼法)

* **中文翻譯：** 煙霧彈、障眼法、掩護行動
* **由來：** 這是標準的**軍事戰術術語**。在戰場上，軍隊會投擲煙霧彈或使用發煙車來製造大範圍的濃煙，藉此遮蔽敵方的視線，掩護己方部隊的移動、攻擊或撤退。
* **延伸：** 在資安領域，這被引申為攻擊者故意製造的大量干擾訊號（例如 DDoS 攻擊），用來掩蓋他們真實的惡意行為（例如同時在背後偷偷竊取資料）。

### 3. Smoke and Mirrors (故弄玄虛 / 虛張聲勢)

* **中文翻譯：** 故弄玄虛、障眼法、虛假表象
* **由來：** 這個詞源自於**19世紀的舞台魔術表演**。當時的魔術師經常利用舞台上的「煙霧」來模糊觀眾的視線，並巧妙放置「鏡子」來反射光線、隱藏助手或製造物體懸浮的幻覺。這句話後來被用來形容任何透過欺騙手法讓人覺得很神奇或很複雜，但實際上缺乏實質內容的事物。
* **延伸：** 在 CTF 或惡意軟體分析中，這指的是作者故意加入的大量無用程式碼（垃圾扣）或混淆技術，用來欺騙逆向工程師的眼睛。

### 4. Smoking Gun (確鑿證據 / 鐵證)

* **中文翻譯：** 確鑿證據、鐵證、決定性證據
* **由來：** 這個詞來自於**犯罪偵查的意象**。想像一個謀殺現場，如果你發現一個人手裡正拿著一把「槍管還在冒煙的槍」，那就無可辯駁地證明他剛剛開過槍。這是在亞瑟·柯南·道爾（福爾摩斯作者）等早期推理小說中經常出現的情境。
* **延伸：** 在資安鑑識（Forensics）中，找到駭客留下的關鍵日誌（Log）或作案腳本，能夠直接證明他就是兇手且還原手法，這個證據就會被稱為 Smoking Gun。

### 5. Magic Smoke (魔法煙霧)

* **中文翻譯：** 魔法煙霧
* **由來：** 這是**硬體駭客和電子工程師之間的一個經典內部笑話**。他們開玩笑地說：所有的電子元件之所以能運作，都是因為工廠在製造時，把神奇的「魔法煙霧」封裝在晶片裡面。
* **延伸：** 當你把正負極接反、給了過高的電壓，導致晶片燒毀並冒出陣陣白煙時，工程師們就會自嘲說：「糟糕，我把魔法煙霧放出來了（let the magic smoke out）。」既然魔法煙霧跑了，零件當然也就壞掉無法運作了。
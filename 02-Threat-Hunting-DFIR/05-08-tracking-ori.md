- web tracking: 在不同情境中重新識別使用者，且技術上無需使用者的期待或同意。 EX: cookie, browser fingerprinting
- 透過web tracking: 暗中記錄使用者的行為，推斷偏好、傾向，以預測或操弄使用者的行為

# (資安意識)
> 如果很疑惑這些隱私洩漏有什麼關係，或覺得隱私不重要，我不認為自己能用三言兩語說服你，...，但我很推薦Shoshana Zboff教授的"監控資本主義時代"(The Age of Surveillance Capitalism)，這本書做了許多論述

---

# 什麼是web tracking
- same-site tracking: [blog.example/A, blog.example/B] | cross-site tracking [blog.example, news.example]
- cross-site tracking 隱私疑慮 EX: 不論使用者在瀏覽哪個網站，Facebook都可以看到他的瀏覽紀錄
- stateful: 嘗試把一個identifier儲存在使用者瀏覽器 | stateless: 用瀏覽器、作業系統、硬體等各種資訊，算出identifier(browser fingerprinting)
- 網站自願/主動，安裝/植入tracker: 為了賺錢 (廣告商/廣告平台 出錢投放廣告在網站上)
- tracker蒐集:identifier, 地理位置資訊、網路流量、瀏覽過的葉面、瀏覽時間、錯誤訊息、點擊的連結、點集或檢視的廣告、廣告顯示的時間長短、系統與瀏覽器的各種資訊
- 即時競標(real-time bidding, RTB):使用者造訪網站時，SSP(Supply-Side Platform)蒐集資訊，將廣告請求交給ADX(Ad-exchange)，ADX分享給各個DSP(Demain-Side Platform)，各DSP看過使用者資訊號出價競標該欄位，網站顯示得標的DSP廣告並向之收錢。整個過程只在幾百毫秒內自動化完成，使用者毫無感覺

# web tracking用途
- 廣告投放 EX: RTB
- 聯盟行銷(Affliate marketing) or 夥伴計畫 (Referral Program): A網站讓B知道，使用者是從A過去的
- 個人化推薦：推薦文章、影片、商品、搜尋紀錄等
- 網站分析(Web Analytics): 流量來源、逗留時間、轉換率、滑鼠移動與點擊、操作習慣
- 監控 EX: NSA的PRISM


# 你在網站打google.com並送出，發生什麼事
1. 連覽器決定 a.像是網址，當網頁請求 b.不像，當搜尋請求
2. 根據preloaded HSTS決定是否用HTTPS (現在幾乎預設HTTPS)
3. Domain Name解析 (host > cache > DNS query `gethostbyname`)
4. TLS handshake建立通道 
5. HTTP request / response (方法、路徑、協定版本...)
6. 瀏覽器收到內容，解析HTML, CSS, JavaScript，建構DOM tree與render tree後，繪製到畫面上



- (dns cache 汙染檢查?)
- WebRTC (Web Real-Time Communication):允許網頁取得影音媒體、串流影音(或任意資料)的API。 EX:線上會議軟體，網站擷取了攝影機與麥克風的輸入，並將其串流出去
- firefox ublock origin
- brave: debouncing
- bounce tracking:應該只看到得瀏覽紀錄

---

# cookie
- key-value pair，儲存在瀏覽器裡面，
- same-origin policy: scheme + hostname + port | BUT domain屬性可讓不同origin共享
- first-party / third-party (bonuse: cookie syncing)
- storage: [local storage, session storage]
- IndexedDB
- cache

# cross-site tracking
- CNAME Cloaking
- Bounce Trackers
- Link Decoration


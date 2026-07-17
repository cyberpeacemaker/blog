---
title: "Project Shepherd Logo Animation Suggestions"
description: "Collects cyber-thriller logo animation prompts and SVG implementation guidance for Project Shepherd branding."
created: 2026-07-16
updated: 2026-07-16
type: reference
lang: zh
status: draft
tags: [ai, uncategorized]
---

> Related: [[06-Design-Creative]] · [[06-Design-Creative/claude-design]] · [[svg-line-drawing]]

這款 **Project Shepherd** 的 Logo 設計得非常出色！圓形徽章、幾何網格斗篷、守護者與羊群的意象，完美契合了「大隱隱於市（High-end hunters often appear as prey）」與「靜默守護者（INFJ）」的品牌設定。

為了配得上如此精緻的品牌視覺，我為你量身打造了 **3 套不同敘事風格的動畫 Prompt（提示詞）**，分別對應不同的品牌核心概念：

### 方案一：【靜默守護，雷達掃描】（The Horizon Scan）

- **品牌意象：** 呼應「在後方靜默引導，掃描地平線尋找狼隻」的守護者設定。
    
- **動畫效果：** 以牧羊人的牧杖為中心發出微光雷達波，掃描整張圖，被掃過的地方（羊群、山脈）會亮起隱藏的幾何網格與數據節點。
    

> **Image-to-Video / Runway / Luma 提示詞：**
> 
> `Animate this Project Shepherd logo with a dark, cyber-thriller atmosphere. A subtle, soft circular radar pulse originates from the shepherd's staff, sweeping outward across the emblem. As the wave passes, the geometric mesh on the shepherd's cloak and the vertices on the background mountains glow with sharp neon teal and slate blue light. The sheep at the bottom remain soft and organic, but a few hidden digital nodes pulse gently inside them, revealing their true hunter nature under the disguise. Dark navy background, volumetric lighting, slow elegant camera zoom-in, futuristic, 4K.`

### 方案二：【獵人覺醒，幾何解構】（The Hunter's Reveal）

- **品牌意象：** 呼應「披著羊皮的狼（Hunters that appear as prey）」。外表是無害的羊，內在是頂尖的威脅獵捕工具（Sheep）。
    
- **動畫效果：** 起初是一幅極簡、無害的扁平插畫，突然一聲低頻脈衝，羊群與斗篷的線條被注入能量，瞬間化為 3D 立體幾何光網，展現出強大的防禦與攻擊性。
    

> **Image-to-Video / Runway / Luma 提示詞：**
> 
> `Start with the flat vector logo of Project Shepherd against a dark navy canvas. Suddenly, a low-frequency data pulse surges through the logo. The geometric lines on the cloak and the umbrella-like dome overhead illuminate into a glowing 3D wireframe matrix. One by one, the sheep at the bottom light up from within, revealing intricate cybernetic patterns on their bodies. The animation shows the transition from passive prey to an active cyber-defense network. Luminous cyan nodes, high-contrast digital glow, ultra-precise motion, 4K rendering.`

### 方案三：【藍圖構建，秩序孕育】（The Breeding Genesis）

- **品牌意象：** 呼應「育種（Breeding）與管理（Managing）羊群」的平台設定。
    
- **動畫效果：** 像是一張正在自動繪製的網路拓撲圖。光點從牧羊人的頭部與牧杖開始，沿著網格連線，向下「孕育」出一隻隻帶有幾何骨架的數位羊。
    

> **Image-to-Video / Runway / Luma 提示詞：**
> 
> `A futuristic self-assembling blueprint animation of the Project Shepherd logo. Starting from a single glowing terminal point on the shepherd's crook, luminous light trails sequentially trace the geometric outlines of the umbrella dome, the mountain vertices, and the shepherd's cape. Next, light nodes cascade downward into the flock of sheep, rapidly "weaving" their wireframe structures as if breeding new security tools. Beautiful particle drift, soft neon glow, tech-inspired construction process, clean, elegant, smooth, 60fps.`

### 🛠️ 給前端開發者的代碼導向提示詞（GSAP / CSS / SVGator）

如果你想用程式碼在網頁上實現**最純粹、不失真的點對點 SVG 連線**，可以使用以下提示詞與 **Claude 3.5 Sonnet** 或 **GPT-4o** 協同寫 Code：

> **請將你的 SVG 原始碼與以下指令一同貼給 AI：**
> 
> `"I want to animate this Project Shepherd SVG using GSAP and CSS. The animation should represent 'order and threat hunting'.
> 
> 1. Start with an empty canvas, only showing the dark navy background (#0D1117 style).
>     
> 2. The shepherd's crook (the staff) should appear first, with its main node glowing in cyan (#00F2FE).
>     
> 3. Use DrawSVG / stroke-dashoffset to draw the umbrella-like dome and the mountain vertices sequentially, like a self-building blueprint.
>     
> 4. Once the structural lines are drawn, the geometric patterns inside the cloak (the triangle mesh) and the sheep's bodies should fade in with a subtle pulsing neon glow.
>     
> 5. Keep the animation infinitely looping with a gentle pulse on the active nodes. Write clean, modular JavaScript and inline SVG styles."`
>     

### 💡 設計師的小建議

由於你的 Logo 有很多**封閉的網格（Cloak & Mountains）**與**圓弧（Umbrella Dome & Sheep）**：

- 如果使用 **Runway/Luma**，強烈建議把你的靜態 Logo 存成高對比度的 PNG 格式（暗色背景）作為起始幀上傳，AI 對那些已經存在的幾何線條會產生非常驚豔的光影渲染。
    
- 如果使用 **SVGator/Rive**，你可以將「斗篷網格」與「山脈連線」群組命名為 `network-lines`，並單獨為它們套用 `Trim Path`（修剪路徑）效果，就能輕鬆做出極具科技感的線條延伸效果！

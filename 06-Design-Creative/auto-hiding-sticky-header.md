---
title: "Auto-Hiding Sticky Header Terminology"
description: "Defines hide-on-scroll header, smart navbar, and Headroom-style behavior for UI prompts."
created: 2026-07-25
updated: 2026-07-25
tags: [dev]
type: concept
lang: en
status: draft
---

> Related: [[06-Design-Creative]] · [[sticky-floating-tab-bar]] · [[visual-feedback]]

## 2. What to Call the Auto-Hiding Scroll Behavior

The animation where the navbar hides when scrolling down and reappears when scrolling up (or hovering) is a classic UX pattern.

### Core Terms

- **Auto-Hiding Sticky Header** (or **Auto-Hide Navbar**): The industry-standard name for a fixed top bar that hides/shows based on scroll direction.
    
- **Hide-on-Scroll-Down, Reveal-on-Scroll-Up Header**: The literal, unambiguous description favored by modern UI component libraries (like Tailwind UI, Radix, or Shadcn).
    
- **Smart Navbar** / **Dynamic Header**: General design terms for headers that react to user scroll state.
    
- **The "Headroom" Effect**: Named after **Headroom.js**, the standard JavaScript library that popularized this exact interaction pattern.
    

### Behavioral Breakdown for Prompts

To ensure an AI or developer implements it accurately, specify these three state rules:

1. **Scroll Down:** Navbar slides up out of view (`translateY(-100%)`).
    
2. **Scroll Up:** Navbar slides back down into view (`translateY(0)`).
    
3. **Hover Edge (Optional):** Mouse moving to top $0\text{--}10\text{px}$ of the viewport triggers a reveal even while scrolled down.
    

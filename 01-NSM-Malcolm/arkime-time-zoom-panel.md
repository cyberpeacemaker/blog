---
title: "Arkime Timeline Zoom Panel"
description: "Shows how to zoom Arkime's timeline by drag-selecting a time range or entering exact times."
created: 2026-07-14 17:07
updated: 2026-07-14 17:07
tags: [malcolm, nsm, arkime]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[arkime]] · [[arkime-session-splitting]]

That is completely on me—you are totally right to call that out! Single-clicking a bar on the Arkime timeline just shows the tooltip, but it doesn't actually trigger a filter change or reload the page.

To actually isolate those 32 sessions, Arkime requires a **click-and-drag** motion on the timeline graph, or a manual time adjustment. Here is how to do it correctly:

### The Real Way: Click and Drag to Zoom

1. Position your mouse cursor slightly to the **left** of that specific tall bar (near the `23:30:00` mark on the axis).
    
2. **Click and hold** your left mouse button down.
    
3. **Drag your mouse horizontally to the right**, painting a small highlight window over that specific spike bar.
    
4. Release the mouse button. The timeline will zoom in, and the session list below will automatically refresh to show only the traffic inside that highlighted slice.
    

### The Foolproof Way: Manual Time Entry

If the graph dragging feels a bit finicky, you can manually force the UI to look at that exact minute based on your tooltip:

1. Find the **Start** time field at the top left and change it to: `2024/04/25 23:36:00`
    
2. Find the **End** time field next to it and change it to: `2024/04/25 23:37:00` _(giving it a clean 1-minute window)_.
    
3. Click the **green magnifying glass (Search)** icon on the far left of the query bar to reload.


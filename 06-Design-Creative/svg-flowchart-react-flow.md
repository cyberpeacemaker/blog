---
created: 2026-06-11
tags: [design]
type: reference
lang: en
status: draft
---

Ah, I got you! No, it is definitely not ASCII art.

What you are looking at is a beautifully rendered **SVG (Scalable Vector Graphic)** or HTML canvas element generated dynamically from a structured data file—specifically a **JSON** file, just as you guessed!

Here is how this "magic" works and how you can build or show graphs just like it to others:

### 1. The Tech Behind It

This graph was created using a **"Diagram-as-Code"** or a declarative UI approach. Instead of manually drawing boxes and arrows in Photoshop or Figma, a developer wrote data (like JSON) that specifies:

* **Nodes:** The boxes (e.g., "OSINT sources", "Collector + Sanitizer").
* **Edges:** The connections/arrows between them (e.g., "1", "raw text — one-way feed").
* **Groups/Containers:** The bounding boxes (e.g., "Online Ingestion Zone").

A rendering engine (often built with JavaScript libraries like **D3.js, React Flow, or Mermaid.js**) took that JSON, applied a CSS stylesheet (handling the dark mode, rounded corners, and glowing borders), and drew it perfectly on the screen.

---

### 2. How You Can Make and Share Graphs Like This

If you want to show a graph like this to others, you don't have to code a custom JSON renderer from scratch. There are fantastic open-source tools designed exactly for this:

#### Option A: Mermaid.js (The Easiest & Most Popular)

Mermaid lets you type plain text, and it instantly turns it into a beautiful diagram. It is natively supported inside GitHub, Notion, and Discord.

To make a graph similar to yours, you would type this into a Mermaid-supported editor:

```text
graph LR
    subgraph Online Ingestion Zone
        A[OSINT sources] -->|1| B(Collector + Sanitizer)
    end
    subgraph Offline Secure Perimeter
        C[Extract IOCs + TTPs]
    end
    B -->|raw text| C

```

#### Option B: React Flow / LiteGraph.js

If you are building a web application and want users to be able to drag nodes around, zoom in/out, and have smooth interactive lines (exactly like the style in your screenshot), you would use a JavaScript library like **React Flow** or **Node-RED**. These libraries take a raw JSON object of positions and connections and render them as interactive web elements.

#### Option C: Excalidraw or tldraw

If you just want to quickly mock up this exact aesthetic manually to show a colleague, use **Excalidraw** or **tldraw**. They are free web tools that give you that clean, modern, box-and-arrow layout with customizable fonts and dark modes.

### Summary

Your image shows a **JSON file being interpreted by a custom visualization widget** (likely using React Flow or a similar SVG engine) to turn raw code into a clean, modern architecture map.

---

You are thinking of **draw.io**!

It is the undisputed classic of the "xxx.io" diagramming world.

A quick heads-up if you try to search for it: they officially rebranded and changed their domain to **diagrams.net** (mostly for security and domain stability reasons), though typing `draw.io` into your browser will still redirect you right to it.

### How it compares to Excalidraw:

* **The Style:** While Excalidraw gives you that trendy, hand-drawn, sketchy "whiteboard" look, draw.io is more traditional. It’s built for formal flowcharts, network architecture diagrams, and AWS/Google Cloud infrastructure maps with crisp, straight lines and massive shape libraries.
* **The Cost:** Just like Excalidraw, it is completely free, open-source, and you don't even need to create an account to use it. You can just save your files directly to your device, Google Drive, or GitHub.

If you want to quickly build a professional version of the diagram from your screenshot, **draw.io** is perfect for it!
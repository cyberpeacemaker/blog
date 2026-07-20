---
title: "Representing Binary Images as Text"
description: "Explains how image data can be represented with text formats such as PPM, SVG, or Base64 and why binary formats remain more efficient."
created: 2026-07-20
updated: 2026-07-20
tags: [dev]
type: reference
lang: en
status: draft
---

> Related: [[05-Software-Engineering]] · [[binary-vs-text-files]] · [[text-protocol-base64]]

You just anticipated a massive concept in computer science. **Yes, absolutely.** Every single binary file can theoretically (and practically) be rewritten or represented entirely as a text file.

In fact, your exact example of writing out pixel coordinates and RGB values (`[255, 0, 135]`) isn't just a theory—it is exactly how several real-world technologies work!

Here is how we actually do this in the real world, along with the one big catch that stops us from doing it all the time.

## Real-World Examples of "Text Images"

### 1. The PPM Image Format (Exactly your idea!)

There is a family of image formats called **Netpbm**. A `.ppm` (Portable Pixmap) file can be written in plain text. If you open a text PPM file in Notepad, it looks like this:

Plaintext

```
P3
2 2
255
255 0 0     0 255 0
0 0 255     255 255 255
```

> **How to read this:** `P3` means it's a text image. `2 2` means it is 2 pixels wide by 2 pixels high. `255` is the maximum color value. The rest are just the RGB values for the 4 pixels (Red, Green, Blue, White). Any compatible image viewer can read this text file and render it as a picture.

### 2. SVG (Scalable Vector Graphics)

Every `.svg` image you see on the web is 100% plain text. It uses XML (a text-based code) to describe shapes. Instead of listing pixels, it says things like:

`<circle cx="50" cy="50" r="40" fill="red" />`

### 3. Base64 Encoding

Have you ever seen an image embedded directly inside a website's HTML code? It looks like a massive, unreadable paragraph of random letters and numbers like `data:image/png;base64,iVBORw0KGgoAAAANSU...`.

This is called **Base64 encoding**. It is a system that takes raw binary data (like a JPEG or an MP3) and translates it entirely into a long string of standard text characters so it can be easily sent over text-only pathways like emails or HTML.

## The Catch: Why don't we always do this?

If we can turn everything into text, why bother with binary files at all? It comes down to **efficiency and file size**.

### 1. Storage Waste

Computers love numbers. In binary, the number **255** can be stored in just **1 byte** of data (`11111111`).

If you write "255" in a text file, the computer has to store the character "2", the character "5", and the character "5". That requires **3 bytes** of data. Add a comma or a space to separate it from the next pixel, and you are using 4 bytes. You just quadrupled the file size for a single color value.

### 2. Processing Speed

If an image is stored as text, your computer's graphics card can't read it directly. The CPU first has to read the text characters, parse them, convert the text "255" back into the number 255, and then send it to the screen.

Doing this for a 4K movie at 60 frames per second would cause your computer to instantly melt from the sheer math overhead. Binary files skip the middleman—the data is already in the exact numeric language the computer's hardware speaks natively.


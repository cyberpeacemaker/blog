---
created: 2026-06-08
tags: [design]
type: reference
lang: en
status: draft
---

**p5.js** is a free, open-source JavaScript library built specifically for **creative coding**. Its main goal is to make coding accessible and fun for artists, designers, educators, and beginners, allowing them to create visual art, animations, and interactive experiences directly in the web browser.

It is a modern web interpretation of **Processing** (which originally used Java).

---

## How It Works: The Core Structure

Every basic p5.js project (often called a **sketch**) relies on two fundamental functions that control how the program initializes and runs:

* **`setup()`**: Runs exactly **once** when the program starts. This is where you define the initial environment, like the size of your drawing canvas.
* **`draw()`**: Runs in a continuous loop (usually 60 times per second) directly after `setup()`. This is where animation, physics loops, and real-time user interactions happen.

---

## Hello World Example

Here is a simple interactive script. It creates a window where you can draw white circles by moving your mouse, and if you click, it clears the screen.

```javascript
function setup() {
  // Create an 800x600 pixel drawing area
  createCanvas(800, 600);
  // Give it a dark gray background
  background(50);
}

function draw() {
  // If the user clicks the mouse, clear the background back to dark gray
  if (mouseIsPressed) {
    background(50);
  }

  // Draw a white circle with a diameter of 20 pixels at the current mouse coordinates
  fill(255);
  noStroke();
  circle(mouseX, mouseY, 20);
}

```

---

## Key Features

* **2D and 3D Graphics:** Easily draw shapes (rectangles, ellipses, custom polygons) or tap into **WebGL** for 3D geometry, lighting, and textures.
* **Web Integration:** Because it runs on JavaScript, your canvas isn't isolated. You can easily interact with other HTML5 elements, text inputs, video captures (like webcams), and webcam audio.
* **Rich Add-on Libraries:** It features official extensions like `p5.sound` for audio synthesis and analysis, as well as community libraries for physics, face-tracking, and machine learning (like `ml5.js`).
* **Beginner Friendly Web Editor:** You don't need to install anything to start. You can write and run code instantly inside the [p5.js Web Editor](https://editor.p5js.org/).

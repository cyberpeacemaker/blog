---
created: 2026-06-11
tags: [design]
type: reference
lang: en
status: draft
---

**p5.js** is a powerful, beginner-friendly JavaScript library designed to make coding visual and creative arts accessible to everyone. It is essentially a modern, web-based evolution of **Processing** (which was based on Java).

Instead of dealing with complex HTML5 Canvas code, p5.js lets you create animations, interactive graphics, and games with just a few lines of code.

---

## 🎨 The Core Concept: The Canvas Life Cycle

Every basic p5.js sketch relies on two fundamental functions that control the life cycle of your program: `setup()` and `draw()`.

```
  [ setup() ]  <-- Runs ONCE at the start to initialize the canvas
       │
       ▼
  [ draw()  ]  <-- Loops continuously (usually 60 times/sec) to animate

```

### 1. `setup()`

This function runs **exactly once** when the program starts. You use it to define initial environment properties like the canvas size or to load media.

### 2. `draw()`

This function loops **continuously** from top to bottom at a default rate of 60 frames per second. This is where the magic happens—animations, physics simulations, and real-time user interactions live here.

---

## 🧱 Anatomy of a Basic Sketch

Here is what a minimal p5.js script looks like:

```javascript
function setup() {
  // Create a drawing area: width 800px, height 600px
  createCanvas(800, 600); 
}

function draw() {
  // Paint the background (0 = black, 255 = white)
  background(220); 
  
  // Draw a circle at coordinates (X: 400, Y: 300) with a diameter of 50
  circle(400, 300, 50); 
}

```

---

## 🗺️ Understanding the p5.js Coordinate System

Unlike traditional mathematics where the origin $(0,0)$ is in the center, the computer graphics coordinate system starts at the **top-left corner**.

* **X-axis:** Increases as you move to the **right**.
* **Y-axis:** Increases as you move **down**.

---

## 🚀 Key Features of p5.js

* **Built-in Shapes:** Easily render complex visuals using primitives like `rect()`, `circle()`, `triangle()`, `line()`, and custom `beginShape()` paths.
* **Easy Interactivity:** Global variables like `mouseX` and `mouseY` automatically track the user's cursor. Built-in functions like `mousePressed()` capture user inputs effortlessly.
* **Web Native:** Because it's standard JavaScript, it interacts flawlessly with other HTML elements, text inputs, webcams, sound APIs, and external data (like JSON APIs).
* **p5.sound addon:** Allows you to play audio, capture microphone input, and analyze frequencies to create audio visualizers.

---

## 🛠️ How to Start Playing with It

You don't need to install anything to get started. The easiest way to experiment is to use the official cloud editor:

👉 **[p5.js Web Editor](https://editor.p5js.org/)**

Are you looking to build something specific with p5.js, like a game, a generative art piece, or an interactive data visualization?

---

Unlike **p5.js**, which focuses on flat, 2D creative coding and digital canvas painting, **Three.js** is a powerful JavaScript library designed entirely for **3D computer graphics** right inside the web browser.

It utilizes **WebGL** (Web Graphics Library) under the hood. While pure WebGL requires hundreds of lines of complex, low-level code just to render a simple spinning cube, Three.js wraps that complexity into an intuitive, object-oriented API.

---

## 📐 The Three.js Core Concept: The 3D Theater

If p5.js is like a **2D sketchbook**, Three.js is like a **3D movie set**. To see anything on your screen, you always need four fundamental components:

```
┌─────────────────────────────────────────────────────────┐
│                       1. SCENE                          │
│                                                         │
│   [ 2. MESH ]               💡 [ 3. LIGHT ]             │
│ (Geometry + Material)        (Casts Shadows/Glow)       │
│                                                         │
│                     🎥 [ 4. CAMERA ]                     │
└─────────────────────────────────────────────────────────┘
                               │
                               ▼
                     [ 5. RENDERER ] ➔ (Displays on Canvas)

```

1. **The Scene:** The 3D world (the stage) where all your objects, lights, and cameras live.
2. **The Objects (Meshes):** The actual 3D models. A `Mesh` is made by combining a **Geometry** (the skeletal shape/polygons) and a **Material** (the skin/color/texture).
3. **The Light:** Just like the real world, without light, a 3D scene is pitch black. You need ambient, directional, or point lights to see your materials.
4. **The Camera:** The viewpoint through which the user looks into the 3D world. The most common is the `PerspectiveCamera`, which mimics how the human eye sees (objects further away look smaller).
5. **The Renderer:** The engine that takes the Scene and the Camera, calculates the mathematics of the 3D space, and draws (renders) it as a 2D image on your HTML `<canvas>` every frame.

---

## 🥊 Comparison: p5.js vs. Three.js

While both are used for creative coding in JavaScript, they are built for entirely different purposes.

| Feature | 🎨 p5.js | 🧊 Three.js |
| --- | --- | --- |
| **Primary Dimension** | **2D** (Has a basic 3D mode, but it's limited). | **3D** (Native X, Y, and Z axes). |
| **Mental Model** | **A Sketchbook.** You draw pixels/shapes on top of each other every frame. | **A Theater Set.** You place objects in a coordinate space and move a camera around them. |
| **Learning Curve** | **Low.** Designed for beginners, artists, and educators. | **Medium to High.** Requires understanding vectors, lighting, materials, and 3D math. |
| **Performance** | Great for 2D, but slows down with thousands of complex moving elements. | Highly optimized. Uses the computer’s GPU via WebGL to render millions of polygons. |
| **Best Used For** | Generative art, simple 2D games, interactive UI data visuals, UI prototypes. | Immersive 3D websites, AAA web games, architectural visualizations, product configurators. |

---

## 💻 Code Comparison: Creating a Rotating Cube

Notice how p5.js focuses on immediate action commands, while Three.js requires you to set up a world structure.

### The p5.js Approach (Using WEBGL mode)

```javascript
function setup() {
  createCanvas(400, 400, WEBGL); // Turn on basic 3D
}

function draw() {
  background(200);
  rotateX(frameCount * 0.01); // Rotate over time
  rotateY(frameCount * 0.01);
  box(100); // Draw a simple 3D box
}

```

### The Three.js Approach

```javascript
// 1. Setup Scene, Camera, and Renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 2. Create a Mesh (Shape + Material)
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube); // Add cube to the stage

camera.position.z = 5; // Move camera back so we can see the cube

// 3. Animation loop
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01; // Spin the cube
  cube.rotation.y += 0.01;
  renderer.render(scene, camera); // Render the frame
}
animate();

```

---

## 🎯 Which one should you choose?

* Choose **p5.js** if you want to quickly sketch an idea, create 2D patterns, work with audio reactive elements, or are brand new to programming visuals.
* Choose **Three.js** if you want to build an interactive 3D portfolio, render 3D models exported from Blender, or build a complex 3D web experience.

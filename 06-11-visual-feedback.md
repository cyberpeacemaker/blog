You are absolutely on the right track! There is definitely a specific set of terms we use in design and development for exactly what you are describing.

Depending on whether you are talking to a designer or a programmer, the exact word changes slightly, but the most common terms are **Micro-interactions**, **Visual Feedback**, and **State Changes**.

Here is a breakdown of what these terms mean and how they fit your examples:

---

### 1. Micro-interactions

This is the most popular term in modern UI/UX (User Interface/User Experience) design. A micro-interaction is a small, subtle visual effect that accomplishes a single task and acknowledges a user's action.

* **Why it fits:** It's exactly what you described—making the interface feel alive and responsive.
* **Example:** A "Like" button that bursts with confetti when clicked, or a loading spinner that turns into a checkmark.

### 2. Visual Feedback (or Interaction Feedback)

This is the broader UX concept. It refers to the system "talking back" to the user to confirm that an action has been registered. Without visual feedback, a user might click a button, see nothing change, and wonder, *"Did that work, or is it frozen?"*

* **Why it fits:** It explicitly tells the user, "Yes, you are interacting with me right now."
* **Example:** A button darkening slightly when you hover over it so you know it's clickable.

### 3. State Changes (or Component States)

If you are coding the element (using CSS or a design tool like Figma), you are managing **States**. Elements change their visual properties based on user behavior.

* **`:hover` (Hover State):** The element changes when the mouse pointer rolls over it.
* **`:active` (Click/Pressed State):** The element changes the exact moment it is being clicked or tapped.
* **`Playing / Active / Selected` (Toggle State):** The element changes to show it is currently "on" or in use (like a play button turning into a pause button).

---

> **Summary:** If you're talking about the *concept* of making things feel responsive, call it **Visual Feedback**. If you're talking about the *cool little animations* themselves, call them **Micro-interactions**.

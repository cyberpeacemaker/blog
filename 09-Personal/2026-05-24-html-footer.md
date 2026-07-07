---
created: 2026-05-24
tags: [personal]
type: reference
lang: en
status: draft
---

Ah, yes! That is a fantastic UI pattern. It's often called a **"smart footer"** or **"auto-hiding footer."** It gives you the best of both worlds: you get maximum screen real estate for the data table when scrolling down, but the moment you need the footer and scroll up, it slides right back into view.

Because CSS alone cannot detect the *direction* you are scrolling, implementing this effect requires a combination of **CSS (for the smooth sliding animation)** and **JavaScript (to detect whether you are scrolling up or down)**.

Here is how you can build that exact effect:

### Step 1: The CSS (The Slide Animation)

First, you set the footer to a fixed position at the bottom, but add a `transition` so it animates smoothly. You also create a `.hidden` class that pushes the footer down entirely out of view using `transform: translateY()`.

```css
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background-color: var(--color-gray-light);
  /* The magic that makes it slide smoothly: */
  transition: transform 0.3s ease-in-out; 
}

/* When this class is added, the footer slides down off the screen */
.footer.footer-hidden {
  transform: translateY(100%); 
}

```

### Step 2: The JavaScript (The Scroll Detector)

Next, you need a small script that keeps track of your scroll position. It compares where you are *now* to where you were a millisecond ago.

* If the new position is higher than the old position = **Scrolling Down** (Add the hidden class).
* If the new position is lower than the old position = **Scrolling Up** (Remove the hidden class).

```javascript
let lastScrollTop = 0;
// Note: Depending on Arkime's layout, the scrolling element might be a specific 
// div (like the table container) rather than the 'window' itself.
const scrollContainer = window; 
const footer = document.querySelector('.footer');

scrollContainer.addEventListener('scroll', function() {
  let currentScroll = scrollContainer.scrollY || scrollContainer.scrollTop;

  if (currentScroll > lastScrollTop) {
    // We are scrolling DOWN - Hide the footer
    footer.classList.add('footer-hidden');
  } else {
    // We are scrolling UP - Show the footer
    footer.classList.remove('footer-hidden');
  }
  
  // Update the last position for the next calculation
  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; 
}, false);

```

### A Quick Note on Arkime's Architecture

Looking at the `data-v-...` attributes in your screenshot, Arkime is built using Vue.js. If you are modifying the actual source code of the application, you would ideally implement this scroll logic inside the Vue component's lifecycle hooks (like `mounted()` and `beforeDestroy()`) rather than just dropping vanilla JavaScript into the DOM.

---

Are you looking to implement this by editing Arkime's actual source code, or are you trying to apply a quick UI patch using a browser extension like Stylish or Tampermonkey?
---
created: 2026-06-10
tags: [software]
type: reference
lang: en
status: draft
---

## 1. Decoupling (Separation of Concerns)

Decoupling is the practice of ensuring that different parts of a software system can operate independently. If Component A breaks or needs a total rewrite, Component B should remain completely unfazed.

* **The Coding Mindset:** Writing a single script where database queries, business logic, and UI rendering are all mashed together (spaghetti code).
* **The Engineering Mindset:** Creating clean interfaces or APIs between modules. You use techniques like **Dependency Injection** and **Event-Driven Architecture** so components talk to each other without knowing the intimate details of how they are implemented.
* **Why it matters:** It makes your codebase modular. You can swap out a Postgres database for a MongoDB database, or change your frontend framework, without tearing down the entire backend.

---

## 2. State Management

State is the memory of your application—it’s the data that represents the current condition of the system at any given moment. Managing it poorly leads to "impossible" bugs where the UI shows one thing, the database says another, and the server thinks a third.

* **The Coding Mindset:** Storing variables haphazardly across various files, modifying them globally, and hoping they stay synchronized.
* **The Engineering Mindset:** Designing a single, predictable source of truth. Engineers treat state changes as explicit, traceable events (think Redux in frontend, or event sourcing in backend systems). They favor **immutability** (creating a new state rather than mutating the old one) to prevent side effects.
* **Why it matters:** It eliminates "Heisenbugs"—those annoying glitches that disappear the moment you try to debug them. Predictable state makes applications testable and reproducible.

---

## 3. Concurrency Control

In the modern world, software rarely executes linearly on a single thread. Multiple users, background jobs, and multi-core processors mean things are happening at the exact same time. Concurrency control is about managing this traffic safely.

* **The Coding Mindset:** Assuming code runs sequentially from top to bottom, ignoring the fact that two users might click "Buy last item" at the exact same millisecond.
* **The Engineering Mindset:** Anticipating race conditions and deadlocks. Engineers use tools like **locks, semaphores, mutexes,** or **optimistic/pessimistic locking** in databases to ensure data integrity when multiple processes collide.
* **Why it matters:** It prevents catastrophic data corruption—like double-spending in a banking app or overbooking a flight.

---

## 4. Boundary Handling

Software does not exist in a vacuum. It interacts with users, third-party APIs, file systems, and unreliable networks. Boundary handling is the art of defining where your system ends and the chaotic outside world begins, and building a "fortress" around your logic.

* **The Coding Mindset:** Assuming APIs are always online, networks never drop, and users only type exactly what they are supposed to in form fields.
* **The Engineering Mindset:** Embracing **Defensive Programming**. You rigorously validate inputs at the gate, handle edge cases, and implement **graceful degradation** (e.g., using circuit breakers, retries, and fallbacks when an external API fails).
* **Why it matters:** It prevents a failure in a minor third-party service from cascading and bringing down your entire application. If the external email service goes down, your app should queue the emails for later, not crash on the user.

---

### Summary: The Ultimate Shift

Ultimately, the software engineering mindset accepts a fundamental truth: **software will change, and software will fail.** Instead of fighting change and fearing failure, an engineer uses decoupling to make change easy, and uses state management, concurrency control, and boundary handling to make failure manageable.

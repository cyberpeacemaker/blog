---
created: 2026-05-25
tags: [dev]
type: reference
lang: en
status: draft
---

## 1. Boundary Tests (Boundary Value Analysis)

**Boundary testing** is a systematic technique where you test the exact limits of an input range. The logic is simple: errors are much more likely to occur at the "edges" of an accepted range (the boundaries) than in the middle.

### How to Use Boundary Tests

To use this technique, you identify a valid range of inputs and then test three specific points for every boundary:

1. **Just below the boundary** (Invalid)
2. **Exactly on the boundary** (Valid)
3. **Just above the boundary** (Valid or Invalid, depending on the rule)

### Examples of Boundary Tests

**Scenario A: Age Verification**
A website requires users to be between **18 and 65 years old** to register.

* **Lower Boundary Tests:**
* `17` (Just below - should fail)
* `18` (Exactly on - should pass)
* `19` (Just above - should pass)


* **Upper Boundary Tests:**
* `64` (Just below - should pass)
* `65` (Exactly on - should pass)
* `66` (Just above - should fail)



**Scenario B: Password Length**
A password must be between **8 and 16 characters**.

* **Tests:** A 7-character password (fail), an 8-character password (pass), a 16-character password (pass), and a 17-character password (fail).

---

## 2. Edge Cases

An **edge case** is a problem or situation that occurs only at extreme operating parameters. While boundary tests look at strict numerical or logical limits of a *single* input, edge cases often involve unusual scenarios, extreme conditions, or the unexpected intersection of rules.

### How to Use Edge Cases

Finding edge cases requires you to step outside the "happy path" (the way a normal user would use the app flawlessly) and think creatively. You have to ask yourself: *"What is the most bizarre, extreme, or unlikely thing a user or the system could do right now?"* ### Examples of Edge Cases

**Scenario A: E-commerce Cart**
A normal user adds 1 to 5 items to their cart and checks out.

* **Edge Case:** What happens if a user tries to add `99,999` of the same item to their cart? Does the total price exceed the maximum number the database can handle? Does the UI break because the number is too wide for the screen?

**Scenario B: Date and Time**
A system calculates interest rates daily.

* **Edge Case:** How does the system behave on **February 29th** during a leap year? What happens if the user performs a transaction exactly at the moment daylight saving time begins or ends, causing the clock to skip ahead or fall back an hour?

**Scenario C: User Inputs**
An app asks for a user's first and last name.

* **Edge Case:** What if the user's name is just one letter long (e.g., "O")? What if they have a hyphenated name that is 150 characters long? What if their name includes special characters, emojis, or is written in Arabic (which reads right-to-left)?

---

## Summary Comparison

| Feature | Boundary Tests | Edge Cases |
| --- | --- | --- |
| **Focus** | Strict limits of expected input ranges. | Extreme, unusual, or unexpected scenarios. |
| **Approach** | Mathematical and highly systematic. | Creative, exploratory, and contextual. |
| **Complexity** | Usually involves testing a single variable at its limit. | Often involves pushing multiple variables to their extremes simultaneously. |
| **Example** | Testing a 256-character string in a 255-character limit field. | Using an app while moving through a tunnel and losing Wi-Fi exactly as payment processes. |

By combining both systematic boundary testing and creative edge case exploration, you can catch the vast majority of bugs before they ever reach your users.
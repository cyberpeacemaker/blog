---
title: "Linter Basics"
description: "Explains what linters do, when to use them, and how they fit IDE and command-line development workflows."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [dev]
---

> Related: [[MOC - Dev Environment]] · [[github-actions-sensitive-patterns]] · [[dry-run-pytest]]
Imagine having a ruthlessly organized, slightly pedantic friend sitting next to you while you code, gently tapping your shoulder every time you typo a variable name, forget a closing bracket, or write code that works but looks like a crime scene.

That is a **linter**.

Technically speaking, a linter is a static code analysis tool used to flag programming errors, bugs, stylistic errors, and suspicious constructs. It examines your code _without_ actually running it.

## When to Use a Linter

Honestly? **All the time.** If you are writing code, a linter should be active. But it becomes completely non-negotiable in these scenarios:

- **Working in Teams:** A linter prevents "tabs vs. spaces" formatting wars. It forces everyone to write code that looks like it was written by a single person.
    
- **Catching Silly Bugs Early:** It catches typos, undeclared variables, or unreachable code _before_ you even try to execute it, saving you frustrating debugging sessions.
    
- **Learning a New Language:** Linters often enforce best practices, making them great guardrails when you're still figuring out the idiomatic way to write a language.
    
- **CI/CD Pipelines:** Automation workflows usually run a linter to block messy or broken code from ever being merged into the main repository.
    

## How to Use a Linter

Using a linter typically involves three main steps:

### 1. Installation

You install the linter via your language's package manager.

- _JavaScript/TypeScript:_ **ESLint** is the undisputed king.
    
- _Python:_ **Ruff** (blazing fast and very popular) or **Flake8**.
    
- _Go:_ **golangci-lint**.
    

### 2. Configuration

You tell the linter your preferences using a configuration file (like `.eslintrc.json` or `pyproject.toml`). This is where you decide things like, "Are semicolons mandatory?" or "What is the maximum line length?"

### 3. Execution

You can use a linter in two main ways:

- **In your IDE (Recommended):** Install an extension (like the ESLint extension in VS Code). It underlines errors in red or yellow while you type, just like a spellchecker.
    
- **Via Command Line:** Run a command to scan your whole project before committing code (e.g., `npx eslint .`). Many linters also have a `--fix` flag that automatically cleans up formatting mistakes for you.
    

## A Quick Example (JavaScript)

Let's look at a piece of JavaScript code that technically runs, but is full of bad practices.

### The "Bad" Code:

JavaScript

```
function calculateTotal(price) {
  var discount = 10
  
  if (price > 100) {
      const bonus = 5;
    return price - discount;
  }

  return price
  console.log("Done!");
}
```

### What the Linter Flags:

If you ran ESLint against this, it would throw a fit and point out:

1. **`var discount`**: It will recommend using `let` or `const` instead of the outdated `var`.
    
2. **`const bonus`**: It will flag this as an _unused variable_ (it's declared but never used).
    
3. **Indentation**: It will complain that the indentation inside the `if` statement is inconsistent.
    
4. **`console.log("Done!")`**: It will flag this as _unreachable code_ because it happens after the `return` statement.
    
5. **Semicolons**: Depending on your settings, it might complain about the missing semicolons on lines 2 and 9.
    

### The Clean, Linted Code:

After fixing the issues (many of which the linter can auto-fix), your code looks like this:

JavaScript

```
function calculateTotal(price) {
  const discount = 10;
  
  if (price > 100) {
    return price - discount;
  }

  return price;
}
```

It's cleaner, safer, and much easier for the next developer to read.

Which programming language are you currently working in? I can recommend the best linting setup for your specific workflow.


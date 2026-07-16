---
title: "Folder by Type vs Folder by Feature"
description: "Explains the tradeoff between category-based and feature-based project structures and the hybrid shared-folder approach."
created: 2026-07-16
updated: 2026-07-16
type: concept
lang: en
status: draft
tags: [dev]
---

> Related: [[05-Software-Engineering]] · [[project-reorganization-challenge]] · [[software-concept]]

You have nailed it. You are describing one of the most debated, classic trade-offs in software architecture.

In the industry, this is known as **Folder-by-Type (Category)** vs. **Folder-by-Feature (Functionality)**.

Your intuition about the pros and cons of both is 100% correct. Let’s break down exactly why you feel this way and how modern development solves this tension.

## 1. Folder-by-Type ("Category")

This is where you organize files by what they _are_ technically (e.g., putting all components in one folder, all API calls in another, and all styles in a third).

Plaintext

```
src/
├── components/
│   ├── UserProfile.js
│   └── ProductCard.js
├── api/
│   ├── userApi.js
│   └── productApi.js
└── styles/
    ├── userProfile.css
    └── productCard.css
```

- **Your diagnosis:** _"Well organized, but hard to get files when working on a task."_
    
- **Why you are right:** To change just the "User Profile" feature, you have to open three different folders scattered across your project. This is called **poor colocation**. It causes high cognitive load because you are constantly jumping around your folder tree just to complete one simple task.
    

## 2. Folder-by-Feature ("Functionality")

This is where you group files by the real-world feature they belong to. Everything needed for that feature lives in one place.

Plaintext

```
src/
├── features/
│   ├── user-profile/
│   │   ├── UserProfile.js
│   │   ├── userApi.js
│   │   └── userProfile.css
│   └── product-catalog/
│       ├── ProductCard.js
│       ├── productApi.js
│       └── productCard.css
```

- **Your diagnosis:** _"Good for quick access... but might forget later on when the job is done."_
    
- **Why you are right:** When you group by feature, you get incredibly fast workflow speeds while working on that feature. But once you have 30 feature folders, you run into the **"out of sight, out of mind"** problem. You might forget that `user-profile` has a great helper function, and you end up accidentally writing the exact same code inside `product-catalog`.
    

## The Modern Solution: The Hybrid Approach

To solve this, modern software engineering uses a hybrid structure. You organize **by feature first**, but you keep a **shared category folder** for global pieces.

Here is how you balance it:

1. **If it belongs to only one feature:** Put it inside that feature's folder (Folder-by-Feature).
    
2. **If it is used by two or more features:** Move it to a global `components/`, `utils/`, or `shared/` folder at the root (Folder-by-Type).
    

Plaintext

```
src/
├── components/           <-- "Category" (Only for truly shared, generic UI like Buttons/Inputs)
│   ├── Button.js
│   └── Card.js
├── features/             <-- "Functionality" (Where 90% of your daily work happens)
│   ├── auth/
│   │   ├── LoginCard.js
│   │   └── authService.js
│   └── dashboard/
│       ├── DashboardStats.js
│       └── dashboardApi.js
```

### Why this works:

- When working on "Auth," everything you need is in the `auth` folder. No tab-hopping.
    
- When you need a generic button, you look in the shared `components` folder. This prevents you from "forgetting" and duplicating code.
    

> **The Organization Rule of Thumb:**
> 
> **Colocate** (keep together) files that change together. If modifying a UI file always requires you to modify a specific API file, they should probably live in the same folder.

How large is the project you are working on right now? If it is a smaller project, a simple Category-based structure might still be easiest, but if it is growing, it might be time to transition to a Feature-based one.

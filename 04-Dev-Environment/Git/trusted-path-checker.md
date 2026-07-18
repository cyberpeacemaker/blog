---
title: "Trusted Path Checker Concepts"
description: "Distinguishes Git safe.directory checks, OIDC trusted publishers, CodeQL path checks, and path-checker actions."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[github-actions-sensitive-patterns]] · [[canary-pattern]]
While there isn't a single, official tool by GitHub explicitly branded as the **"trusted-path checker,"** that phrase is commonly used to describe several crucial security and automation concepts in the Git and GitHub ecosystem.

Depending on where you encountered the term, you are likely looking at one of the following security mechanisms:

### 1. Git's `safe.directory` Check (The "Trusted Repo Path" Guardian)

- **The Context:** Running Git commands locally or in CI/CD environments.
    
- **How it works:** To address major security vulnerabilities where malicious actors could exploit shared multi-user environments, Git introduced a built-in "trusted path" checker. Before executing commands, Git checks if the repository directory is owned by the current user.
    
- **The Guardrail:** If Git detects that the repository's path is owned by someone else, it halts and throws a `fatal: unsafe repository` error. To bypass this, you must explicitly tell Git to trust that specific path by adding it to your configuration:
    
    Bash
    
    ```
    git config --global --add safe.directory /path/to/repo
    ```
    

### 2. GitHub Actions "Trusted Publishers" (OIDC)

- **The Context:** Securely publishing packages (like NPM, PyPI, or NuGet) directly from GitHub workflows.
    
- **How it works:** Instead of storing highly vulnerable, long-lived API keys or passwords in your GitHub Secrets, you establish a "trusted path" of authority between your GitHub repository and the external package registry using **OpenID Connect (OIDC)**.
    
- **The Guardrail:** The package registry acts as the checker. When your workflow runs, the registry inspects a cryptographic token issued by GitHub. It checks the _trusted path of execution_—meaning it verifies that the repository owner, repo name, and workflow file match your pre-configured settings before allowing the release to publish.
    

### 3. CodeQL Path Injection & Trust Boundary Scanners

- **The Context:** GitHub Advanced Security (GHAS) static analysis.
    
- **How it works:** If you are auditing code, GitHub's analysis engine (**CodeQL**) includes query checkers that inspect how your application handles file paths.
    
- **The Guardrail:**
    
    - **Path Injection Checkers:** CodeQL scans your codebase to ensure that user-controlled input cannot escape "trusted directories" (preventing directory traversal attacks).
        
    - **Trust Boundary Violation Checkers:** These flag instances where untrusted, unvalidated input crosses over into your system's trusted execution space.
        

### 4. Third-Party "Path Checker" Actions

- **The Context:** CI/CD file sanity checking.
    
- **How it works:** There are several third-party GitHub Actions in the Marketplace (like `arnesor/path-checker`).
    
- **The Guardrail:** These act as automated linters that scan your repository's file tree to ensure that file names or directory paths do not contain spaces, non-ASCII characters, or excessive character lengths that could break builds on different operating systems (like Windows vs. Linux).
    

Which of these scenarios matches the specific problem you are trying to solve or learn more about?


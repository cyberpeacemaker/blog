---
created: 2026-08-02 15:08
updated: 2026-08-02 15:08
tags: []
type: reference
lang: en
status: draft
---
### What is this?

You are using the **GitHub CLI (`gh`)** to log into your GitHub account so you can clone the `nagameTW/otex-claw` repository.

Two things went wrong:

1. **No local browser bridge:** Your Linux terminal couldn't open a browser automatically because system helpers like `wslview` or `xdg-open` aren't installed.
    
2. **Rate limited (`slow_down`):** Because the auto-launch failed and the session timed out, GitHub temporarily blocked the login attempt due to too many requests.
    

### What URL should you enter?

The URL to open in your browser is:

> **`[https://github.com/login/device](https://github.com/login/device)`**

_(Note: **Do not** use code `CFB0-0918` anymore. Because of the `slow_down` error, that code has expired.)_

### How to Fix It (Step-by-Step)

#### Option 1: Browser Device Flow (Easiest)

1. **Wait 2–3 minutes** for GitHub's rate limit (`slow_down`) to clear.
    
2. In your terminal, run the login command again:
    
    Bash
    
    ```
    gh auth login
    ```
    
3. Select the options as you did before:
    
    - **Account:** `GitHub.com`
        
    - **Protocol:** `HTTPS`
        
    - **Authenticate Git:** `Yes`
        
    - **Method:** `Login with a web browser`
        
4. Copy the **NEW code** shown on screen.
    
5. Open **`[https://github.com/login/device](https://github.com/login/device)`** in your standard web browser (Chrome, Edge, Firefox, etc.).
    
6. Enter the **NEW code** and click **Authorize**.
    
7. Go back to your terminal, press **Enter**, and you will be logged in!
    

#### Option 2: Use a Personal Access Token (Bypasses browser limits)

If you keep getting browser or rate limit errors, you can log in directly with a Personal Access Token:

1. Go to GitHub in your browser: **Settings** $\rightarrow$ **Developer Settings** $\rightarrow$ **Personal Access Tokens** $\rightarrow$ **Tokens (classic)**.
    
2. Click **Generate new token (classic)**, check the **`repo`** scope, and copy the generated token string.
    
3. In your terminal, run:
    
    Bash
    
    ```
    gh auth login
    ```
    
4. Choose **GitHub.com** $\rightarrow$ **HTTPS** $\rightarrow$ **Paste an authentication token**.
    
5. Paste your token and hit Enter.


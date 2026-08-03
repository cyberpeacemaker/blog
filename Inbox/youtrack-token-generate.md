---
created: 2026-08-03 09:08
updated: 2026-08-03 09:08
tags: []
type: reference
lang: en
status: draft
---
## How to Generate or Manage Your YouTrack Token

You can create and manage your permanent authentication tokens directly inside your YouTrack profile.

> **Crucial Note:** YouTrack **only shows full token values once** at the time of creation. For security reasons, existing full tokens cannot be viewed again after you close the creation window. If you lost an existing token, you'll need to delete it and create a new one.

### Steps to Generate a New Token

1. **Open Profile Settings:** Log into YouTrack, click your **Profile Avatar** in the top-right corner, and select **Profile**.
    
2. **Navigate to Security:** Click on the **Account Security** tab.
    
3. **Create Token:** Scroll down to the **Tokens** section and click the **New token...** button.
    
4. **Define Name & Scopes:**
    
    - Enter a descriptive **Name** (e.g., _Power BI Integration_ or _GitHub Automation_).
        
    - Select the necessary **Scope(s)** (e.g., `YouTrack` for general issues/projects, `YouTrack Administration` for administrative API calls).
        
5. **Generate:** Click **Create token**.
    
6. **Save Immediately:** Copy the generated token string using the **Copy token** button. Store it in a secure location or password manager right away, as it won't be shown again.
    

### Replacing a Lost Token

If you are looking for a token you created previously:

1. Return to **Profile** > **Account Security**.
    
2. Locate the token under the **Tokens** list.
    
3. Click **Delete** (or the trash icon) to revoke the old token.
    
4. Follow the creation steps above to generate a fresh token.


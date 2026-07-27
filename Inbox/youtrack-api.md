---
created: 2026-07-27 15:07
updated: 2026-07-27 15:07
tags: []
type: reference
lang: en
status: draft
---
Short answer: **yes, JetBrains YouTrack has a comprehensive, built-in REST API.**

The API is enabled by default across all YouTrack installations (both Cloud and Server/Standalone).

### Key Capabilities

Using the YouTrack REST API, you can programmatically manage virtually every part of the platform:

- **Issues:** Create, update, delete, search, link, or transition issues.
    
- **Projects & Fields:** Manage projects, custom fields, bundles, and custom field values.
    
- **Agile Boards & Workflows:** Retrieve and update agile board configurations, time tracking, and work logs.
    
- **Users & Roles:** Access user accounts, groups, project teams, organizations, and permissions directly.
    
- **Data Migration:** Programmatically import issues and attachments from third-party tools.
    

### Core Details

- **Data Format:** Requests and responses use standard JSON (`application/json`).
    
- **Authentication:** Authenticate using a **Permanent Token** passed via the `Authorization: Bearer <token>` header. You can generate personal access tokens directly from your YouTrack account settings.
    
- **Base Endpoint:** REST calls typically target `https://<your-youtrack-url>/api/...`.
    

### Getting Started

1. **API Reference:** Check the official [JetBrains Developer Portal YouTrack REST API Reference](https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html) for exact schemas and endpoints.
    
2. **Postman Collection:** JetBrains maintains an official Postman collection for the YouTrack REST API to help you test requests quickly.
    
3. **Libraries:** Official or community client wrappers exist for languages like Python (`youtrack` package) and .NET (`YouTrackSharp`) to simplify API integration.


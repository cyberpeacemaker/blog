---
created: 2026-07-09 15:07
updated: 2026-07-09 15:07
tags: []
type: reference
lang: en
status: draft
---
That purple highlight you see in **image_66239b.png** is part of a fantastic browser feature called **Scroll to Text Fragment** (often just called "Link to Highlight").

The great news is that you don't need any special developer tools to do this—you can easily create these links yourself in seconds!

## The Easy Way: How to Share a Highlighted Link

If you are using a modern browser like **Google Chrome**, **Microsoft Edge**, or **Opera**, the feature is built right into your mouse click.

1. **Select the text:** Go to any webpage and use your cursor to highlight the specific sentence or paragraph you want to share.
    
2. **Right-click:** Right-click directly on top of that highlighted text.
    
3. **Copy the link:** Click on **"Copy link to highlight"** from the menu that pops up.
    

That's it! A customized link is now copied to your clipboard. You can paste it into an email, a chat, or a document to share with anyone else.

## How the Magic Works (Under the Hood)

If you paste that copied link somewhere to look at it, you will notice that the browser automatically tacked on a special snippet of code to the very end of the regular URL.

The structure looks like this:

> `[https://example.com/page/#:~:text=Start%20Of%20Text,End%20Of%20Text](https://example.com/page/#:~:text=Start%20Of%20Text,End%20Of%20Text)`

- **`#`**: This tells the browser to look for a specific fragment on the page.
    
- **`:~:text=`**: This is the magic directive. It tells the browser: _"Scroll down until you find these exact words, and highlight them in purple/yellow."_
    

When your friend clicks the link, their browser reads that snippet, jumps straight to the correct section of the page, and creates the exact visual highlight you see in **image_66239b.png**.

### A Quick Compatibility Note

This feature is natively supported by almost all major modern browsers (Chrome, Edge, Safari, and Opera). If you send the link to someone using an older browser that doesn't support it, the link will still work perfectly fine—it will just open the webpage normally at the very top without scrolling or highlighting.


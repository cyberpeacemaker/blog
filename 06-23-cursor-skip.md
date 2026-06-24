No, Cursor does not automatically skip questions or autonomously submit prompts on your behalf just because it has been left idle for a long time.

The AI chat and composer features in Cursor are designed to wait indefinitely for your input. If you see the AI’s internal reasoning (the "Thought" block) concluding that you "skipped the questions," it is likely due to one of the following reasons rather than a time-out:

* **Accidental Blank Submission:** When you returned to the computer, you might have accidentally hit `Enter` or clicked submit without typing anything. The AI received an empty prompt, noticed you didn't answer its previous questions, and reasoned, *"The user skipped the questions, so I'll proceed with the default."*
* **Generic Reply:** If you came back and typed something simple like "continue," "go ahead," or "next," the AI interpreted that as you explicitly choosing not to answer the specific questions it asked previously.
* **Context Window Shift:** If you made code edits in the background or performed other actions that synced to the AI's context before your next prompt, the AI might have re-evaluated the state of the workspace and inferred that it should just move forward.
* **Session Refresh/Glitch:** Leaving a session idle for a long period can sometimes cause a websocket disconnection. Upon reconnecting, if the UI sends a silent refresh ping that the LLM accidentally interprets as a blank user turn, it might trigger a response where the AI assumes you just want to move on.

**What you can do:**
If the AI is going down the wrong path because it skipped those questions, you can simply stop its generation (or delete the message) and type: *"Wait, I didn't skip the questions. Here are my answers:..."* The AI will easily course-correct and use your input.
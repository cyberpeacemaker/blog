A **dry run** is a rehearsal or a trial run of a process to make sure everything works correctly before you do it for real. Think of it as a safety net—you go through all the motions, but without actually risking any real-world consequences, spending money, or breaking anything.

Depending on the context, a dry run means slightly different things:

### 1. In Programming & Tech

For developers, a dry run (often called **desk checking**) means mentally or manually stepping through code line by line to see what it does before actually running it on a computer.

* **How it works:** You write down your variables on a piece of paper and update their values as you simulate how the computer would execute the logic.
* **Why do it:** It’s an amazing way to catch logic flaws, infinite loops, or "off-by-one" errors before deployment.

### 2. In DevOps & System Administration

Many software tools and command-line interfaces have a literal `--dry-run` flag.

* **Example:** If you are syncing a massive database or deleting old files, running `command --dry-run` will output exactly what the system *would* have done, without actually modifying or deleting a single file.

### 3. In Business & Presentations

Before a major product launch, a massive keynote presentation, or a theater performance, the team will do a dry run.

* This involves running through the entire event from start to finish to test the timing, the tech (microphones, slides), and the transitions so there are no surprises on the big day.

---

> **The Golden Rule of a Dry Run:** It should mimic the real event as closely as possible, but with the "safety switch" turned on.

---

In `pytest` (the popular Python testing framework), a **dry run** means checking which tests exist and making sure your test configuration is correct—**without actually running the test code.** This is incredibly useful if you have hundreds of tests and don't want to wait for them to execute just to see if a specific test is being picked up, or if you want to verify that your test markers are working.

Here is how you do it:

### The Magic Flag: `--collect-only`

To perform a dry run in `pytest`, you use the `--collect-only` flag (or its shorter alias, `-co`).

When you run this command in your terminal:

```bash
pytest --collect-only

```

`pytest` will look through your directories, find all the test files and functions, and print them out in a neat tree structure.

### Why use a dry run in pytest?

* **Verifying Selectors:** If you are trying to run a specific subset of tests using keyword expressions (the `-k` flag), you can combine it with a dry run to make sure you're targeting the right ones.
```bash
# "Show me all tests with 'login' in the name, but don't run them"
pytest -k "login" --collect-only

```


* **Checking Custom Markers:** If you use custom markers to categorize tests (like `@pytest.mark.slow`), you can verify which tests are marked without running them.
```bash
# "Show me all tests marked as slow"
pytest -m slow --collect-only

```


* **Debugging Test Discovery:** If you just wrote a new test and `pytest` isn't finding it, a dry run helps you see if it's a configuration issue (like an incorrect file naming format) without wasting time running the rest of your test suite.

---

> 💡 **Bonus Tip:** If you want a super clean, minimal list of just the test names without the extra formatting, you can use `pytest --q --collect-only`.

Are you trying to debug why a specific test isn't being found, or are you looking to filter a large test suite right now?
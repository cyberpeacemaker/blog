---
created: 2026-07-21 14:07
updated: 2026-07-21 14:07
tags: []
type: reference
lang: en
status: draft
---
In short: **Usually no, but sometimes you must.**

In YAML, strings are unquoted by default. However, double quotes are necessary—or at least strongly recommended—in specific situations.

## 1. When You MUST Use Double Quotes (`"..."`)

### A. When using escape sequences

Double quotes are the **only** quoting style in YAML that processes escape sequences like `\n` (newline), `\t` (tab), or unicode characters.

YAML

```
# Evaluates as two lines
message: "Hello\nWorld" 

# Literal text "\n" (does NOT create a newline)
plain: Hello\nWorld
single: 'Hello\nWorld'
```

### B. When dealing with leading or trailing whitespace

If your string starts or ends with spaces that you want to preserve:

YAML

```
padded_text: "  has spaces on both sides  "
```

## 2. When You SHOULD Quote (Single or Double)

You should quote strings when they could be misinterpreted by the YAML parser.

### A. To prevent automatic type conversion

YAML automatically converts certain unquoted words into booleans, numbers, or `null`.

YAML

```
# Needs quotes, otherwise parsed as booleans/numbers/null:
country_code: "NO"       # Without quotes, older YAML parsers treat 'NO' as false
is_string: "true"        # Parsed as string "true", not boolean true
version: "1.0"           # Parsed as string "1.0", not float 1
zip_code: "01234"        # Preserves leading zero (otherwise parsed as octal/integer)
null_string: "null"      # Parsed as string "null", not null value
```

### B. When strings contain YAML special characters

If your string contains characters that have structural meaning in YAML—such as `:`, `#`, `{`, `}`, `[`, `]`, `,`, `&`, `*`, `?`, `|`, `>`, `-`, `%`, or `@`—you must quote it.

YAML

```
# Special characters require quotes:
title: "User Profile: Edit"     # ':' followed by space confuses the parser
hashtag: "#golang"              # '#' starts a comment
mapping: "{ key: value }"       # '{}' looks like inline JSON
```

## Quick Comparison

|**Style**|**Example**|**Behavior**|**Best Used For**|
|---|---|---|---|
|**Unquoted**|`greeting: Hello World`|Plain text|Simple, clean text without special characters.|
|**Single Quotes**|`path: 'C:\Users\Name'`|Exact literal (treats `\` as a regular character)|Regex, file paths, or text with literal backslashes.|
|**Double Quotes**|`msg: "Line 1\nLine 2"`|Evaluates escape characters (`\n`, `\t`)|Anything with escape characters or special YAML syntax.|

> **Rule of Thumb:**
> 
> Keep strings **unquoted by default** for clean readability. Switch to **single quotes** for exact literal strings with special characters, and save **double quotes** for when you specifically need escape sequences like `\n`.


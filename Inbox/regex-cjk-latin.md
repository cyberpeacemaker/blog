---
created: 2026-07-19 16:07
updated: 2026-07-19 16:07
tags: []
type: reference
lang: en
status: draft
---
When dealing with **CJK (Chinese, Japanese, Korean) <-> Latin** regex, the most common goal is to find the boundary between these character sets to insert a space (often called "Pangu spacing" or "autospacing") to improve typography.

Because different programming languages handle Unicode differently, here are the two best ways to write this regex: using **Modern Unicode Properties** (cleaner) and **Traditional Hex Ranges** (more compatible).

## 1. The Modern Approach (Unicode Properties)

If your environment supports Unicode property escapes (JavaScript ES2018+, Python `regex` module, PCRE, Ruby, .NET), you can target the scripts directly.

- **CJK Definition:** Includes Han Ideographs (Chinese/Japanese), Hiragana/Katakana (Japanese), and Hangul (Korean).
    
- **Latin Definition:** Standard alphanumeric (`[a-zA-Z0-9]`).
    

### CJK followed by Latin

- **Match:** `(\p{Unified_Ideograph}|\p{Script=Hiragana}|\p{Script=Katakana}|\p{Script=Hangul})([a-zA-Z0-9])`
    
- **Replace with:** `$1 $2` (Inserts a space between them)
    

### Latin followed by CJK

- **Match:** `([a-zA-Z0-9])(\p{Unified_Ideograph}|\p{Script=Hiragana}|\p{Script=Katakana}|\p{Script=Hangul})`
    
- **Replace with:** `$1 $2`
    

## 2. The Traditional Approach (Hex Ranges)

If you are working in an older environment or just want maximum compatibility, you can use explicit Unicode hex ranges.

- **CJK Range:** `[\u4e00-\u9fa5\u3040-\u30ff\uac00-\ud7af]`
    
- **Latin Range:** `[a-zA-Z0-9]`
    

### CJK followed by Latin

- **Match:** `([\u4e00-\u9fa5\u3040-\u30ff\uac00-\ud7af])([a-zA-Z0-9])`
    
- **Replace:** `$1 $2`
    

### Latin followed by CJK

- **Match:** `([a-zA-Z0-9])([\u4e00-\u9fa5\u3040-\u30ff\uac00-\ud7af])`
    
- **Replace:** `$1 $2`
    

> **Note:** If you _only_ care about Chinese characters and English, you can shorten the CJK range to just `[\u4e00-\u9fa5]`.

## Code Implementation Examples

### JavaScript (ES2018+)

Using the `u` (unicode) and `g` (global) flags:

JavaScript

```
function panguSpace(text) {
  return text
    // CJK followed by Latin
    .replace(/(\p{Unified_Ideograph}|\p{Script=Hiragana}|\p{Script=Katakana}|\p{Script=Hangul})([a-zA-Z0-9])/gu, '$1 $2')
    // Latin followed by CJK
    .replace(/([a-zA-Z0-9])(\p{Unified_Ideograph}|\p{Script=Hiragana}|\p{Script=Katakana}|\p{Script=Hangul})/gu, '$1 $2');
}

console.log(panguSpace("提示:请使用Chrome浏览器")); 
// Output: "提示: 请使用 Chrome 浏览器"
```

### Python

Python's built-in `re` module doesn't fully support `\p{...}` properties natively without the external `regex` package, so the hex range method is safest:

Python

```
import re

def pangu_space(text):
    cjk_range = r'[\u4e00-\u9fa5\u3040-\u30ff\uac00-\ud7af]'
    latin_range = r'[a-zA-Z0-9]'
    
    # CJK -> Latin
    text = re.sub(f'({cjk_range})({latin_range})', r'\1 \2', text)
    # Latin -> CJK
    text = re.sub(f'({latin_range})({cjk_range})', r'\1 \2', text)
    return text

print(pangu_space("提示:请使用Chrome浏览器"))
# Output: "提示: 请使用 Chrome 浏览器"
```

Which programming language or text editor are you planning to use this regex in, and are you trying to do a search-and-replace or just validation?


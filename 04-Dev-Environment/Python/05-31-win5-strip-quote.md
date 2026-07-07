This is famously one of the most frustrating quirks in PowerShell 5.1. The parser aggressively strips quotes before handing the string over to a native executable (like `kubectl`, `aws`, `cmd`, or `exe` files), effectively destroying things like inline JSON.

Here are the three approaches that actually work to bypass or satisfy the PS 5.1 parser, depending on whether you need to inject variables.

### 1. The `\"` Escape (Best for strings with variables)

Native executables on Windows rely on the C/C++ runtime to parse arguments, which expects quotes to be escaped with a backslash (`\"`). In PS 5.1, you have to satisfy *both* PowerShell and the native executable.

If you are using **single quotes** (no PowerShell variables):

```powershell
# The backslash is ignored by PS, but read by the native executable
mycmd.exe '{\"key\": \"value\"}'

```

If you are using **double quotes** (to inject PowerShell variables), you must escape the quote for PowerShell (```) AND for the native executable (`\`):

```powershell
$val = "hello"
# `\" escapes the quote for PowerShell AND sends \" to the executable
mycmd.exe "{\`"key\`": \`"$val\`"}"

```

### 2. The Stop-Parsing Symbol `--%` (Best for static strings)

If you do not need to evaluate any PowerShell variables in the arguments, you can use the `--%` operator. This tells PowerShell to stop parsing the rest of the line and pass it exactly as written directly to the executable.

```powershell
# Everything after --% is passed exactly as is.
mycmd.exe --% {"key": "value"}

```

*Note: You cannot use PowerShell variables (like `$val`) after `--%`. However, you CAN use traditional Windows environment variables (like `%USERNAME%`).*

### 3. Wrapping in an Array (Best for complex, multi-argument commands)

Sometimes the cleanest way to prevent PS 5.1 from mangling your arguments is to define them explicitly in an array, combining the backslash escape method. When you splat or pass an array to a native command, it handles the spaces and boundaries slightly better.

```powershell
$args = @(
    "--config",
    '{\"key\": \"value\"}',
    "--force"
)

mycmd.exe $args

```

### Why does this happen?

PowerShell 5.1 tries to rebuild the argument string before calling the `CreateProcess` API, and it deliberately drops quotes it assumes are just wrapping strings.

*(Note: If you ever have the luxury of migrating to PowerShell 7+, this was finally fixed via the `$PSNativeCommandArgumentPassing = 'Standard'` preference, which completely stops the quote-stripping behavior.)*

---

To check the current setting for native command argument passing, you just need to type the variable name directly into your PowerShell console and press Enter:

```powershell
$PSNativeCommandArgumentPassing

```

### What to expect from the output:

* **`Standard`**: This is the behavior you want for predictable quote parsing. It passes the arguments to the native executable exactly as you'd expect, without stripping the internal quotes. (This is the default on Linux and macOS in PS 7.3+).
* **`Windows`**: This is the default on Windows in PS 7.3+. It behaves mostly like `Standard`, but uses the `Legacy` behavior *specifically* for a few known problematic executables (`cmd.exe`, `find.exe`, `cscript.exe`, `wscript.exe`, `sqlcmd.exe`, `bat` files, etc.) so that old scripts don't break.
* **`Legacy`**: This is the classic PowerShell 5.1 behavior (the one that aggressively strips quotes and breaks inline JSON).
* *(Nothing/Blank)*: If the command returns absolutely nothing, you are either running an older version of PowerShell (like 5.1) where this feature doesn't exist, or you are on PowerShell 7.2 where the feature existed but had to be explicitly enabled.

### Checking your PowerShell version

Because this feature is highly version-dependent, it is a good idea to verify exactly what version of PowerShell you are running. You can check it with:

```powershell
$PSVersionTable.PSVersion

```

* **If you are on PS 5.1:** `$PSNativeCommandArgumentPassing` doesn't exist. You have to use the escape tricks (`\`"`) or `--%` mentioned previously.
* **If you are on PS 7.3 or higher:** You can change the behavior globally in your current session or profile by simply running:
```powershell
$PSNativeCommandArgumentPassing = 'Standard'

```
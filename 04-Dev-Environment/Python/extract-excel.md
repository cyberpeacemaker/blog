---
title: "Extract Excel Data"
description: "Compares Python, CLI, Node.js, and manual workflows for converting Excel files into CSV, JSON, or Markdown."
created: 2026-07-17
updated: 2026-07-17
type: howto
lang: en
status: draft
tags: [dev, python]
---

> Related: [[MOC - Dev Environment]] · [[python-venv]] · [[requirements]]
Extracting data from Excel and converting it into machine-friendly formats (like CSV, JSON, or Markdown) is a very common task. Depending on your workflow, you can do this using **code**, **command-line tools**, or **built-in Excel features**.

Here is a breakdown of the most efficient ways to get this done.

## Method 1: The Developer Gold Standard (Python)

Python is the absolute best tool for this because of the **Pandas** library. It can read Excel files and write to almost any format in just a few lines of code.

### 1. Install the required libraries

Bash

```
pip install pandas openpyxl tabulate
```

_(Note: `openpyxl` helps read `.xlsx` files, and `tabulate` is required if you want to export to Markdown)._

### 2. The Conversion Script

Here is a single script that reads an Excel file and exports it to **CSV**, **JSON**, and **Markdown**:

Python

```
import pandas as pd

# Load the Excel file (defaults to the first sheet)
# You can specify a sheet name: sheet_name='Sheet1'
df = pd.read_excel('input_file.xlsx')

# 1. Convert to CSV (Standard comma-separated)
df.to_csv('output.csv', index=False)

# 2. Convert to JSON (Orient='records' gives a clean array of developer-friendly objects)
df.to_json('output.json', orient='records', indent=4)

# 3. Convert to Markdown (Perfect for documentation or GitHub)
# Requires the 'tabulate' library installed
markdown_table = df.to_markdown(index=False)
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(markdown_table)

print("Extraction complete! Saved to CSV, JSON, and Markdown.")
```

## Method 2: The Quick CLI Way (No Coding Required)

If you don't want to write a script and just need a quick terminal command, use **`csvkit`** or **`xlsx2csv`**.

### Using `xlsx2csv` (Fast & Lightweight)

1. Install it:
    
    Bash
    
    ```
    pip install xlsx2csv
    ```
    
2. Convert in your terminal:
    
    Bash
    
    ```
    xlsx2csv input_file.xlsx output.csv
    ```
    

### Using `csvkit` (Swiss Army Knife for Data)

1. Install it:
    
    Bash
    
    ```
    pip install csvkit
    ```
    
2. Convert Excel directly to CSV:
    
    Bash
    
    ```
    in2csv input_file.xlsx > output.csv
    ```
    

## Method 3: Node.js (For JavaScript Environments)

If you are building a web app or working in a Node environment, **SheetJS (xlsx)** is the industry standard.

1. Install SheetJS:
    
    Bash
    
    ```
    npm install xlsx
    ```
    
2. Read and convert to JSON:
    
    JavaScript
    
    ```
    const XLSX = require('xlsx');
    
    // Read the workbook
    const workbook = XLSX.readFile('input_file.xlsx');
    
    // Get the first sheet name
    const sheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[sheetName];
    
    // Convert to JSON
    const jsonData = XLSX.utils.sheet_to_json(worksheet);
    
    // Print or save the JSON
    console.log(JSON.stringify(jsonData, null, 2));
    ```
    

## Method 4: Built-in Excel Features (Manual)

If you only have one or two files to convert manually:

- **For CSV:** Go to `File` > `Save As` and select **CSV (Comma delimited) (*.csv)**.
    
- **For JSON/Markdown:** Excel doesn't do this natively. However, you can copy the cells, paste them into an online converter (like [TableConvert](https://tableconvert.com/)), and instantly get JSON, Markdown, or XML.
    

### ⚠️ Common Excel Pitfalls to Watch Out For

- **Merged Cells:** These will usually result in `NaN` or `null` values in your output for all but the top-left cell. Unmerge them before exporting if possible.
    
- **Formulas vs. Values:** Libraries like Pandas read the _evaluated values_ by default. If you need the raw formulas (e.g., `=SUM(A1:A10)`), you will need specific configurations in libraries like `openpyxl`.
    
- **Multiple Sheets:** Remember that CSV files can only support _one sheet per file_. If your Excel workbook has multiple tabs, you will need to loop through them and export a separate CSV for each sheet.
    

Which environment (Python, Node, Command Line, etc.) are you planning to run this in, and how large/complex are the Excel files you're working with?


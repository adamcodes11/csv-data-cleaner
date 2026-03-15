# 🧹 CSV Data Cleaner

A Python script that automatically detects and fixes common data quality issues in CSV files.

## What it fixes
- Removes duplicate rows
- Fills in missing first names
- Normalizes capitalization (names, departments)
- Flags and replaces invalid emails
- Removes unrealistic age values
- Standardizes date formats to YYYY-MM-DD
## Requirements
```
Python 3.8+ installed
```

## Usage
```bash
python csv_cleaner.py
```
Generates a `dirty_data.csv` demo file, cleans it, and saves `clean_data.csv` with a full report.

## Example Output
```
Cleaning complete!
  Original rows:      55
  Cleaned rows:       50
  Duplicates removed: 5
  Invalid emails:     8
  Dates normalized:   6
```

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
Commands:
pip3 / python3     - Mac/Linux
pip  / pythin      - Windows

# 1. Download repo
git clone https://github.com/adamdev/book-price-scraper.git
cd book-price-scraper
# or simply download zip file

# 2. Create venv (optional but recommended)
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Uruchom
python price_scraper.py
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

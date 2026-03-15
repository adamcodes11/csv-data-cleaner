import csv
import os
import random
from datetime import datetime, timedelta

def generate_dirty_csv(filename="dirty_data.csv"):
    headers = ["id", "first_name", "last_name", "email", "phone", "age", "salary", "department", "join_date"]
    departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]
    first_names = ["Alice", "Bob", "Carol", "David", "Emma", "Frank", "Grace", "Henry"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]

    rows = []
    for i in range(1, 51):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        date = (datetime(2018, 1, 1) + timedelta(days=random.randint(0, 1800))).strftime("%Y-%m-%d")
        row = {
            "id": i,
            "first_name": name if random.random() > 0.1 else "",
            "last_name": surname if random.random() > 0.05 else surname.upper(),
            "email": f"{name.lower()}.{surname.lower()}@example.com" if random.random() > 0.15 else "INVALID_EMAIL",
            "phone": f"+48 {random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}" if random.random() > 0.2 else "N/A",
            "age": random.randint(20, 65) if random.random() > 0.1 else random.randint(200, 999),
            "salary": f"{random.randint(3000, 15000)}.00" if random.random() > 0.1 else "",
            "department": random.choice(departments) if random.random() > 0.1 else random.choice(departments).lower(),
            "join_date": date if random.random() > 0.1 else date.replace("-", "/")
        }
        rows.append(row)

    # Add duplicates
    rows.extend(random.choices(rows[:10], k=5))

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated dirty CSV: {filename} ({len(rows)} rows)")
    return filename

def clean_csv(input_file, output_file="clean_data.csv"):
    issues = {"missing": 0, "invalid_email": 0, "invalid_age": 0, "duplicates": 0,
              "normalized_dept": 0, "normalized_date": 0, "fixed_name": 0}

    with open(input_file, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    cleaned = []
    seen_ids = set()

    for row in rows:
        # Remove duplicates
        if row["id"] in seen_ids:
            issues["duplicates"] += 1
            continue
        seen_ids.add(row["id"])

        # Fix missing first name
        if not row["first_name"].strip():
            row["first_name"] = "Unknown"
            issues["missing"] += 1

        # Normalize last name to title case
        if row["last_name"] == row["last_name"].upper() and len(row["last_name"]) > 1:
            row["last_name"] = row["last_name"].title()
            issues["fixed_name"] += 1

        # Validate email
        if "@" not in row["email"] or "." not in row["email"]:
            row["email"] = "invalid@unknown.com"
            issues["invalid_email"] += 1

        # Fix age
        try:
            age = int(row["age"])
            if age < 16 or age > 100:
                row["age"] = ""
                issues["invalid_age"] += 1
        except ValueError:
            row["age"] = ""

        # Normalize department capitalization
        if row["department"] != row["department"].title():
            row["department"] = row["department"].title()
            issues["normalized_dept"] += 1

        # Normalize date format to YYYY-MM-DD
        if "/" in row["join_date"]:
            row["join_date"] = row["join_date"].replace("/", "-")
            issues["normalized_date"] += 1

        cleaned.append(row)

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(cleaned)

    print(f"\nCleaning complete!")
    print(f"  Original rows:     {len(rows)}")
    print(f"  Cleaned rows:      {len(cleaned)}")
    print(f"  Duplicates removed:{issues['duplicates']}")
    print(f"  Missing names fixed:{issues['missing']}")
    print(f"  Invalid emails:    {issues['invalid_email']}")
    print(f"  Invalid ages:      {issues['invalid_age']}")
    print(f"  Dept normalized:   {issues['normalized_dept']}")
    print(f"  Dates normalized:  {issues['normalized_date']}")
    print(f"\nSaved to {output_file}")

def main():
    print("=== CSV Cleaner Demo ===\n")
    dirty = generate_dirty_csv()
    clean_csv(dirty)

main()

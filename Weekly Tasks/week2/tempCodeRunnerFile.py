import pandas as pd

# 1. Load the messy CSV file
df = pd.read_csv("messy_data7.csv")

print("Original rows:", len(df))

# 2. Create summary variables
original_rows = len(df)
missing_before = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

# 3. Fix column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 4. Remove duplicate rows
df = df.drop_duplicates()

# 5. Handle missing numeric values
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# 6. Handle missing text values
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# 7. Fix text formatting
for column in text_columns:
    df[column] = df[column].astype(str).str.strip().str.title()

# 8. Save cleaned CSV
df.to_csv("cleaned_data.csv", index=False)

# 9. Create summary
missing_after = df.isnull().sum().sum()
cleaned_rows = len(df)

report = f"""
DATA CLEANING SUMMARY
---------------------

Original rows: {original_rows}
Rows after cleaning: {cleaned_rows}

Duplicate rows removed: {duplicates}

Missing values before cleaning: {missing_before}
Missing values after cleaning: {missing_after}

Cleaning performed:
- Removed extra spaces from column names
- Converted column names to lowercase
- Replaced spaces with underscores
- Removed duplicate rows
- Filled numeric missing values with mean
- Filled text missing values with "Unknown"
- Removed extra spaces from text
- Converted text to title case

Output file:
cleaned_data.csv
"""

# 10. Save report
with open("cleaning_report.txt", "w") as file:
    file.write(report)

print("\nCleaning completed!")
print("Cleaned file: cleaned_data.csv")
print("Report file: cleaning_report.txt")
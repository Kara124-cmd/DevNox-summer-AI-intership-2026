
# TASK 1
# Read and write both CSV and JSON files; parse and filter specific records.

# read filter and save csv file
import pandas as pd
df = pd.read_csv('student.csv')
print(df)

#filter tha student  marks
marks = df[df['Marks'] > 80]
print('\nHighest marks')
print(marks)

# save to the csv file
marks.to_csv('highest_marks.csv', index = False)

# read filter and save json file
import pandas as pd 

df = pd.read_json('student.json')
print(df)

city = df[df['City'] == 'Lahore']
print('\nYour city ')
print(city)

city.to_json('your_city.json', orient = 'records')




# TASK 2:
# create arrays, index/slice them, and compute basic statistics without loops.

import numpy as np

array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# index
print('indexing')
print(array[0])
print(array[4])
print(array[-2])

#slicing
print('\nSlicing')
print(array[1:])
print(array[:6])
print(array[2:7])
print(array[::2])

# bASIC STATISTICS 
print('\nStatistics')
print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.min(array))
print(np.max(array))
print(np.std(array))
print(np.var(array))




# TASK 3:
# load a dataset, filter rows, group by a column, and handle missing values.
import pandas as pd

df = pd.read_csv('studentRecord.csv')
print(df)

# missing values
print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['City'] = df['City'].fillna(df['City'].mode()[0])
print(df)

# filter rows
high_marks = df[df['Marks'] > 80]
print('\nthe highest marks are : ')
print(high_marks)

select_city = df[df['City'] == 'Islamabad']
print('\n Your selected city is : ')
print(select_city)

# groupby columns
grouped_columns = df.groupby('City')['Marks'].mean()
print(grouped_columns)





# TASK 4
# Merge two small datasets (dictionaries or DataFrames) and produce a summary.
import pandas as pd
# Dataset 1
students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Usman", "Ahmed", "Sara"],
    "City": ["Lahore", "Islamabad", "Karachi", "Peshawar"]
})
# Dataset 2
marks = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [85, 90, 75, 88],
    "Grade": ["A", "A+", "B", "A"]
})
# Merge both datasets using ID
merged = pd.merge(students, marks, on="ID")
print("Merged Dataset:")
print(merged)

# Summary
print("\nSummary:")
print("Total Students:", len(merged))
print("Average Marks:", merged["Marks"].mean())
print("Highest Marks:", merged["Marks"].max())
print("Lowest Marks:", merged["Marks"].min())






# TASK 5
# Write a custom exception class and use the logging module instead of print() for errors.
import logging
# Setup logging
logging.basicConfig(level=logging.ERROR)
# Custom exception
class AgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("You are eligible")
except AgeError as e:
    logging.error(e)
except ValueError:
    logging.error("Please enter a number")




# TASK 6:
# Practice Git: create a repo, make a branch, commit changes, push, and open a pull request.







# MINI PROJECT :  TASK 7
# Data Cleaning Tool — take a messy CSV (duplicates, missing values, inconsistent formats) and output a cleaned CSV plus a short summary report of what was fixed.
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
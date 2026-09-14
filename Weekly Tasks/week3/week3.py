

# TASK 1
# Plot a bar chart, a line chart, and a pie chart from a sample dataset.

#bar Chat
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 140, 200]

plt.bar(months, sales)
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


#Line char
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 140, 200]

plt.plot(months, sales, marker = 'o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# Pie chart
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 140, 200]

plt.pie(sales, labels=months, autopct = '%1.1f%%')
plt.title("Monthly Sales - Line Chart")
plt.show()





# TASK 2
# Create a correlation heatmap for a numeric dataset using Seaborn.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample numeric dataset
data = {
    "Age": [20, 22, 25, 28, 30, 35],
    "Study_Hours": [2, 3, 4, 5, 6, 7],
    "Marks": [55, 60, 65, 72, 80, 88],
    "Attendance": [70, 75, 78, 82, 90, 95]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df.corr()

# Create heatmap
sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Correlation Heatmap")
plt.show()










# TASK 3
# Fetch data from a public REST API using requests and save the result to a file.
from fastapi import FastAPI
import requests
import json

app = FastAPI()

# Fetch users from REST API
@app.get("/users")
def get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        # Save data to JSON file
        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

        return data

    return {"error": "Failed to fetch data"}





# TASK 4
# Parse a JSON API response and turn part of it into a chart.
import requests
import matplotlib.pyplot as plt

# Get JSON data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Convert JSON response to Python data
data = response.json()

# Get names and IDs
names = []
ids = []

for user in data:
    names.append(user["name"])
    ids.append(user["id"])

# Create bar chart
plt.bar(names, ids)

plt.xlabel("Users")
plt.ylabel("User ID")
plt.title("User IDs from JSON API")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()







# TASK 5
# Build 2, 3 reusable plotting functions (a tiny personal visualization module).
import matplotlib.pyplot as plt
# 1. Bar chart function
def create_bar_chart(x, y, title):
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.show()
# 2. Line chart function
def create_line_chart(x, y, title):
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# 3. Pie chart function
def create_pie_chart(labels, values, title):
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title(title)
    plt.show()

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]
# Use the functions
create_bar_chart(months, sales, "Monthly Sales")

create_line_chart(months, sales, "Sales Trend")

create_pie_chart(months, sales, "Sales Distribution")





# TASK 6
# Push a small script to GitHub with at least 3 meaningful, separate commits










# TASK 7
# EDA Mini-Dashboard Script — load a public dataset (or fetched API data), auto-generate 4 charts, and write 3–4 sentences of insight based on what the charts show.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#    Load public dataset
df = sns.load_dataset("penguins")

print("Dataset loaded successfully!")
print(df.head())

#  Basic cleaning
# Remove rows with missing values
df = df.dropna()
print("\nRows after cleaning:", len(df))

#   Chart 1 - Histogram
plt.figure()
plt.hist(df["body_mass_g"], bins=15)
plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Number of Penguins")
plt.show()

#    Chart 2 - Scatter Plot
plt.figure()
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

#    Chart 3 - Bar Chart
average_mass = df.groupby("species")["body_mass_g"].mean()
plt.figure()
average_mass.plot(kind="bar")

plt.title("Average Body Mass by Species")
plt.xlabel("Species")
plt.ylabel("Average Body Mass (g)")
plt.xticks(rotation=0)
plt.show()

#   Chart 4 - Correlation Heatmap
numeric_data = df.select_dtypes(include="number")
correlation = numeric_data.corr()

plt.figure()
sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


    # Generate insights
largest_species = (df.groupby("species")["body_mass_g"].mean().idxmax())
largest_mass = (df.groupby("species")["body_mass_g"].mean().max())
correlation_value = correlation.loc["flipper_length_mm", "body_mass_g"]

print("\nEDA INSIGHTS")
print("------------")

print(f"The dataset contains {len(df)} penguins after removing missing values.")
print(
    f"{largest_species} has the highest average body mass, "
    f"at approximately {largest_mass:.0f} grams."
)
print(
    f"The scatter plot shows that penguins with longer flippers "
    f"generally have higher body mass."
)
print(
    f"The correlation between flipper length and body mass is "
    f"{correlation_value:.2f}, indicating a positive relationship."
)
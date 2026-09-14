
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
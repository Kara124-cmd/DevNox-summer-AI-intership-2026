

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Create a simple dataset
data = {
    "Study_Hours": [1, 1.5, 2, 2.5, 3, 8, 8.5, 9, 9.5, 10, 20],
    "Marks": [30, 32, 35, 38, 40, 80, 82, 85, 88, 90, 50]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Select features
X = df[["Study_Hours", "Marks"]]

# Create DBSCAN model
dbscan = DBSCAN(eps=5, min_samples=2)

# Train the model and create clusters
df["Cluster"] = dbscan.fit_predict(X)

# Print dataset
print(df)

# Plot the clusters
plt.scatter(df["Study_Hours"], df["Marks"], c=df["Cluster"], s=100)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("DBSCAN Clustering")

plt.show()










# dbscan clustering on builtin dataset

from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

# Get the data
X = iris.data

# Scale the data
X_scaled = StandardScaler().fit_transform(X)

# Create DBSCAN model
dbscan = DBSCAN(eps=0.8, min_samples=5)
# Create clusters
labels = dbscan.fit_predict(X_scaled)

# Print cluster labels
print(labels)

# Plot first two features
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("DBSCAN Clustering on Iris Dataset")

plt.show()







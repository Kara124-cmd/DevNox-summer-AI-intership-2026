
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#  Create a small student dataset
data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12"],
    "Study_Hours": [1, 1.5, 2, 2.5, 4, 4.5, 5, 5.5, 7, 7.5, 8, 8.5],
    "Quiz_Score": [40, 45, 50, 55, 65, 68, 72, 75, 85, 88, 92, 95]
}
df = pd.DataFrame(data)
print("Student Dataset:")
print(df)

#  Select features
X = df[["Study_Hours", "Quiz_Score"]]

#  Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df["Cluster"] = kmeans.fit_predict(X)

#  Show clustered students
print("\nStudents with Clusters:")
print(df)

#  Print cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Visualize the clusters
plt.figure(figsize=(8, 6))

for cluster in range(3):
    cluster_data = df[df["Cluster"] == cluster]
    plt.scatter(cluster_data["Study_Hours"], cluster_data["Quiz_Score"], label=f"Cluster {cluster}")

# Plot cluster centers
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker="X", s=200, label="Centroids")
plt.xlabel("Study Hours per Day")
plt.ylabel("Quiz Score")
plt.title("Student Segmentation Using K-Means")
plt.legend()
plt.show()

#  Create cluster profiles
print("\nCluster Profiles:")

for cluster in range(3):
    cluster_data = df[df["Cluster"] == cluster]
    avg_hours = cluster_data["Study_Hours"].mean()
    avg_score = cluster_data["Quiz_Score"].mean()
    print(
        f"Cluster {cluster}: "
        f"Average Study Hours = {avg_hours:.1f}, "
        f"Average Quiz Score = {avg_score:.1f}"
    )
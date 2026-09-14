

# TASK 1
# Implement K-Nearest Neighbors from scratch on a small 2D dataset.

import math
data = [[1, 2, "A"], [2, 3, "A"], [3, 3, "A"], [6, 5, "B"], [7, 7, "B"], [8, 6, "B"]]

#  Euclidean distance function
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
#  KNN prediction function
def knn_predict(data, new_point, k=3):
    distances = []
    # Calculate distance from new point
    # to every point in the dataset
    for point in data:
        distance = euclidean_distance(point, new_point)
        distances.append(
            (distance, point[2])
        )
    # Sort distances from smallest to largest
    distances.sort()
    # Select the k nearest neighbors
    neighbors = distances[:k]
    # Count votes
    votes = {}

    for distance, label in neighbors:
        if label not in votes:
            votes[label] = 0
        votes[label] += 1

    # Find class with maximum votes
    predicted_class = max(votes, key=votes.get)

    return predicted_class, neighbors
# Predict a new point
new_point = [4, 4]
prediction, neighbors = knn_predict(data, new_point, k=3)

print("New Point:", new_point)

print("\nNearest Neighbors:")
for distance, label in neighbors:
    print("Distance:", round(distance, 2), "Class:", label)

print("\nPredicted Class:", prediction)











# TASK 2:
# Train a Decision Tree classifier and visualize the resulting tree.

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


#  Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Create the Decision Tree model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
#  Train the model
model.fit(X_train, y_train)
#  Make predictions
y_pred = model.predict(X_test)

#  Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#  Visualize the Decision Tree
plt.figure(figsize=(15, 8))
plot_tree(model, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True)
plt.title("Decision Tree Classifier")
plt.show()









# TASK 3:
# Train a Random Forest and compare its accuracy and feature importance to the single Decision Tree.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#  Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

feature_names = iris.feature_names

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Train Decision Tree
decision_tree = DecisionTreeClassifier(random_state=42)

decision_tree.fit(X_train, y_train)
dt_predictions = decision_tree.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_predictions)
#  Train Random Forest
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

random_forest.fit(X_train, y_train)
rf_predictions = random_forest.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

# 5. Compare Accuracy
print("Decision Tree Accuracy:", dt_accuracy)
print("Random Forest Accuracy:", rf_accuracy)

# Get Feature Importance
dt_importance = decision_tree.feature_importances_
rf_importance = random_forest.feature_importances_

# Create comparison table
comparison = pd.DataFrame({"Feature": feature_names, "Decision Tree Importance": dt_importance, "Random Forest Importance": rf_importance})
print("\nFeature Importance Comparison:")
print(comparison)

#  Plot Accuracy Comparison
models = ["Decision Tree", "Random Forest"]
accuracy_values = [dt_accuracy, rf_accuracy]

plt.figure(figsize=(8, 5))

plt.bar(models, accuracy_values)
plt.title("Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0, 1.1)

plt.show()

#  Plot Feature Importance
x = range(len(feature_names))

plt.figure(figsize=(10, 5))

plt.bar(x, dt_importance, width=0.4, label="Decision Tree")
plt.bar( [i + 0.4 for i in x], rf_importance, width=0.4, label="Random Forest")
plt.xticks([i + 0.2 for i in x], feature_names, rotation=20)
plt.ylabel("Importance")
plt.title("Feature Importance Comparison")
plt.legend()
plt.show()














# TASK 4:
# Implement K-Means from scratch and use the elbow method to pick a good value of k.

import numpy as np
import matplotlib.pyplot as plt

#  Create a small 2D dataset
data = np.array([[1, 2], [1.5, 1.8], [2, 2.5], [2, 1], [8, 8], [8.5, 8], [9, 8.5], [8, 9], [4, 7], [4.5, 7.5],
    [5, 7], [5, 8]])

#  K-Means from scratch
def kmeans(data, k, max_iterations=100):
    # Randomly select k points as centroids
    np.random.seed(42)
    random_indexes = np.random.choice( len(data), k, replace=False)
    centroids = data[random_indexes].astype(float)

    for _ in range(max_iterations):
        # Store cluster for every point
        clusters = []
        # Assign each point to nearest centroid
        for point in data:
            distances = []
            for centroid in centroids:
                distance = np.linalg.norm(point - centroid)
                distances.append(distance)
            nearest_cluster = np.argmin(distances)
            clusters.append(nearest_cluster)
        clusters = np.array(clusters)

        # Calculate new centroids
        new_centroids = []

        for i in range(k):
            cluster_points = data[clusters == i]
            if len(cluster_points) > 0:
                new_centroid = np.mean(cluster_points, axis=0 )
            else:
                new_centroid = centroids[i]
            new_centroids.append(new_centroid)
        new_centroids = np.array(new_centroids)

        # Stop if centroids do not change
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    # Calculate inertia
    inertia = 0
    for i, point in enumerate(data):
        centroid = centroids[clusters[i]]
        inertia += np.sum((point - centroid) ** 2)
    return clusters, centroids, inertia

#  Elbow Method
inertia_values = []
k_values = range(1, 7)

for k in k_values:
    clusters, centroids, inertia = kmeans(data, k)
    inertia_values.append(inertia)
# Plot Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for K-Means")
plt.show()

#  Choose K = 3
k = 3
clusters, centroids, inertia = kmeans(data, k)

#  Plot Final Clusters
plt.figure(figsize=(8, 6))
for i in range(k):
    cluster_points = data[clusters == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i + 1}")

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker="X", s=200, label="Centroids")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-Means Clustering from Scratch")
plt.legend()
plt.show()












# TASK 5:
# Apply DBSCAN to the same data and compare its clusters against K-Means

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

#  Same 2D dataset
data = np.array([[1, 2], [1.5, 1.8], [2, 2.5], [2, 1], [8, 8], [8.5, 8], [9, 8.5], [8, 9],
 [4, 7], [4.5, 7.5], [5, 7], [5, 8]])

#  K-Means from Scratch
def kmeans(data, k, max_iterations=100):
    np.random.seed(42)
    # Select random centroids
    random_indexes = np.random.choice( len(data), k, replace=False )

    centroids = data[random_indexes].astype(float)

    for _ in range(max_iterations):
        # Assign each point to nearest centroid
        clusters = []

        for point in data:
            distances = []
            for centroid in centroids:
                distance = np.linalg.norm(point - centroid)
                distances.append(distance)
            nearest_cluster = np.argmin(distances)
            clusters.append(nearest_cluster)

        clusters = np.array(clusters)
        # Calculate new centroids
        new_centroids = []

        for i in range(k):
            cluster_points = data[clusters == i]
            if len(cluster_points) > 0:
                new_centroid = np.mean(
                    cluster_points,
                    axis=0
                )
            else:
                new_centroid = centroids[i]
            new_centroids.append(new_centroid)
        new_centroids = np.array(new_centroids)

        # Stop when centroids stop changing
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids
# Run K-Means with K = 3
kmeans_clusters, centroids = kmeans(data, k=3)

# Apply DBSCAN
dbscan = DBSCAN(eps=2, min_samples=2)
dbscan_clusters = dbscan.fit_predict(data)

print("K-Means Clusters:")
print(kmeans_clusters)
print("\nDBSCAN Clusters:")
print(dbscan_clusters)










# TASK 6:
# Run k-fold cross-validation on one of this week's models and report the average score.

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

#  Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

#  Apply 5-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=5)
#  Print scores and average score
print("Score for each fold:")
print(scores)
print("\nAverage Accuracy:")
print(scores.mean())












                                    # Mini Project

# Mini Segmentation Project — cluster a small dataset (e.g., study habits or quiz scores) into meaningful groups and write a one-line profile for each cluster.

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
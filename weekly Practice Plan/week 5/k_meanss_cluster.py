

'''
K-means
K-means is an unsupervised learning method for clustering data points. The algorithm iteratively divides data points into K clusters by minimizing the variance in each cluster.'''

# simple k-means clustring program of studetn study hours and marks
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create a simple dataset
data = {
    "Study_Hours": [1, 2, 2, 3, 8, 9, 10, 11],
    "Marks": [30, 35, 40, 45, 80, 85, 90, 95]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Select features
X = df[["Study_Hours", "Marks"]]

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=42)

# Train the model and create clusters
df["Cluster"] = kmeans.fit_predict(X)

# Print the dataset
print(df)

# Print cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Plot the clusters
plt.scatter(df["Study_Hours"], df["Marks"], c=df["Cluster"])

# Show cluster centers
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker="X", s=200)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("K-Means Clustering")

plt.show()



# Student study Hour and marks with the inertai method
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create a simple dataset
data = {
    "Study_Hours": [1, 2, 2, 3, 4, 5, 8, 9, 10, 11],
    "Marks": [30, 35, 40, 45, 50, 55, 80, 85, 90, 95]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Select features
X = df[["Study_Hours", "Marks"]]

# STEP 1: Find Inertia for K values
inertia = []

# Try K values from 1 to 6
for k in range(1, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    # Store inertia value
    inertia.append(kmeans.inertia_)

# STEP 2: Draw Elbow Graph
plt.plot(range(1, 7), inertia, marker="o")

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for K-Means")

plt.show()

# STEP 3: Create K-Means Model
# Choose K = 2
kmeans = KMeans( n_clusters=2, random_state=42)

# Create clusters
df["Cluster"] = kmeans.fit_predict(X)

# Print data
print(df)

# STEP 4: Plot Clusters
plt.scatter( df["Study_Hours"], df["Marks"], c=df["Cluster"])

# Show cluster centers
plt.scatter( kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker="X", s=200)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("K-Means Clustering")

plt.show()












# new example with inertias
# Start by visualizing some data points:

import matplotlib.pyplot as plt

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x, y)
plt.show()





# Now we utilize the elbow method to visualize the intertia for different values of K:

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# The elbow method shows that 2 is a good value for K, so we retrain and visualize the result:
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()

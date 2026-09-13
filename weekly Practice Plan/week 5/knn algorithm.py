
'''
KNN
KNN is a simple, supervised machine learning (ML) algorithm that can be used for classification or regression tasks - and is also frequently used in missing value imputation. It is based on the idea that the observations closest to a given data point are the most "similar" observations in a data set, and we can therefore classify unforeseen points based on the values of the closest existing points. By choosing K, the user can select the number of nearby observations to use in the algorithm.'''

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

plt.scatter(x, y, c = classes)
plt.show()

# knn of value k = 1 and then 5
data = list(zip(x, y))
# print(data)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes)

# classify new data points
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)

plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()






# another example
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier

data = {
    'Height': [167, 182, 176, 173, 172, 174, 169, 173, 170],
    'Weight': [51, 62, 69, 64, 65, 56, 58, 57, 55],
    'Class': ['Underweight','Normal','Normal','Normal','Normal','Underweight','Normal','Normal','Normal']
}

df = pd.DataFrame(data)
print(df)

sns.scatterplot(x = 'Height', y = 'Weight', data = df, hue = 'Class')
plt.show()

newdata = list(zip(df['Height'], df['Weight']))
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(newdata, df['Class'])

# classify new data points
new_Height = 175
new_Weight = 65
new_point = [(new_Height, new_Weight)]
prediction = knn.predict(new_point)

# Plot original data
sns.scatterplot(x='Height', y='Weight', data=df, hue='Class')
# Plot new point
plt.scatter(new_Height, new_Weight, color='black', s=20)
# Add text
plt.text(new_Height - 1.7, new_Weight - 0.7, f"new point, class: {prediction[0]}")

plt.show()




# KNN on the load dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add class
df['Class'] = iris.target
print(df.head())

# Features and target
X = df[['petal length (cm)', 'petal width (cm)']]
y = df['Class']

# Create KNN
knn = KNeighborsClassifier(n_neighbors=3)
# Train model
knn.fit(X, y)

# New flower
new_length = 5.0
new_width = 1.8

new_point = [[new_length, new_width]]

# Prediction
prediction = knn.predict(new_point)

print("Predicted class:", prediction[0])
print("Predicted flower:", iris.target_names[prediction[0]])
# Plot original data
sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', hue='Class')
# Plot new point
plt.scatter(new_length, new_width, color='red', s=40)
# Label new point
plt.text(new_length - 0.5, new_width - 0.1, f"New point: {iris.target_names[prediction[0]]}")
plt.show()
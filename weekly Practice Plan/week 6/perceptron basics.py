
'''
A Perceptron is one of the simplest algorithms in Machine Learning. It is mainly used for binary classification.

Binary classification means there are only two classes, such as:
Yes / No
Pass / Fail
Spam / Not Spam
0 / 1
'''



# simple Perceptron code
import numpy as np
from sklearn.linear_model import Perceptron

# Input data
X = np.array([[1, 1], [2, 1], [4, 3], [5, 4], [6, 5]])

# Output
y = np.array([0, 0, 1, 1, 1])
# Create Perceptron model
model = Perceptron()
# Train the model
model.fit(X, y)
# Make prediction
prediction = model.predict([[3, 2]])
print("Prediction:", prediction)









# Perceptron from Scratch without using sklearn
import numpy as np

# Input data
X = np.array([[1, 1], [2, 1], [4, 3], [5, 4]])
# Actual output
y = np.array([0, 0, 1, 1])
# Initial weights
weights = np.array([0.0, 0.0])
# Initial bias
bias = 0.0
# Learning rate
learning_rate = 0.1
# Train for 10 epochs
for epoch in range(10):
    for i in range(len(X)):
        # Calculate weighted sum
        z = np.dot(X[i], weights) + bias
        # Step activation function
        if z > 0:
            prediction = 1
        else:
            prediction = 0
        # Calculate error
        error = y[i] - prediction
        # Update weights
        weights = weights + learning_rate * error * X[i]
        # Update bias
        bias = bias + learning_rate * error
print("Weights:", weights)
print("Bias:", bias)
# Test new data
new_data = np.array([3, 2])
z = np.dot(new_data, weights) + bias
if z > 0:
    prediction = 1
else:
    prediction = 0
print("Prediction:", prediction)








# Perceptron Program on Load Dataset on scale data with better imporvement

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create Perceptron model
model = Perceptron(max_iter=1000, random_state=42)
# Train model
model.fit(X_train, y_train)
# Predict
y_pred = model.predict(X_test)
# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
# Predict first test sample
print("Prediction:", model.predict([X_test[0]]))
print("Actual:", y_test[0])








'''
Perceptron Using Iris Dataset 🌸
The Iris dataset has 3 flower classes, but a basic Perceptron is best for binary classification, so we will select only 2 classes.'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load Iris dataset
iris = load_iris()

# Use only the first 100 samples
# This gives us only 2 classes: Setosa and Versicolor
X = iris.data[:100]
y = iris.target[:100]

# 2. Use only two features
# Feature 0 = Sepal Length
# Feature 2 = Petal Length
X = X[:, [0, 2]]

# 3. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
# 4. Create Perceptron model
model = Perceptron(max_iter=1000, eta0=0.1, random_state=1)
# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict test data
y_pred = model.predict(X_test)

# 7. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 8. Show confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# 9. Predict a new flower
new_flower = [[5.0, 1.5]]
prediction = model.predict(new_flower)
print("\nPrediction:", prediction)
if prediction[0] == 0:
    print("Flower: Setosa")
else:
    print("Flower: Versicolor")





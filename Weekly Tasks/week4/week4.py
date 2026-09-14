
# TASK 1
# Compute mean, median, standard deviation, and variance by hand, then verify with NumPy./
'''
Data = [2, 4, 6, 8, 10]
1. Mean
mean = sum of all values/ number of values
mean = 2 + 4 + 6 + 8 + 10 / 5

mean = 6

2. Median
first arrange in ascending order
median = 2, 4, [6], 8, 10

median = 6

3. Mode 
subract mean from every Value and then take the square 
2 - 6 = -4      16
4 - 6 = -2      4
6 - 6 = 0       0
8 - 6 = 2       4
10 - 6 = 4      16

sum of squared differences and divide by number of Value
variance = 40 / 5 = 8


4. Standard Divation 
it is the sqaure root of variance
standard divation = squareroot(8) = 2.828

'''

# Now verify using numpy

import numpy as np

# Dataset
data = np.array([2, 4, 6, 8, 10])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Variance
variance = np.var(data)

# Standard Deviation
std = np.std(data)

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std)







# TASK 2
# Implement simple linear regression from scratch using manual gradient descent.

import numpy as np
import matplotlib.pyplot as plt

#  Create simple dataset
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)

#  Initialize parameters
m = 0       # slope
b = 0       # intercept

learning_rate = 0.01
epochs = 1000

n = len(X)

#  Gradient Descent
for i in range(epochs):
    # Make predictions
    y_pred = m * X + b
    # Calculate error
    error = y_pred - y
    # Calculate gradients manually
    dm = (2 / n) * np.sum(X * error)
    db = (2 / n) * np.sum(error)
    # Update slope and intercept
    m = m - learning_rate * dm
    b = b - learning_rate * db

# Final prediction
y_pred = m * X + b

# Print results
print("Slope (m):", m)
print("Intercept (b):", b)

print("\nPredicted values:")

for actual, predicted in zip(y, y_pred):
    print("Actual:", actual, "Predicted:", round(predicted, 2))

# Plot the result
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("X")
plt.ylabel("y")

plt.title("Linear Regression from Scratch")
plt.legend()
plt.show()






# TASK 3
# Train scikit-learn's LinearRegression on a small dataset and evaluate with MAE, MSE, and R².

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([2, 4, 5, 4, 5, 7])

# Create and train model
model = LinearRegression()
model.fit(X, y)

#  Make predictions
y_pred = model.predict(X)
print("Actual values:   ", y)
print("Predicted values:", y_pred)

#  Evaluate the model
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

#  Print results
print("\nModel Evaluation")
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)

#  Print equation values
print("\nSlope:", model.coef_[0])
print("Intercept:", model.intercept_)





# TASK 4:
# Implement the sigmoid function manually and explain what it does in your own words.

import math

# Manual sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Test the function
print("Sigmoid(-5):", sigmoid(-5))
print("Sigmoid(-1):", sigmoid(-1))
print("Sigmoid(0):", sigmoid(0))
print("Sigmoid(1):", sigmoid(1))
print("Sigmoid(5):", sigmoid(5))


'''
What does it do?
A large negative number becomes close to 0
0 becomes 0.5
A large positive number becomes close to 1

suppose a model calculate score of 3.5
The score itself is not a probability. After applying sigmoid:   sigmoid(3.5) ≈ 0.97
Now we can interpret it as approximately a 97% probability.
'''







# TASK 5
# Train a logistic regression classifier and compute accuracy, precision, and recall.

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

#  Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

#  Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#  Create Logistic Regression
model = LogisticRegression(max_iter=5000)

#  Train the model
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)
#  Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)







# TASK 6
# Plot the decision boundary of a simple classifier on a 2D toy dataset.
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#  Create a 2D toy dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, cluster_std=2, random_state=42)

#  Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the classifier
model = LogisticRegression()

model.fit(X_train, y_train)

#  Create points for boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))

# Predict every grid point
grid_points = np.c_[xx.ravel(), yy.ravel()]
Z = model.predict(grid_points)
# Convert predictions back to grid shape
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3)
# Plot original data points
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="black")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Logistic Regression Decision Boundary")
plt.show()






# Mini Project 4
# Marks Predictor & Pass/Fail Classifier — one regression model predicting marks from study hours, and one classifier predicting pass/fail, each with a short evaluation summary.


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression

from sklearn.metrics import (mean_absolute_error, mean_squared_error,r2_score, accuracy_score,
    precision_score, recall_score)

#  Create Student Dataset
# Study hours
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

# Student marks
marks = np.array([35, 40, 45, 50, 55, 60, 65, 72, 80, 90])

# Pass/Fail labels
# 0 = Fail
# 1 = Pass
pass_fail = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
# Split the Dataset
X_train, X_test, marks_train, marks_test = train_test_split(X, marks, test_size=0.3, random_state=42)
# Same split for classification labels

X_train2, X_test2, y_train, y_test = train_test_split(X, pass_fail, test_size=0.3, random_state=42)

#  MARKS PREDICTOR
# Linear Regression
regression_model = LinearRegression()

# Train the model
regression_model.fit(X_train, marks_train)

# Predict marks
marks_pred = regression_model.predict(X_test)

# Evaluate Regression Model
mae = mean_absolute_error(marks_test, marks_pred)
mse = mean_squared_error(marks_test, marks_pred)
r2 = r2_score(marks_test, marks_pred)

print("========== MARKS PREDICTOR ==========")
print("Actual Marks:   ", marks_test)
print("Predicted Marks:", np.round(marks_pred, 2))
print("\nMAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("R² Score:", round(r2, 2))


#  PASS/FAIL CLASSIFIER
# Logistic Regression
classifier_model = LogisticRegression()

# Train classifier
classifier_model.fit(X_train2, y_train)

# Predict Pass/Fail
y_pred = classifier_model.predict(X_test2)

# Evaluate Classification Model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\n========== PASS/FAIL CLASSIFIER ==========")
print("Actual Values:   ", y_test)
print("Predicted Values:", y_pred)
print("\nAccuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))

# Predict a New Student
new_student = np.array([[7]])
predicted_marks = regression_model.predict(new_student)
predicted_result = classifier_model.predict(new_student)

print("\n========== NEW STUDENT PREDICTION ==========")
print("Study Hours:", new_student[0][0])
print("Predicted Marks:", round(predicted_marks[0], 2))

if predicted_result[0] == 1:
    print("Result: PASS")
else:
    print("Result: FAIL")

    
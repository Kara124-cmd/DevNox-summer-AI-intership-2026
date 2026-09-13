

# A dataset is a collection of data that we use to train a machine learning model.
# We need some unseen data to test the model. That is why we divide the dataset into different parts.

# Training Data : The training data is used to teach the machine learning model.
# Validation Data : /The validation data is used while developing the model.
# Test Data : The test data is completely unseen by the final model during training and tuning.

'''
70% → Train
15% → Validation
15% → Test
'''

# create own sample dataset and apply the train/test and split the dataset

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
# Create dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Exam_Score": [35, 40, 50, 55, 65, 70, 80, 85, 90, 95, 42, 48, 58, 63, 72, 78, 83, 88, 94, 98]
}
# Convert dictionary into DataFrame
df = pd.DataFrame(data)
# Features
X = df[["Hours_Studied"]]

# Target
y = df["Exam_Score"]
# First split:
# 70% Training
# 30% Temporary
X_train, X_temp, y_train, y_temp = train_test_split( X, y, test_size=0.30, random_state=42
)
# Second split:
# Temporary data becomes
# 15% Validation
# 15% Test
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42
)

# Create model
model = LinearRegression()
# Train model using ONLY training data
model.fit(X_train, y_train)

# VALIDATION
# Predict validation data
val_prediction = model.predict(X_val)

# Check validation error
val_error = mean_absolute_error( y_val, val_prediction
)
print("Validation Error:", val_error)


# TEST
# Predict test data
test_prediction = model.predict(X_test)

# Check test error
test_error = mean_absolute_error( y_test, test_prediction
)
print("Test Error:", test_error)










# Example With Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# STEP 1: TRAIN = 70%, TEMPORARY = 30%
X_train, X_temp, y_train, y_temp = train_test_split(X,y, test_size=0.30, random_state=42
)
# TEMPORARY DATA = 15% VALIDATION + 15% TEST
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

# Create model
model = DecisionTreeClassifier()

# TRAIN
model.fit(X_train, y_train)

# VALIDATION
val_prediction = model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_prediction)
print("Validation Accuracy:", val_accuracy)

# TEST
test_prediction = model.predict(X_test)
test_accuracy = accuracy_score(y_test,test_prediction)
print("Test Accuracy:", test_accuracy)







#  Example of Breast Cancer dataset and train a KNN Classification model.

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)

X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

val_prediction = model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_prediction)
print("Validation Accuracy:", val_accuracy)

test_prediction = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_prediction)
print("Test Accuracy:", test_accuracy)
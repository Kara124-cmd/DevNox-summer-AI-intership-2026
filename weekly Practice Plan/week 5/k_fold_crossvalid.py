








# predict whether a student will Pass (1) or Fail (0) based on:
# Hours Studied
# Previous Score

import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Create our own dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5, 6, 3, 7, 4, 8],
    "Previous_Score": [40, 45, 50, 55, 60, 70, 75, 90, 35, 65, 80, 48, 85, 58, 95],
    "Result": [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Print dataset
print(df)

# Features (input)
X = df[["Hours_Studied", "Previous_Score"]]

# Target (output)
y = df["Result"]

# Create Decision Tree model
model = DecisionTreeClassifier()

# Create 5 folds
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Apply K-Fold Cross Validation
scores = cross_val_score(model, X, y, cv=kfold)

# Print accuracy of each fold
print("\nAccuracy of each fold:")
print(scores)

# Print average accuracy
print("\nAverage Accuracy:")
print(scores.mean())







# Example: K-Fold Cross Validation with Logistic Regression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# Load dataset
data = load_breast_cancer()

# Features and target
X = data.data
y = data.target

# Create the model
model = LogisticRegression(max_iter=5000)

# Create 5 folds
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Apply K-Fold Cross Validation
scores = cross_val_score(model,X,y,cv=kfold)

# Print score of each fold
print("Scores of each fold:")
print(scores)

# Print average accuracy
print("Average Accuracy:")
print(scores.mean())











# Implementation of K-Fold Cross Validation
# Here’s a Python example of how to implement K-Fold Cross Validation using the scikit-learn library:
from sklearn.model_selection import KFold, cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

data = load_iris()
X, y = data.data, data.target  

# K-Fold Cross Validation
k = 5  
kf = KFold(n_splits=k, shuffle=True, random_state=42)

# Initialize the RandomForestClassifier model
model = RandomForestClassifier(random_state=42)

# Perform Cross Validation
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print(f"Accuracy for each fold: {scores}")

average_accuracy = np.mean(scores) 
print(f"Average Accuracy: {average_accuracy:.2f}")
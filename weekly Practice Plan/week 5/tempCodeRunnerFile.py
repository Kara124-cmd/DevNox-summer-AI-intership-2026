
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


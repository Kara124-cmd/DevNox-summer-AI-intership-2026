
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

    
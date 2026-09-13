

'''
confusion matrix is a table that is used in classification problems to assess where errors in the model were made.
The rows represent the actual classes the outcomes should have been. While the columns represent the predictions we have made. Using this table it is easy to see which predictions are wrong.'''



# creating confustin matrix using logistic regresssion

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

cm_display.plot()
plt.show()

# accuracy   : (True Positive + True Negative) / Total Predictions
Accuracy = metrics.accuracy_score(actual, predicted)

# precision   :    True Positive / (True Positive + False Positive)
Precision = metrics.precision_score(actual, predicted)

# Recall       :  True Positive / (True Positive + False Negative)
Sensitivity_recall = metrics.recall_score(actual, predicted)

# specificity   : True Negative / (True Negative + False Positive)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

# f1-score      :  2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
F1_score = metrics.f1_score(actual, predicted)

#metrics
print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})















# Example of Breast Cancer prgram 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# Load Dataset
data = load_breast_cancer()

X = data.data
y = data.target

# 70% Training
# 30% Temporary
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)

#Split Temporary Data
# 15% Validation
# 15% Test
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

#  Create KNN Model
model = KNeighborsClassifier(n_neighbors=5)

#  Train Model
model.fit(X_train, y_train)

#  Validation
val_prediction = model.predict(X_val)

val_accuracy = accuracy_score(y_val, val_prediction)

print("Validation Accuracy:", val_accuracy)

# Test Prediction
test_prediction = model.predict(X_test)

test_accuracy = accuracy_score(y_test, test_prediction)
print("Test Accuracy:", test_accuracy)

#  Confusion Matrix
cm = confusion_matrix(y_test, test_prediction)

print("\nConfusion Matrix:")
print(cm)








# Example of Iris Dataset 

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#  Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

#  Split Dataset
# 80% Training
# 20% Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
# Create Model
model = DecisionTreeClassifier()

#  Train Model
model.fit(X_train, y_train)

# Make Predictions
predicted = model.predict(X_test)
#  Create Confusion Matrix
confusion_matrix = metrics.confusion_matrix(y_test, predicted)

# Display Confusion Matrix
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,
display_labels=iris.target_names)
cm_display.plot()
plt.show()

# ACCURACY
Accuracy = metrics.accuracy_score(y_test, predicted)

# PRECISION
Precision = metrics.precision_score(y_test, predicted, average="weighted")

# RECALL
Recall = metrics.recall_score(y_test, predicted, average="weighted")

# F1-SCORE
F1_score = metrics.f1_score(y_test, predicted, average="weighted")
# PRINT METRICS
print({"Accuracy": Accuracy, "Precision": Precision, "Recall": Recall, "F1_score": F1_score})


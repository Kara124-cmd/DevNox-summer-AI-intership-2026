'''
Logistic Regression
is a supervised machine learning algorithm used for classification problems. Unlike linear regression, which predicts continuous values it predicts the probability that an input belongs to a specific class.

It is used for binary classification where the output can be one of two possible categories such as Yes/No, True/False or 0/1.
It uses sigmoid function to convert inputs into a probability value between 0 and 1'''

# Load Data  --> Separate X and y  --> Split Data  --> Create Model  -->  Train Model   --> Make Predictions  --> Calculate Accuracy


# 1 . Binomial Logistic regression: In binomial logistic regression, the target variable can only have two possible values such as "0" or "1", "pass" or "fail". The sigmoid function is used for prediction.

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=23
)
# Create and train model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predict classes: 0 or 1
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy * 100, "%")






# 2 . Multinomial Logistic Regression:
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics

# load dataset
digits = datasets.load_digits()
X = digits.data
y = digits.target

# seperate x and y into testng and training
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size = 0.4, random_state = 1
)

# create and train model 
reg = linear_model.LogisticRegression(max_iter=10000, random_state=0)
reg.fit(X_train, y_train)

# predict model
y_pred = reg.predict(X_test)

# check accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print('accuracy = ', accuracy * 100, "%")




# 3 .  Ordinal Logistic Regression:
#  Used when the dependent variable has three or more categories with a natural order, such as Low, Medium, and High. It considers the ranking of categories during prediction.

import numpy as np
import statsmodels.api as sm
from statsmodels.miscmodels.ordinal_model import OrderedModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Create simple data
X = np.array([
    [20], [25], [30], [35], [40],
    [45], [50], [55], [60], [65],
    [22], [28], [33], [38], [43],
    [48], [53], [58], [63], [68]
])

# 1 = Low, 2 = Medium, 3 = High
y = np.array([
    1, 1, 1, 1, 1,
    2, 2, 2, 2, 2,
    1, 1, 2, 2, 2,
    3, 3, 3, 3, 3
])

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)
# 3. Create Ordinal Logistic Regression model
model = OrderedModel(
    y_train,
    X_train,
    distr='logit'
)
# 4. Train the model
result = model.fit(method='bfgs', disp=False)
# 5. Make predictions
predictions = result.model.predict(
    result.params,
    exog=X_test
)
# Get the class with highest probability
y_pred = predictions.argmax(axis=1) + 1

# 6. Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", y_test)
print("Accuracy =", accuracy * 100, "%")











'''
Evaluation Metrics for Logistic Regression
Evaluating the logistic regression model helps assess its performance and ensure it generalizes well to new, unseen data. The following metrics are commonly used:
1 . Accuracy
2 . Precision
3 . Recall
4 . F1_score
'''


# 1 ) Accuracy tells us: Out of all predictions, how many were correct?
# The formula is:  Accuracy = TP+TN / TP+TN+FP+FN

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# import datasets
data = load_breast_cancer()
X = data.data
y = data.target

# split data into testing and training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 23
)
# create model 
model = LogisticRegression(max_iter = 10000)

# train model 
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100, "%")






# 2) . Precision: Of all the cases the model predicted as positive, how many were actually positive?
# Formula: Precision=  TP+FP / TP

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score

# import datasets
data = load_breast_cancer()
X = data.data
y = data.target

# split data into testing and training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 23
)
# create model 
model = LogisticRegression(max_iter = 10000)

# train model 
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# precision
precision = precision_score(y_test, y_pred)
print("prescision:", precision * 100, "%")




# 3) . Recall  Of all the actual positive cases, how many did the model successfully find?
# Formula: TP+FN / TP

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score

# import datasets
data = load_breast_cancer()
X = data.data
y = data.target

# split data into testing and training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 23
)
# create model 
model = LogisticRegression(max_iter = 10000)

# train model 
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# precision
recall = recall_score(y_test, y_pred)
print("recall:", recall * 100, "%")




# 4) . F1_score is usefull when you want the balance between the precisin and recall
# formula :   F1 = 2 x precision * recall / precision + recall

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

# import datasets
data = load_breast_cancer()
X = data.data
y = data.target

# split data into testing and training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 23
)
# create model 
model = LogisticRegression(max_iter = 10000)

# train model 
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# precision
F1 = f1_score(y_test, y_pred)
print("F1-Score:", F1 * 100, "%")






'''
Machine learning models should learn useful patterns from training data. When a model learns too little or too much, we get underfitting or overfitting.
Underfitting means that the model is too simple and does not cover all real patterns in the data.
Overfitting means that the model learns not just the underlying pattern, but also noise or random quirks in the training data. model memorizes training data
A good model finds the right spot, it is complex enough to capture real patterns, but not so complex that it “memorizes” noise'''


# Underfitting happens when the model fails to learn important patterns. It performs poorly on both training and testing data


# Overfitting happens when the model learns too much from the training data, including noise and outliers. It performs very well on training data but poorly on test data


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

#  Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# UNDERFITTING MODEL
# Very simple tree
underfit_model = DecisionTreeClassifier(max_depth=1, random_state=42)
underfit_model.fit(X_train, y_train)

train_pred = underfit_model.predict(X_train)
test_pred = underfit_model.predict(X_test)

print("UNDERFITTING MODEL")
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))

# GOOD FIT MODEL
# Medium complexity
good_model = DecisionTreeClassifier(max_depth=3,random_state=42)
good_model.fit(X_train, y_train)

train_pred = good_model.predict(X_train)
test_pred = good_model.predict(X_test)

print("\nGOOD FIT MODEL")
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))

# OVERFITTING MODEL
overfit_model = DecisionTreeClassifier(random_state=42)

overfit_model.fit(X_train, y_train)

train_pred = overfit_model.predict(X_train)
test_pred = overfit_model.predict(X_test)

print("\nOVERFITTING MODEL")
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))













'''Exmple of Breast Cancer dataset and compare:

Underfitting → Model is too simple.
Good fitting → Model learns properly.
Overfitting → Model learns training data too much.
'''

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#  Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# ---------------- UNDERFITTING ----------------
# Simple model: tree depth = 1
underfit_model = DecisionTreeClassifier(max_depth=1)

underfit_model.fit(X_train, y_train)

train_pred = underfit_model.predict(X_train)
test_pred = underfit_model.predict(X_test)

print("UNDERFITTING")
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))
# ---------------- GOOD FIT ----------------
# Balanced model
good_model = DecisionTreeClassifier(max_depth=4)

good_model.fit(X_train, y_train)

train_pred = good_model.predict(X_train)
test_pred = good_model.predict(X_test)

print("\nGOOD FIT")
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))

# ---------------- OVERFITTING ----------------

# Very complex model
overfit_model = DecisionTreeClassifier()

overfit_model.fit(X_train, y_train)

train_pred = overfit_model.predict(X_train)
test_pred = overfit_model.predict(X_test)

print("\nOVERFITTING")
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))



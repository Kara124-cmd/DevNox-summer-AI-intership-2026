
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
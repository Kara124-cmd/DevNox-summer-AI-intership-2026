

'''A Feed-Forward Neural Network (FNN) is one of the basic types of neural networks.
It is called feed-forward because data moves in only one direction:
Input Layer >  Hidden Layer >  Output Layer
'''

# Feed-Forward Neural Network Program
# We will use the built-in Iris dataset.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

#  Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#  Scale the data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#  Create Feed-Forward Neural Network
model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42)

#  Train the model
model.fit(X_train, y_train)

#  Make predictions
y_pred = model.predict(X_test)

#  Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#  Predict one new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

# Scale the new data
new_flower = scaler.transform(new_flower)
prediction = model.predict(new_flower)

print("Prediction:", prediction)
# Print flower name
print("Flower Name:", iris.target_names[prediction[0]])










# TensorFlow Feed-Forward Neural Network
# Import libraries
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 1. Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Scale the data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Create Feed-Forward Neural Network
model = tf.keras.Sequential([

    # Hidden Layer
    tf.keras.layers.Dense(8, activation="relu", input_shape=(4,)),
    # Another Hidden Layer
    tf.keras.layers.Dense(6, activation="relu"),
    # Output Layer
    tf.keras.layers.Dense(3, activation="softmax")
])

# 5. Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# 6. Train the model
model.fit(X_train, y_train, epochs=50, verbose=1)

# 7. Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)

print("\nTest Accuracy:", accuracy)

# 8. Predict the test data
predictions = model.predict(X_test)

# Convert probabilities into class numbers
y_pred = predictions.argmax(axis=1)

# Check accuracy
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# 9. Predict a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

# Scale the new flower data
new_flower = scaler.transform(new_flower)
prediction = model.predict(new_flower)

# Get the class with highest probability
class_index = prediction.argmax()
print("\nPredicted Flower:", iris.target_names[class_index])







# TensorFlow Neural Network – Binary Classification

import tensorflow as tf
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 3. Scale the data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Create Neural Network
model = tf.keras.Sequential([
    # First hidden layer
    tf.keras.layers.Dense(16, activation="relu"),
    # Second hidden layer
    tf.keras.layers.Dense(8, activation="relu"),
    # Output layer
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# 5. Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# 6. Train the model
model.fit(X_train, y_train, epochs=20, batch_size=16)

# 7. Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

# 8. Predict one sample
sample = X_test[0].reshape(1, -1)
prediction = model.predict(sample)
print("Prediction Probability:", prediction)

# Convert probability into 0 or 1
if prediction[0][0] >= 0.5:
    print("Prediction: Benign")
else:
    print("Prediction: Malignant")

print("Actual:", data.target_names[y_test[0]])



# TASK 1
# Split a dataset into train/validation/test sets and explain why each portion matters.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# 70% training and 30% temporary data
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)
# Split remaining 30% into validation and test
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

# Create and train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Check validation accuracy
val_predictions = model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_predictions)
print("Validation Accuracy:", val_accuracy)

# Final evaluation using test data
test_predictions = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_predictions)
print("Test Accuracy:", test_accuracy)












# TASK 2
# Compute a confusion matrix for a classifier and interpret each cell in plain English


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Actual answers
actual = [1, 0, 1, 1, 0, 0, 1, 0]
# Model predictions
predicted = [1, 0, 1, 0, 0, 1, 1, 0]

# Create confusion matrix
cm = confusion_matrix(actual, predicted)
print(cm)

# Display confusion matrix
display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No", "Yes"])
display.plot()
plt.show()













# TASK 3
# Plot an overfitting-vs-underfitting example on a toy dataset (train error vs. test error).

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Create a toy dataset
X, y = make_classification(n_samples=500, n_features=10, n_informative=5, n_redundant=2, random_state=42)

# Split dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Different model complexities
depths = range(1, 16)
train_errors = []
test_errors = []

# Train models with different tree depths
for depth in depths:
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )
    # Train model
    model.fit(X_train, y_train)

    # Predictions
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    # Calculate error
    train_error = 1 - accuracy_score(y_train, train_pred)
    test_error = 1 - accuracy_score(y_test, test_pred)
    # Save errors
    train_errors.append(train_error)
    test_errors.append(test_error)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(depths, train_errors, marker="o", label="Training Error")
plt.plot(depths, test_errors, marker="o", label="Test Error")

plt.xlabel("Model Complexity (Tree Depth)")
plt.ylabel("Error")
plt.title("Underfitting vs Overfitting")
plt.legend()
plt.grid()
plt.show()












# TASK 4
# Build a perceptron manually (weights, bias, step function) and test it on a simple case.


# Step activation function
def step_function(value):
    if value >= 0:
        return 1
    else:
        return 0

# Perceptron function
def perceptron(x1, x2, w1, w2, bias):
    # Calculate weighted sum
    weighted_sum = (x1 * w1) + (x2 * w2) + bias
    # Apply step function
    output = step_function(weighted_sum)
    return weighted_sum, output

# Weights and bias
w1 = 1
w2 = 1
bias = -1.5

# Test cases for AND gate
test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Test the perceptron
for x1, x2 in test_cases:
    weighted_sum, output = perceptron(x1, x2, w1, w2, bias
    )
    print("Input:", x1, x2, "| Weighted Sum:", weighted_sum, "| Output:", output)













# TASK 5
# Train a small feed-forward neural network (PyTorch or TensorFlow) on a toy dataset.

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# 1. Create a toy classification dataset
X, y = make_classification(n_samples=500, n_features=2, n_redundant=0, n_informative=2, n_classes=2, random_state=42)

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 3. Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Build a feed-forward neural network
model = tf.keras.Sequential([
    
    # Input layer
    tf.keras.layers.Dense(8, activation="relu", input_shape=(2,)),
    # Hidden layer
    tf.keras.layers.Dense(4, activation="relu"),
    # Output layer
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# 5. Compile the model
model.compile( optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# 6. Train the model
model.fit(X_train, y_train, epochs=20, verbose=1)
# 7. Test the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy:", accuracy)











# TASK 6:
# Tune the learning rate and number of epochs, and note how accuracy changes.

import numpy as np
import tensorflow as tf
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Create a toy dataset
X, y = make_classification(n_samples=1000, n_features=4, n_informative=3, n_redundant=1, random_state=42)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Different learning rates and epochs
learning_rates = [0.1, 0.01, 0.001]
epochs_list = [10, 50, 100]


# Try different combinations
for lr in learning_rates:
    for epochs in epochs_list:
        # Create a new model
        model = tf.keras.Sequential([tf.keras.layers.Input(shape=(4,)), tf.keras.layers.Dense(8, activation="relu"),
            tf.keras.layers.Dense(4, activation="relu"), tf.keras.layers.Dense(1, activation="sigmoid")])

        # Compile the model
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr), loss="binary_crossentropy", metrics=["accuracy"])
        # Train the model
        model.fit(X_train, y_train, epochs=epochs, verbose=0)
        # Test the model
        loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
        print("Learning Rate:", lr, "| Epochs:", epochs, "| Test Accuracy:", round(accuracy, 4))













#                                                  MINI PROJECT 
# Handwritten Digit Classifier — train a basic neural network on a small MNIST subset and produce a short evaluation report (accuracy, a few misclassified examples).

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#  Load MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("Original Training Shape:", X_train.shape)
print("Original Test Shape:", X_test.shape)

#  Use a small subset
X_train = X_train[:10000]
y_train = y_train[:10000]

X_test = X_test[:2000]
y_test = y_test[:2000]

print("\nSubset Training Shape:", X_train.shape)
print("Subset Test Shape:", X_test.shape)

#  Normalize pixel values
X_train = X_train / 255.0
X_test = X_test / 255.0

#  Build Neural Network
model = tf.keras.Sequential([
    # Convert 28x28 image into 1D array
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # Hidden layer
    tf.keras.layers.Dense(128, activation="relu"),
    # Output layer for digits 0-9
    tf.keras.layers.Dense(10, activation="softmax")
])

#  Compile model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
#  Train model
model.fit(X_train, y_train, epochs=5, validation_split=0.1, verbose=1)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\n----- Evaluation Report -----")
print("Test Accuracy:", round(accuracy * 100, 2), "%")
print("Test Loss:", round(loss, 4))

#  Make predictions
predictions = model.predict(X_test)

# Get the digit with highest probability
y_pred = np.argmax(predictions, axis=1)

#  Classification report
print("\n----- Classification Report -----")
print(classification_report(y_test, y_pred))

#  Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\n----- Confusion Matrix -----")
print(cm)

#  Find misclassified examples
wrong_indexes = np.where(y_pred != y_test)[0]
print("\nNumber of Misclassified Images:", len(wrong_indexes))

#  Show a few wrong predictions
plt.figure(figsize=(12, 6))

for i, index in enumerate(wrong_indexes[:10]):

    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[index], cmap="gray")
    plt.title(f"Actual: {y_test[index]}\n" f"Predicted: {y_pred[index]}")
    plt.axis("off")
plt.tight_layout()
plt.show()
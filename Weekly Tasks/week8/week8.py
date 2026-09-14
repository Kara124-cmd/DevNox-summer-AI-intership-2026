
# TASK 1
# Integrate this month's Python/ML work into your group's assigned project.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# 1. Load the Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

print("Features shape:", X.shape)
print("Target shape:", y.shape)

# 2. Create DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["target"] = y

print("\nFirst 5 rows:")
print(df.head())

# 3. Dataset Information
print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
df.info()

# 4. Visualize the Dataset
plt.figure(figsize=(8, 5))

plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"], c=df["target"])

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Dataset")
plt.show()

# 5. Separate Features and Target
X = df.drop("target", axis=1)
y = df["target"]

# 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# 7. Standardize the Data
scaler = StandardScaler()

# Fit scaler only on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data using the same scaler
X_test_scaled = scaler.transform(X_test)

# 8. Train Decision Tree Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_scaled, y_train)
print("\nDecision Tree model trained successfully.")

# 9. Make Predictions
y_pred = model.predict(X_test_scaled)

print("\nPredictions:")
print(y_pred)

# 10. Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nTest Accuracy:", accuracy)

# 11. Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 12. Confusion Matrix
# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)

disp.plot()
plt.title("Confusion Matrix")
plt.show()

# 13. Predict a New Flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

# Scale the new flower using the trained scaler
new_flower_scaled = scaler.transform(new_flower)

# Make prediction
prediction = model.predict(new_flower_scaled)

print("\nNew Flower Prediction:")
print("Predicted class:", iris.target_names[prediction[0]])

# 14. Save Model and Scaler
# Create models folder if it does not exist
os.makedirs("./models", exist_ok=True)

# Save Decision Tree model
joblib.dump(
    model,
    "./models/iris_model.pkl"
)

# Save scaler
joblib.dump(
    scaler,
    "./models/scaler.pkl"
)

print("\nModel and scaler saved successfully.")

# 15. Load Saved Model and Scaler
loaded_model = joblib.load(
    "./models/iris_model.pkl"
)

loaded_scaler = joblib.load(
    "./models/scaler.pkl"
)
print("Saved model and scaler loaded successfully.")

# 16. Test the Saved Model
new_sample = [[5.1, 3.5, 1.4, 0.2]]

# Scale the sample
new_sample_scaled = loaded_scaler.transform(new_sample)

# Predict using saved model
prediction = loaded_model.predict(new_sample_scaled)

print("\nPrediction from Saved Model:")
print("Predicted class:", iris.target_names[prediction[0]])










# TASK 2
# Write unit tests for at least 3 functions in your project.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def create_model():
    return DecisionTreeClassifier(random_state=42)

 # load_dataset = load_data("test_data.csv")

test_data = pd.DataFrame({
    "feature1": [1, 2, 3],
    "feature2": [4, 5, 6],
    "target": [0, 1, 0]
})
test_data.to_csv("./data/test_data.csv", index=False)

df = load_data("test_data.csv")
assert df.shape == (3, 3)
print("load_data() test passed!")

assert df.shape == (3, 3)
df.shape == (3, 3)

# test function 2
# Let's create data containing a duplicate and missing value.

test_df = pd.DataFrame({
    "feature1": [1, 2, 2, 3],
    "feature2": [4, 5, 5, None],
    "target": [0, 1, 1, 0]
})
cleaned_df = clean_data(test_df)
print(cleaned_df)

assert cleaned_df.isnull().sum().sum() == 0
assert cleaned_df.duplicated().sum() == 0

print("clean_data() test passed!")


# test function 3
model = create_model()
assert isinstance(model, DecisionTreeClassifier)
print("create_model() test passed!")

isinstance(model, DecisionTreeClassifier)


# All three tests passed togather 
# Test 1
df = load_data("./data/test_data.csv")

assert df.shape == (3, 3)


# Test 2
test_df = pd.DataFrame({
    "feature1": [1, 2, 2, 3],
    "feature2": [4, 5, 5, None],
    "target": [0, 1, 1, 0]
})

cleaned_df = clean_data(test_df)

assert cleaned_df.isnull().sum().sum() == 0
assert cleaned_df.duplicated().sum() == 0

# Test 3
model = create_model()
assert isinstance(model, DecisionTreeClassifier)
print("All 3 unit tests passed!")









# TASK 3
# Write a clear README documenting setup and usage for your project.

# Iris Flower Classification Using Decision Tree

## 1. Project Description
'''
This project uses **Machine Learning** to classify Iris flowers into one of three classes:

* Setosa
* Versicolor
* Virginica'''
'''
A **Decision Tree Classifier** is trained using the Iris dataset from Scikit-learn.

The project includes:

* Dataset loading and analysis
* Missing-value checking
* Data visualization
* Train-test splitting
* Feature scaling
* Decision Tree training
* Model prediction
* Accuracy evaluation
* Classification report
* Confusion matrix
* Prediction of a new flower
* Saving and loading the trained model
* Unit testing
'''

## 2. Technologies Used

'''The project is developed using Python and the following libraries:

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Joblib
* Unittest
'''
## 3. Project Structure
'''
text
iris-ml-project/
│
├── iris_project.py
│
├── test_iris_model.py
│
├── models/
│   ├── iris_model.pkl
│   └── scaler.pkl
│
└── README.md
```'''

### Files Description

'''| File                    | Description                   |
| ----------------------- | ----------------------------- |
| `iris_project.py`       | Main machine learning program |
| `test_iris_model.py`    | Unit tests for the project    |
| `models/iris_model.pkl` | Saved Decision Tree model     |
| `models/scaler.pkl`     | Saved StandardScaler          |
| `README.md`             | Project documentation         |

---
'''
## 4. Requirements
'''
Make sure Python is installed on your computer.

Check the Python version:

bash
python --version
```

The project requires these libraries:


numpy
pandas
matplotlib
scikit-learn
joblib

'''
## 5. Installation

### Step 1: Open the project folder

# Open Command Prompt or Terminal and go to your project folder:

# bash
# cd iris-ml-project


### Step 2: Install required libraries

# Run:
'''
pip install numpy pandas matplotlib scikit-learn joblib

'''
## 6. Running the Project

# Run the main Python file:


# python iris_project.py
'''
The program will:

1. Load the Iris dataset.
2. Display dataset information.
3. Check for missing values.
4. Display a dataset visualization.
5. Split the data into training and testing sets.
6. Scale the features.
7. Train a Decision Tree model.
8. Make predictions.
9. Calculate accuracy.
10. Display the classification report.
11. Display the confusion matrix.
12. Predict a new Iris flower.
13. Save the model and scaler.
14. Load the saved model and test it again.
'''
'''
## 7. Example Prediction

# The project uses this new flower:

new_flower = [[5.1, 3.5, 1.4, 0.2]]

# The model predicts:


# Predicted class: setosa

## 8. Model Evaluation

# The project evaluates the model using:

### Accuracy

# Accuracy shows how many predictions were correct.

accuracy_score(y_test, y_pred)

# Classification Report
The classification report provides:

* Precision
* Recall
* F1-score
* Support
'''
### Confusion Matrix

# The confusion matrix shows the number of correct and incorrect predictions for each Iris class.



## 9. Saving the Model

# The trained Decision Tree model is saved using Joblib:

joblib.dump(model, "./models/iris_model.pkl")


# The scaler is also saved:


joblib.dump(scaler, "./models/scaler.pkl")

# The `models` folder is automatically created if it does not already exist.

## 10. Loading the Saved Model

# The saved model can be loaded later without training it again:


loaded_model = joblib.load("./models/iris_model.pkl")
loaded_scaler = joblib.load("./models/scaler.pkl")

# Then a new prediction can be made:


new_sample = [[5.1, 3.5, 1.4, 0.2]]

new_sample_scaled = loaded_scaler.transform(new_sample)

prediction = loaded_model.predict(new_sample_scaled)

print(iris.target_names[prediction[0]])

'''
---

## 11. Running Unit Tests

The project contains three unit tests.

The tests check:

1. Whether the dataset has the correct shape.
2. Whether the model produces a valid prediction.
3. Whether the model achieves at least 80% accuracy.

Run the tests with:
''''''
bash
python -m unittest test_iris_model.py
```

Expected output:

text

Ran 3 tests

OK

'''
## 12. Machine Learning Workflow
'''
The project follows this workflow:


Load Dataset
     ↓
Explore Dataset
     ↓
Check Missing Values
     ↓
Visualize Data
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
Train Decision Tree
     ↓
Make Predictions
     ↓
Evaluate Model
     ↓
Save Model
     ↓
Load Saved Model
     ↓
Make New Prediction

'''

'''
## 13. Future Improvements

The project can be improved by:

* Comparing Decision Tree with Random Forest and KNN.
* Adding a web interface.
* Allowing users to enter flower measurements.
* Adding more visualizations.
* Using cross-validation.
* Deploying the model as a web application.
* Adding more automated tests.

'''

## 14. Conclusion

# This project demonstrates a complete basic Machine Learning workflow using the Iris dataset. It covers data preparation, visualization, model training, evaluation, prediction, model saving/loading, and unit testing.

# It provides a simple example of how a Machine Learning model can be integrated into a practical project.









# TASK 4
# Do a peer code review for one other group member and leave written feedback.

# Peer Code Review
# **Reviewer:** Muhammad Usman
# **Reviewed Project:** Python/ML Project
'''
I reviewed my group member's Python/ML project and checked the code for correctness, readability, organization, Machine Learning practices, testing, security, and documentation.

## Review Feedback'''

'''The project successfully implements the main Machine Learning workflow. It includes important steps such as loading the dataset, preprocessing the data, splitting the data into training and testing sets, training the ML model, making predictions, and evaluating the model's performance. This shows a good understanding of the basic concepts covered in our Python and Machine Learning work.
'''
### Code Quality and Organization

'''The code is generally understandable and uses appropriate Python libraries. However, the code could be better organized by dividing different tasks into separate functions. For example, data loading, preprocessing, model training, and prediction could each be placed in their own functions. This would make the code easier to read, reuse, and maintain.

Meaningful variable and function names should also be used. Adding comments to explain important or difficult sections would help other group members understand the code more easily.
'''
### Machine Learning Implementation

'''The ML workflow is implemented correctly at a basic level. The model is trained using the training data and then tested using unseen test data. The project also uses evaluation methods to check model performance.

I recommend adding more evaluation metrics such as accuracy, precision, recall, F1-score, and a confusion matrix where appropriate. Comparing the selected model with another algorithm could also help determine which model performs better.
'''
### Error Handling and Input Validation

'''Basic error handling should be added to handle problems such as missing datasets, incorrect input, or invalid values. User inputs should also be validated before being passed to the model. This will prevent unexpected errors and make the application more reliable.
'''
### Testing

'''The project should include unit tests for important functions. At least three tests could be written to check data loading, model prediction, and model performance. Automated testing will help ensure that the code continues to work correctly after future changes.
'''
### Security

'''The project should follow basic security practices when handling user input and files. User input should be validated, and functions such as `eval()` should not be used with untrusted input. Sensitive information such as passwords or API keys should not be stored directly in the source code.
'''
### Documentation

'''The project should have clear documentation explaining how to install the required libraries, run the program, and understand the output. A `requirements.txt` file would also make it easier for other group members to set up the project.
'''
## Overall Feedback

'''Overall, the project is a good implementation and demonstrates a clear understanding of Python and Machine Learning concepts. The main ML workflow is working, but the project can be improved by using better code organization, meaningful names, comments, error handling, input validation, unit testing, security practices, and documentation.

These improvements would make the project more **reliable, readable, maintainable, and professional** and would also make it easier to integrate with the group's overall project.

**Overall Rating: Good — Minor Improvements Recommended**
'''''








# TASK 5
# Find and fix at least 1 real bug uncovered during testing.

import pandas as pd

test_df = pd.DataFrame({
    "feature1": [1, 2, 2, 3],
    "feature2": [4, 5, 5, 6],
    "target": [0, 1, 1, 0]
})

cleaned_df = clean_data(test_df)
cleaned_df = cleaned_df.drop_duplicates(ignore_index=True)
assert cleaned_df.duplicated().sum() == 0

def clean_data(df):
    df = df.dropna()
    return df

# Fix the Bug
def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

# Run the Test Again
cleaned_df = clean_data(test_df)
assert cleaned_df.duplicated().sum() == 0
print("Bug fixed: duplicate rows are removed.")








# TASK 6
# Prepare a 5-minute progress-demo script for your group's project.

'''5-Minute Progress Demo Script
Since we have been using the Data Science / AI-ML Core project with the Iris dataset, you can use the following script for your progress demonstration. It is designed for about 5 minutes and can be presented directly in class.

5-Minute Progress Demo
0:00–0:30 — Introduction

Assalam-o-Alaikum everyone.

Today, I am going to give a short progress demonstration of our Data Science and AI/ML project.

The main purpose of our project is to build a simple machine learning pipeline that can load data, preprocess it, train a machine learning model, evaluate its performance, and make predictions on new data.

For our current progress, we are using the Iris dataset and a Decision Tree Classifier.'''

'''
0:30–1:15 — Dataset and Preprocessing
First, we load the Iris dataset using Scikit-learn.

The dataset contains information about three different Iris flower species.

We have four input features:

Sepal Length
Sepal Width
Petal Length
Petal Width

The target variable represents the flower species.

After loading the data, we convert it into a Pandas DataFrame so that it is easier to inspect and process.

We also check the shape of the dataset and check for missing values and duplicate records.'''



import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
df["target"] = iris.target
print(df.shape)
print(df.isnull().sum())


'''
1:15–2:00 — Data Visualization
    After preprocessing, we perform some basic data visualization.

    Visualization helps us understand the relationship between different features and identify how the       three classes are distributed.

    For example, we can create a scatter plot using petal length and petal width.

    This gives us a visual understanding of how the flower classes differ from each other.'''


from matplotlib import pyplot as plt
plt.scatter(df["petal length (cm)"], df["petal width (cm)"])

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Iris Dataset")
plt.show()


'''2:00–3:00 — Model Training
Next, we divide the dataset into training and testing sets.

The training data is used to teach the machine learning model, while the testing data is used to evaluate how well the model performs on unseen data.

We are currently using a Decision Tree Classifier.

A decision tree makes predictions by creating a series of decision rules based on the input features.'''


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

'''
3:00–3:45 — Model Evaluation
After training the model, we make predictions using the test data.

Then we evaluate the model using accuracy, classification report, and a confusion matrix.
'''


from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

print(cm)



'''
3:45–4:20 — Testing and Bug Fix
As part of our project development, we also started implementing unit testing.

We tested important functions such as data loading, data cleaning, and model creation.

During testing, we discovered a bug in our data cleaning function.

Initially, the function removed missing values but did not remove duplicate records.

We fixed the bug by adding drop_duplicates().'''

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

'''
4:20–4:50 — Current Progress
So far, our project has the following components:

First, dataset loading and exploration.

Second, data cleaning and preprocessing.

Third, basic data visualization.

Fourth, machine learning model training.

Fifth, model evaluation using accuracy and a confusion matrix.

Sixth, unit testing and bug fixing.

We have also prepared project documentation in the form of a README file.

4:50–5:00 — Future Work / Conclusion
For the next stage, we plan to improve the project by experimenting with additional machine learning models, improving visualization, performing better model comparison, and further improving testing and documentation.

This is our current progress, and we will continue improving the project in the next stage.'''





















# MINI Project 
# Full Group Demo — each group presents a working end-to-end slice of its assigned project (Cyber LLM / Face Recognition & Alerts / Data Science / AI-ML Core) to mentors.


# Import Libraries
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load Face Images
# !pip install face_recognition/
import face_recognition

DATASET_PATH = "../data/faces"

# Create the dataset directory if it doesn't exist
if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)
    print(f"Created directory: {DATASET_PATH}. Please upload your face images into subdirectories within this path (e.g., {DATASET_PATH}/person1/image.jpg).")

X = []
y = []

for person_name in os.listdir(DATASET_PATH):

    person_folder = os.path.join(DATASET_PATH, person_name)

    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = face_recognition.load_image_file(image_path)

        face_encodings = face_recognition.face_encodings(image)

        if len(face_encodings) == 0:
            print(f"No face found in: {image_path}")
            continue

        # Take the first detected face
        encoding = face_encodings[0]

        X.append(encoding)
        y.append(person_name)

print("Total face samples:", len(X))
print("People:", set(y))


# converts the face into a numerical representation.
face_encodings = face_recognition.face_encodings(image)

# stores the features.
X.append(encoding)

#stores the correct person's name.
y.append(person_name)

# Convert Data to NumPy Arrays
X = np.array(X)
y = np.array(y)

print("X shape:", X.shape)
print("y shape:", y.shape)

# split the data into train test set
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# Train the Machine Learning Model
model = KNeighborsClassifier(
    n_neighbors=3
)

model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

print("Predictions:")
print(y_pred)

print("\nActual:")
print(y_test)

# Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

# classification report 
print(classification_report(y_test, y_pred))



# Recognize a New Face
# We give the system a new image, and it predicts the person's name.
def recognize_face(image_path, model):
    
    image = face_recognition.load_image_file(image_path)

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(
        image,
        face_locations
    )

    predictions = []

    for encoding in face_encodings:

        prediction = model.predict([encoding])[0]

        predictions.append(prediction)

    return image, face_locations, predictions


# Test the Recognition Function
test_image_path = "../data/test/test_image.jpg"

image, face_locations, predictions = recognize_face(
    test_image_path,
    model
)

print("Recognized person:", predictions)


# Visualize the Recognized Face
# display the face and predicted name.
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

for (top, right, bottom, left), name in zip(
    face_locations,
    predictions
):

    cv2.rectangle(
        image,
        (left, top),
        (right, bottom),
        (0, 255, 0),
        2
    )

    cv2.putText(
        image,
        name,
        (left, top - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Face Recognition Result")
plt.show()

# Load dataset
def load_face_dataset(dataset_path):

    X = []
    y = []

    for person_name in os.listdir(dataset_path):

        person_folder = os.path.join(
            dataset_path,
            person_name
        )

        if not os.path.isdir(person_folder):
            continue

        for image_name in os.listdir(person_folder):

            image_path = os.path.join(
                person_folder,
                image_name
            )

            image = face_recognition.load_image_file(
                image_path
            )

            encodings = face_recognition.face_encodings(
                image
            )

            if len(encodings) == 0:
                continue

            X.append(encodings[0])
            y.append(person_name)

    return np.array(X), np.array(y)


# Train model
def train_face_model(X_train, y_train):

    model = KNeighborsClassifier(
        n_neighbors=3
    )

    model.fit(X_train, y_train)

    return model




# Recognize face
def recognize_face(image_path, model):

    image = face_recognition.load_image_file(
        image_path
    )

    face_locations = face_recognition.face_locations(
        image
    )

    face_encodings = face_recognition.face_encodings(
        image,
        face_locations
    )

    predictions = []

    for encoding in face_encodings:

        prediction = model.predict(
            [encoding]
        )[0]

        predictions.append(prediction)

    return image, face_locations, predictions





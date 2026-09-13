

# dicision tree
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Age': [25, 35, 45, 22],
    'Income': ['Low', 'High', 'Medium', 'Low'],
    'Buys': ['No', 'Yes', 'Yes', 'No']
})

# Convert categorical column 'Income' to numeric using one-hot encoding
data_encoded = pd.get_dummies(data[['Income']])
X = pd.concat([data[['Age']], data_encoded], axis=1)
y = data['Buys']

# Train a decision tree classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Visualize the tree
plt.figure(figsize=(10, 5))
tree.plot_tree(model, feature_names=X.columns, class_names=model.classes_, filled=True)
plt.show()






# another example
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('decision_tree_data.csv')
# print(df)

# convert non numerical columns to numerial columns
d = {'UK' : 0, 'USA' : 1, 'N' : 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'NO' : 0, 'YES' : 1}
df['Go'] = df['Go'].map(d)
# print(df)

# seperate feature columns and traget columsn, x = feature, y = columns
feature = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[feature]
y = df['Go']

print(X)
print(y)


# create the decision tree and fit values in it
model = DecisionTreeClassifier()
model.fit(X,y)
# display the tree
tree.plot_tree(model, feature_names=["Age", "Experience", "Rank", "Nationality"], filled=True)
plt.show()

# predict values of new person
print(model.predict([[40, 10, 7, 1]]))
print("[1] means 'GO'")
print("[0] means 'NO'")











# DECISION TREE CLASSIFICATION
# Predict whether a customer will buy a product

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# 1. CREATE DATASET
data = {
    'Income': [30000, 40000, 45000, 48000, 52000, 55000, 60000, 65000, 70000, 75000, 80000, 90000],
    'Age': [25, 28, 35, 40, 25, 29, 32, 35, 40, 45, 50, 55],
    'Previous_Purchase': [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    'Purchase': ['No Purchase','No Purchase','No Purchase','No Purchase','No Purchase','No Purchase','No Purchase','Purchase', 'Purchase','Purchase','Purchase','Purchase']
}


# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# 2. DISPLAY DATASET
print("Dataset:")
print(df)


# 3. SEPARATE FEATURES AND TARGET
# Input features
X = df[['Income', 'Age', 'Previous_Purchase']]
# Target/output
y = df['Purchase']

# 4. CREATE DECISION TREE MODEL
model = DecisionTreeClassifier(
    max_depth=3,
    criterion='entropy',
    random_state=42
)
# 5. TRAIN THE MODEL
model.fit(X, y)

# 6. DISPLAY DECISION TREE
plt.figure(figsize=(14, 8))

tree.plot_tree(model,feature_names=['Income','Age','Previous_Purchase'],
    class_names=model.classes_,
    filled=True,
    rounded=True
)

plt.title("Decision Tree - Customer Purchase Prediction")
plt.show()

# 7. PREDICT A NEW CUSTOMER
# Customer:
# Income = 60000
# Age = 35
# Previous Purchase = 1

new_customer = [[60000, 35, 1]]

prediction = model.predict(new_customer)

print("\nNew Customer:")
print("Income = 60000")
print("Age = 35")
print("Previous Purchase = 1")

print("\nPrediction:", prediction[0])

# 8. ANOTHER CUSTOMER
new_customer2 = [[45000, 40, 1]]

prediction2 = model.predict(new_customer2)

print("\nSecond Customer:")
print("Income = 45000")
print("Age = 40")
print("Previous Purchase = 1")

print("\nPrediction:", prediction2[0])













# ====================================================================================
# Random Forest Classifier

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load CSV file
df = pd.read_csv("decision_tree_data.csv")

# Convert Nationality into numbers
df["Nationality"] = df["Nationality"].map({"UK": 0,"USA": 1,"N": 2})

# Convert Go into numbers
df["Go"] = df["Go"].map({"NO": 0, "YES": 1})

# Features
X = df[["Age", "Experience", "Rank", "Nationality"]]
# Target
y = df["Go"]

# Create Random Forest
model = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the model
model.fit(X, y)

# Make prediction
prediction = model.predict([[40, 10, 7, 1]])

print("Prediction:", prediction)

if prediction[0] == 1:
    print("GO")
else:
    print("NO")








# Implementing Random Forest for Classification Tasks
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

# Make all column names lowercase
df.columns = df.columns.str.strip().str.lower()

# Print column names to check
print("Columns:", df.columns.tolist())

# Remove rows where survived is missing
df = df.dropna(subset=["survived"])

# Select features
X = df[["pclass", "sex", "age", "sibsp", "parch", "fare"]].copy()

# Target
y = df["survived"]

# Convert sex into numbers
X["sex"] = X["sex"].map({"female": 0, "male": 1})

# Fill missing age with median
X["age"] = X["age"].fillna(X["age"].median())

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Create Random Forest
rf = RandomForestClassifier(n_estimators=100,random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy, 2))

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Test one passenger
sample = X_test.iloc[[0]]

prediction = rf.predict(sample)

print("\nSample Passenger:")
print(sample)

# Display prediction
if prediction[0] == 1:
    print("Predicted Survival: Survived")
else:
    print("Predicted Survival: Did Not Survive")











# ====================================================================================
# XGBooost


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create XGBoost model
model = XGBClassifier(
    use_label_encoder=False,
    eval_metric="logloss"
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)




# xgbooost example on the breast cancer data set
# 1. Import Libraries

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from xgboost import XGBClassifier
import matplotlib.pyplot as plt


# 2. Load Dataset
data = load_breast_cancer()

# Input features
X = data.data

# Target variable
y = data.target

print("Feature names:")
print(data.feature_names)

print("\nTarget names:")
print(data.target_names)

# 3. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data size:", X_train.shape)
print("Testing data size:", X_test.shape)

# 4. Create XGBoost Model
model = XGBClassifier(

    # Number of trees
    n_estimators=100,

    # Learning rate
    learning_rate=0.1,

    # Maximum depth of each tree
    max_depth=3,

    # Random seed
    random_state=42,

    # Evaluation metric
    eval_metric="logloss"
)

# 5. Train the Model
model.fit(X_train, y_train)

print("\nModel Training Completed!")

# 6. Make Predictions
y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred[:10])

# 7. Predict Probabilities
y_prob = model.predict_proba(X_test)

print("\nPrediction Probabilities:")
print(y_prob[:5])


# 8. Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# 9. Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 10. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# 11. Feature Importance
importance = model.feature_importances_

print("\nFeature Importance:")

for feature, score in zip(data.feature_names, importance):
    print(feature, ":", score)

# 12. Plot Feature Importance
plt.figure(figsize=(10, 6))

plt.barh(data.feature_names, importance)

plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.title("XGBoost Feature Importance")

plt.tight_layout()
plt.show()











# example of used the Wholesale customers data set

import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from xgboost import cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df =  pd.read_csv('Wholesale customers data.csv')
print(df)

print(df.shape)

print(df.head())

print(df.info())

print(df.describe())

df.isnull().sum()

X = df.drop('Channel', axis=1)
y = df['Channel']
print(X.head())
print(y.head())

# convert labels into binary values
y[y == 2] = 0
y[y == 1] = 1

# again preview the y label
y.head()

# define data_dmatrix
data_dmatrix = xgb.DMatrix(data=X,label=y)

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# declare parameters
params = {'objective':'binary:logistic','max_depth': 4,'alpha': 10,'learning_rate': 1.0,'n_estimators':100}          
# instantiate the classifier 
xgb_clf = XGBClassifier(**params)
# fit the classifier to the training data
xgb_clf.fit(X_train, y_train)

# alternatively view the parameters of the xgb trained model
print(xgb_clf)

# make predictions on test data
y_pred = xgb_clf.predict(X_test)

# check accuracy score
print('XGBoost model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

params = {"objective":"binary:logistic",'colsample_bytree': 0.3,'learning_rate': 0.1,
                'max_depth': 5, 'alpha': 10}
xgb_cv = cv(dtrain=data_dmatrix, params=params, nfold=3,
                    num_boost_round=50, early_stopping_rounds=10, metrics="auc", as_pandas=True, seed=123)

print(xgb_cv.head())

# making the plot 
xgb.plot_importance(xgb_clf)
plt.rcParams['figure.figsize'] = [6, 4]
plt.show()


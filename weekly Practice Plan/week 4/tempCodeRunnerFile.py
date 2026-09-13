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


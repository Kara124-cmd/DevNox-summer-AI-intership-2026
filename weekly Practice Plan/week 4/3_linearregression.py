
# Linear regression is a machine learning algorithm used to predict a continuous numerical value by finding a straight-line relationship between variables.

# linear equation formula y = mx + c where: y is dependent, x is independent and c is intercept 

# Linear Regression From Scratch

import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 8, 10])

# Mean
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate slope
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

m = numerator / denominator

# Calculate intercept
b = y_mean - m * x_mean

# Prediction function
def predict(x):
    return m * x + b

# Prediction
prediction = predict(6)

print("Slope:", m)
print("Intercept:", b)
print("Prediction for x=6:", prediction)

# visualize our model
plt.scatter(x, y)

plt.plot(x, predict(x))

plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# This example using the scikit 
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 8, 10])

# Convert X to 2D
X = x.reshape(-1, 1)

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Slope
print("Slope:", model.coef_[0])

# Intercept
print("Intercept:", model.intercept_)

# Prediction
prediction = model.predict([[6]])

print("Prediction:", prediction[0])




# MAE, MSE, RMSE, R2

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Data
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

y = np.array([45,50,55,62,68,72,78,85,90,95])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Model parameters
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)

# New prediction
new_prediction = model.predict([[11]])

print("Prediction for 11:", new_prediction[0])







# ANOTHER EXAMPLE
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()





# BAD FIT
import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()








# Multiple Regression
# Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.

# MULITIPLE REGRESSION CODE
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [
    [2, 70, 60],
    [3, 75, 65],
    [4, 80, 70],
    [5, 85, 75],
    [6, 90, 80]
]

y = [55, 62, 70, 78, 85]

model = LinearRegression()

model.fit(X, y)

#prediction
prediction = model.predict([[7, 92, 85]])
print(prediction)

# visuailize
plt.scatter(X, y)

plt.plot(X, model.predict(X))

plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.show()




# another example
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('multiple_regression_cars.csv')

# print(df)
X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)




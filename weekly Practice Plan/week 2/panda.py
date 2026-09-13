

import pandas
mydata = {
    'name' : ['usman', 'ahmad', 'ali'],
    'age' : [10, 20 , 30]
}

myvar = pandas.DataFrame(mydata)
print(myvar)



# now use pandas as pd
import pandas as pd
data = {
    'name' : ['usman', 'hamid', 'jawad'],
    'age' : [20, 22, 24],
    'marks' : [60, 70, 80]
}

mydata = pd.DataFrame(data)
print(mydata)




'''What is a Series?
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.'''
# simple pandas series from a list
import pandas as pd
a = [1, 4, 6, 8, 9]
df = pd.Series(a)
print(df)


# accesss specific value using labels indexi
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])



# with the index argument you can name your own lables
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
# you can also acces item by reffering labels
print(myvar["y"])



# You can also use a key/value object, like a dictionary, when creating a Series.
# create a simple pandas sereies from dictionary
import pandas as pd
dictionary = {'name': 'usman', 'rollno': 22, 'age': 22}
mydict = pd.Series(dictionary)
print(mydict)
# here the key of dictionary become the labels



# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
import pandas as pd
dictionary = {'name': 'usman', 'rollno': 22, 'age': 22}
mydict = pd.Series(dictionary, index = ['name', 'age'])
print(mydict)







'''DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.'''

import pandas as pd
myvar = {
    'students' : ['usman', 'imran', 'hamid', 'jawad'],
    'age' : [21, 44, 22, 25]
}

datafr = pd.DataFrame(myvar)
print(datafr)



# What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


import pandas as pd
employe = {
    'name' : ['khan', 'kara', 'ali', 'ahamd'],
    'age' : [21, 23, 45, 65]
}

#load data into a DataFrame object:
obemploye = pd.DataFrame(employe)
# print(obemploye)

# locate rows Pandas use the loc attribute to return one or more specified row(s)
print(obemploye.loc[0])
# use the list of index 
print(obemploye.loc[[0,1]])


# also you can name your own indexing your index 
import pandas as pd
myvar = {
    'students' : ['usman', 'imran', 'hamid', 'jawad'],
    'age' : [21, 44, 22, 25]
}

datafr = pd.DataFrame(myvar, index = ['a', 'b', 'c', 'd'])
print(datafr)
# locate using name indexing
print(datafr.loc['b'])







# store passenger data of the Titanic. For a number of passengers, I know the name (characters), age (integers) and sex (male/female) data

import pandas as pd
df = pd.DataFrame({
  'Name' : ['usman', 'sara', 'jawad'],
  'Age' : [21, 22, 25],
  'Sex' : ['male', 'female', 'male'],
})

print(df)
# access only one columns When selecting a single column of a pandas DataFrame, the result is a pandas Series. To select the column, use the column label in between square brackets [].
print(df['Age'])
# find the maximum age from the dataframe
print(df['Age'].max())
# The describe() method provides a quick overview of the numerical data in a DataFrame
print(df.describe())


# The describe() method provides a quick overview of the numerical data in a DataFrame. As the Name and Sex columns are textual data, these are by default not taken into account by the describe() method.

# You can create a Series from scratch as well:
import pandas as pd
df = pd.Series([33, 56, 38], name = 'Age')
print(df)
# find the maximum age from the series
print(df.max())
print(df.describe())









'''Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.
'''
import pandas as pd
df = pd.read_csv('student.csv')
print(df)



'''
Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.'''

import pandas as pd
df = pd.read_csv('data.csv')
print(df)
print(df.to_string())      # Tip: use to_string() to print the entire DataFrame.

# You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows) 


# Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd
pd.options.display.max_rows = 1000
df = pd.read_csv('data.csv')
print(df)




# select a subset of a DataFrame specific columns
import pandas as pd
df = pd.read_csv('data.csv')
print(df['Pulse'])
# A check on how pandas interpreted each of the column data types can be done by requesting the pandas dtypes attribute:
print(df.dtypes)



'''Read JSON
Big data sets are often stored, or extracted as JSON.
JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.'''

import pandas as pd
df = pd.read_json('student.json')
print(df)
print(df.to_string())

# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries.


# Load a Python Dictionary into a DataFrame:
import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)




'''
Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.'''


# Get a quick overview by printing the first 10 rows of the DataFrame:
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))


# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
# accesssing two column 
print(df[['Calories', 'Pulse']])



'''There is also a tail() method for viewing the last rows of the DataFrame.
The tail() method returns the headers and a specified number of rows, starting from the bottom.
'''
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(8))
print(df.tail())
print(df.tail(10))
# '''Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.'''
print(df.info())
# Each column in a DataFrame is a Series. we can check it by using type
print(type(df['Duration']))      # it give us series

print(df['Duration'].shape)   # Dataframe.shape is an attribute of pandas series and dataframe containing seires and dataframe A pandas Series is 1-dimensional and only the number of rows is returned.





'''Data Cleaning
Data cleaning means fixing bad data in your data set.
Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates'''


# empty cells: gives you wrong result when you analyze data
# one way to deal with empty cell is to remove rows that contain empty cells
# Return a new Data Frame with no empty cells:

import pandas as pd
df = pd.read_csv('data.csv')
newdf = df.dropna()           #By default, the dropna() method returns a new DataFrame, and will not change the original.
print(newdf.to_string())
print(newdf.info())


# If you want to change the original DataFrame, use the inplace = True argument:
import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(inplace = True)
print(df.to_string())




'''Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:'''

# Replace NULL values with the number 130:
import pandas as pd
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
print(df.to_string())


# replace only for specified columns
import pandas as pd
df = pd.read_csv('data.csv')
df.fillna({'Maxpulse' : 130}, inplace = True)
print(df.to_string())



'''Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:'''

# Calculate the MEAN, and replace any empty values with it:
import pandas as pd
df = pd.read_csv('data.csv')
x = df['Calories'].mean()          # the average value (the sum of all values divided by number of values).
df.fillna({'Calories':x}, inplace = True)
print(df.to_string())


# Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd
df = pd.read_csv('data.csv')
x = df['Calories'].median()           #  the value in the middle, after you have sorted all values ascending.
df.fillna({'Calories':x}, inplace = True)
print(df.to_string())



# Calculate the MODE, and replace any empty values with it:
import pandas as pd
df = pd.read_csv('data.csv')
x = df['Calories'].mode()             #  the value that appears most frequently.
df.fillna({'Calories':x}, inplace = True)
print(df.to_string())









'''Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.'''



import pandas as pd
df = pd.read_csv('newdata.csv')
print(df)
# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:

# Pandas has a to_datetime() method for this:
import pandas as pd
df = pd.read_csv('newdata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())



# the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.
#remove row by using dropna() method

import pandas as pd
df = pd.read_csv('newdata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset = 'Date', inplace = True)
print(df.to_string())




'''Wrong Data
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99"'''


# If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.


# One way to fix wrong values is to replace them with something else.it is most likely a typo, and the value should be "45" instead of "450"
import pandas as pd
df = pd.read_csv('newdata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset = 'Date', inplace = True)
df.loc[7, 'Duration'] = 45                                  # df.loc[row, column]
print(df.to_string())


# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Loop through all values in the "Duration" column If the value is higher than 120, set it to 120:
import pandas as pd
df = pd.read_csv('newdata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset = 'Date', inplace = True)
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())



# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
# delete the rows where duration is greater than 120
import pandas as pd
df = pd.read_csv('newdata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset = 'Date', inplace = True)
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())






# removing duplicates
# Duplicate rows are rows that have been registered more than one time.

import pandas as pd
df = pd.read_csv('newdata.csv')
print(df.to_string())
print(df.duplicated())   # The duplicated() method returns a Boolean values for each row: True for duplicate else false

# To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace = True)
print(df.to_string())

















# Practice pandas details
import pandas as pd
data = pd.read_csv('newdata.csv')
print(data.to_string())

#select the duration which is greater thann 60
print(data['Duration'] > 60)

# the isin() conditional function returns a True for each row the values are in the provided list.
print(data['Duration'].isin([450, 30]))
























#  practice problem

import pandas as pd
df = pd.Series([10, 20, 30, 40, 50])
print(df)
print(df[2])
print(df[4])



#create a series and use custom labels
import pandas as pd
df = pd.Series([100, 200, 300], index = ['a', 'b', 'c'])
print(df)
print(df['b'])
print(df['c'])



# create the pandas dictionary of student and convert it to pandas series
import pandas as pd

student = {
  'name' : 'usman',
  'age' : 21,
  'gpa' : 4.0,
  'semester' : 4
}

data = pd.DataFrame(student, index = [0])
print(data)
print(data[['name','age']])




#  create a dataframe containing the student name, age and marks

import pandas as pd
student = pd.DataFrame({
  'name' : ['usman', 'hamid', 'jawad'],
  'age' : [21, 22, 34],
  'marks' : [90, 56, 67]
})

print(student)
print(student[['name', 'marks']])



# using the same data frame print rows 
import pandas as pd
student = pd.DataFrame({
  'name' : ['usman', 'hamid', 'jawad'],
  'age' : [21, 22, 34],
  'marks' : [90, 56, 67]
})
print(student.loc[0])
print(student.loc[2])
print(student.loc[[0, 1]])


# now create the custom dataframe index 
import pandas as pd
student = ({
  'name' : ['usman', 'hamid', 'jawad'],
  'age' : [21, 22, 34]
})

data = pd.DataFrame(student, index = ['a', 'b', 'c'])
print(data)
print(data.loc['b'])
print(data.loc['c'])





# create the dataframe and perform some basic opeartions

import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid", "Jawad"],
  "Age": [20, 21, 22, 20, 23],
  "Marks": [75, 88, 91, 67, 82]
}
newdata = pd.DataFrame(data)
print(newdata['Marks'].max())
print(newdata['Age'].max())
print(newdata.describe())
print(newdata.dtypes)
print(newdata.info())

print(type(newdata['Name']))
print(newdata.shape)
print(newdata['Name'].shape)



# read the csv file 
import pandas as pd
df = pd.read_csv('student.csv')
print(df)
print(df.to_string())  # display full dataframe

print(df.head(3))       # print first 3 row
print(df.head(5))       # print* first 5 row
print(df.tail(3))       # print last 3 row
print(df.tail(5))       # print last 5 row
print(df.info())

print(df['Marks'])
print(df[['Marks', 'Age']])
print(df.dtypes)


# read the json files
import pandas as pd
df = pd.read_json('student.json')
print(df)
print(df['Marks'])



# create the dataframe and remove the value containing empty values
import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Age": [20, None, 22, 21],
  "Marks": [75, 88, None, 91]
}

newdata = pd.DataFrame(data)
print(newdata)
newmod = newdata.dropna()              # remove empty row
print(newmod)



# remove missing data from the original permanently
import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Age": [20, None, 22, 21],
  "Marks": [75, 88, None, 91]
}
df = pd.DataFrame(data)
df.dropna(inplace = True)
print(df)



# fill all missing values with some value
import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Age": [20, None, 22, 21],
  "Marks": [75, 88, None, 91]
}

df = pd.DataFrame(data)
newdf = df.fillna(0)
print(newdf)



# fill one specific column
import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Age": [20, None, 22, 21],
  "Marks": [75, 88, None, 91]
}

df = pd.DataFrame(data)
newdf = df.fillna({'Age' : 30})
print(newdf)





# calculate the mean of marks, replace the missing value with mean and print dataframe
import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Age": [20, None, 22, 21],
  "Marks": [75, 88, None, 91]
}

df = pd.DataFrame(data)
mean = df['Marks'].mean()
print(mean)
missval = df.fillna({'Marks' : df['Marks'].mean(), 'Age' : df['Age'].mean()})
print(missval)
print(df)



# replace the missing value with median and mode
import pandas as pd
data = {
  'name' : ['usman', 'hamid', 'jawad', 'ali'],
  'age' : [21, 34, None, 44],
  'marks' : [77, 56, 88, None]
}

df = pd.DataFrame(data)
newdf = df.fillna({'age' : df['age'].median()})
print(newdf)

newmod = df['marks'].mode()[0]
newdf.fillna({'marks' : newmod}, inplace = True)
print(newdf)




# create the dataframe of the following and perform the operation on your own
import pandas as pd
students = {
  'name': ['usman', 'sara', 'jawad', 'ali', 'sara'],
  'age': [21, 34, 28, None, 25],
  'city': ['Lahore', 'Karachi', 'Islamabad', None, 'Lahore'],
  'salary': [50000, 65000, None, 80000, 55000],
  'marks': [77, 56, 88, None, 65]
}

df = pd.DataFrame(students)
df.fillna({'age' : df['age'].mean(), 'city' : df['city'].mode()[0], 'marks' : df['marks'].median()}, inplace = True)
print(df)







# wrong data dates

import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman"],
  "Date": ["2026-01-10", "2026/02/15", "March 20 2026"]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
print(df.dtypes)
print(df)



# remove invalid dates

import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Date": ["2026-01-10", "not a date", "2026-03-20", None]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors = 'coerce')
print(df)

# remove row where data is missing
df_clean = df.dropna(subset = ['Date'], inplace = True)
print(df_clean)
print(df)






import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman"],
  "Date": ["2026-01-10", "2026/02/15", "March 20 2026"]
}

df = pd.DataFrame(data)
print(df)

df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
print(df)




import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman"],
  "Duration": [45, 450, 60]
}

df = pd.DataFrame(data)
print(df)

df.loc[df['Duration'] > 45, 'Duration'] = 60
print(df)



import pandas as pd
data = {
  'name' : ['usman', 'hassan', 'ali', 'ahmad', 'anis'],
  'marks' : [60, 70, 450, 90, 30]
}

df = pd.DataFrame(data)
print(df)

for x in df.index:
  if df.loc[x, 'marks'] > 120:
    df.drop(x, inplace = True)
print()
print(df)



import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Ali", "Usman", "Ahmad"],
  "Marks": [80, 90, 80, 85, 90]
}
df= pd.DataFrame(data)
print(df)
dup = df.duplicated()
print(dup)
df.drop_duplicates(inplace = True)
print(df)



import pandas as pd
data = {
  "Name": ["Ali", "Ahmad", "Usman", "Hamid"],
  "Marks": [65, 80, 95, 70]
}

df = pd.DataFrame(data)
ew = df['Marks'] == 70
print(ew)



import pandas as pd
Duration = [30, 45, 60, 90, 120, 150]
ds = pd.Series(Duration)
res = ds[ds.isin([30, 90, 150])]
print(res)
newds = ds[(ds == 45) | (ds == 120)]
print(newds)




import pandas as pd
df = pd.read_csv('raw.csv')
print(df.to_string())
print()
# print(df.head())
# print('\n')
# print(df.tail())
# print()
# print(df.info())
# print()
# print(df.dtypes)

cln_dt = df.dropna(subset = ['Date'])
print(cln_dt)


ms_dr = df['Duration'].fillna(df['Duration'].mean()) 
print(ms_dr)

ms_cl= df['Calories'].fillna(df['Calories'].mean())
print(ms_cl)


for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df)


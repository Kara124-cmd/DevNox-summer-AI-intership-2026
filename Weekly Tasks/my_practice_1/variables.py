


# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


'''
Variables
Variables are containers for storing data values.'''

x = 5
name = 'usman'
print(x)
print(name)



'''Casting
If you want to specify the data type of a variable, this can be done with casting.'''

x = str(3)
y = int(3.99)
z = float(32)

print(x)
print(y)
print(z)

# get the type
print(type(x))
print(type(y))
print(type(z))


# Variable Names
myvar = "usman"
my_var = "usman"
_my_var = "usman"
myVar = "usman"
MYVAR = "usman"
myvar2 = "usman"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)



# multi words variable names
# 1 camel case
myVariableName = "John"

# 2 MyVariableName = "John"
MyVariableName = "John"

# 2 Snake case
my_variable_name = "John"




# deleting a variable
x = 10
print(x)
del x
print(x)

# counting characters in string variable
word = "Python"
length = len(word)
print("Length of the word:", length)



# Multi Words Variable Names
# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"






# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = 'orange', 'banana', 'mango'
print(x)
print(y)
print(z)


# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = 'Usman'
print(x)
print(y)
print(z)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

      
# Output Variables
# The print() function is often used to output variables.

x = 'my name is usman'
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = 'Usman'
y = 'is'
z = 'good boy'
print(x,y,z)

# You can also use the + operator to output multiple variables:
x = 'Usman'
y = 'is'
z = 'good boy'
print(x + y + z)



# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = 'python'
print(x + y)   # this show type error because python does not support to add int with string

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = 'python'
print(x, y)




# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = 'usman'
def myFunc():
    print('this is '+ x)

myFunc()


# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# Create a variable inside a function, with the same name as the global variable



x = 10
def myfunc():
    print('the number is : ', x)
myfunc()




x = 'usman'
def myfunc():
    x = 'imran'
    print('this is'+ x)

myfunc()
print('this is'+ x)



# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def myfun():
    global x
    x = 'usman'
    print('this is',x)

myfun()
print('this is',x)



# Also, use the global keyword if you want to change a global variable inside a function.

x = 'awesome'
def newfunc():
    global x
    x = 'nice'
    print('you are',x)
newfunc()
print('this is',x)



# deleting a variable
x = 5
y = 7
print(x)
print(y)

del x
print(x)


# to calculate the length of words in python
name = 'usman'
print(len(name))







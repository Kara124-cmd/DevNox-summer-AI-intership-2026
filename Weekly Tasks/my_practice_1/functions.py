"""Python Functions
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.

"""

# in python function is defined by def keyword along with function name
def myfunc():
    print("hello world")
myfunc()                # calling function



# function to add two number 
def cal_sum(a, b):
   sum = a + b
   print(sum)
   return sum

cal_sum(1, 5)


# function to calculate the fahreheit to celcius
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(99))
print(fahrenheit_to_celsius(104))


# return from the fucntion
def greeting():
   return 'hello, this is usman'
message = greeting()
print(message)

# functino arguments 
def myfunc(fname):
   print(fname + ' imran')
myfunc('usman')

# hello name 
def myfunc(name):
   print('hello', name)

myfunc('usman')


# Example: In this example, function checks whether the number passed as an argument is even or odd.
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))



# function to calculate the average of 3 number 
def avg(a, b, c):
   average = (a + b + c) / 3
   return average

average = avg(1,2,3)
print(average)



# number of arguments 

def my_name(fname, lname):
   print(fname + " " + lname)

my_name('usman', 'imran')



# default parameter
def my_func(name = 'friend'):
   print('hello', name)

my_func('usmman')
my_func('khan')
my_func()


# keyword arguments
def anime(animal, name):
   print('my ' + animal + ' name is ' + name)

anime(animal= 'dog', name= "hubby")


# sending a list of argument
def my_func(fruits):
   for fruit in fruits:
      print(fruit)

my_fruits = ['apple', 'banana', 'mango']
my_func(my_fruits)



# seding dictionary 
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


# return values 
def my_func(x, y):
   return x + y
add = my_func(2,4)
print(add)




# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.

# Inside the function, args becomes a tuple containing all the passed arguments:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


# Using *args with Regular Arguments
# You can combine regular parameters with *args.

# Regular parameters must come before *args:
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


# function that calculate the sum of any number value

def my_total(*numbers):
    total = 0
    for num in numbers:
      total += num
    return total
print(my_total(1,3,6))
print(my_total(20,10,10,34))





# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.

# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


# Using **kwargs with Regular Arguments
# You can combine regular parameters with **kwargs.

# Regular parameters must come before **kwargs:

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# *args collects extra positional arguments as a tuple.
# **kwargs collects extra keyword arguments as a dictionary.
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', fname='Usman', mid='imran', last='kara')










# write a function to print the length of list
number = [1, 2, 4, 5, 6, 7, 9]
def len_lists(list):
   print(len(list))
   return list
len_lists(number)




# write a program to print the list in single line
names = ['usman', 'imran', 'hamid', 'jawad', 'ahmad']
def print_names(list):
   for name in names:
      print(name, end=" ")

print_names(names)



# write a program to calculate the factorial 
def cal_fact(n):
   fact = 1 
   for i in range(1,n+1):
      fact *= i
   print(fact)

cal_fact(5)


# write a function to convert the usd to Pkr
def convert(usd):
   pkr = usd * 280
   print(pkr)
convert(1)


# program in function that return fahreheit to celsus
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(98))

# return values
def myfucn():
   return "hello wrold"
message = myfucn()
print(message)






# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# The data type will be preserved inside the function:

def my_function(fruits):
   for fruit in fruits:
      print(fruit)

my_fruits = ['apple', 'bananaa', 'mango', 'cherry']
my_function(my_fruits)


# seding return values
def my_fucntion(x,y):
   return x + y
print(my_fucntion(2,3))


# here can return differnt data types like list, tuples , dictionary
def my_function():
   return ['apple', 'mango', 'banana', 'cherry']

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])











"""Lambda Functions
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression."""

# syntax : lambda arguments : expression
# add 10 to argument a and return the result 
x = lambda a: a + 10
print(x(5))


# multiply argument a with b and then return the result
x = lambda a,b: a * b
print(x(2,5))



# threee arguments 
x = lambda a, b, c: a + b + c
print(x(2, 5, 6))




'''Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:'''

# Use that function definition to make a function that always doubles and triple the number you send in

def my_func(n):
   return lambda a: a * n
num_doubler = my_func(2)
print(num_doubler(11))
print(num_doubler(7))


# Or, use the same function definition to make both functions, in the same program:
def any_func(n):
   return lambda a: a * n
num_doubler = any_func(2)
num_tripler = any_func(3)

print(num_doubler(2))
print(num_tripler(12))


# Using Lambda with map()
# use lambda with map

lists = [1, 3, 5, 6, 7]
x = list(map(lambda x: x * 2, lists))
print(x)


# use lamdda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)






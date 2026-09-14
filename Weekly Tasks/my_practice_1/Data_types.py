


'''
 Data  types in python 
data types define the type of values stored in variables and determine the opeartions that 
can perform on data'''

# Numeric data types
# 1 - integer    2 - float     3 - complex number

a = 5
b = 5.0 
c = 2 + 3j

print(type(a))
print(type(b))
print(type(c))


'''
sequence data types
A sequence is an ordered collection of items, which can be of similar or different data types. Elements in a sequence can be accessed using indexing.'''
# 1 - string     2 - tuple     3 - List

# 1 string
s = "usman"
print(s)
print(type(s))
print(s[1:4])

# 2 List
Li = ['usman', 'kara', 'imran', 'goku']
print(Li)
print(type(Li))
print(Li[-3])

# tuple
tu = ('usman', 'kara', 23, 89.32)
print(tu)
print(type(tu))
print(tu[1:3])

# range
x = range(1, 10)
print(x)
print(type(x))
print(x[1])


''' boolean Data type
Boolean data type represents one of two values: True or False. It is mainly used in conditions and comparisons and is represented by the bool class.'''

print(type(True))
print(type(False))

# truthy and falsy value
if 1:
    print('truthy value')
if not 0:
    print('falsy value')


'''Set Data type
Sets are unordered and mutable collections used to store unique elements. Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.

'''
sets = {'a', 'b', 'c', 'a', 'd'}
print(sets)
print(type(sets))
for i in sets:
    print(i, end=" ")


# frozenset      = immutalbe set
x = frozenset({'apple', 'banana', 'cherry'})
print(x)
print(type(x))
# print(x[1])
# you can acces element by memebership operator not by indexing
for item in x:
    print(item)

# or by making it first list than indexing work
print('now this will be list from frozenset')
lists = list(x)
print(lists[1])
print(type(lists))




'''Dictionary Data type
Dictionaries are used to store data in key:value pairs. Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method
'''

dicts = {1: 'usman', 2: 'khan', 3: 'imran', 4: 'hamid'}
print(dicts)
print(dicts[1])
print(dicts.get(2))




''' binary Data type '''
# byte 
x = b"hello"
print(x)
print(type(x))

# bytearray
x = bytearray(5)
print(x)
print(type(x))

# memoryview(bytes)
x = memoryview(bytes(5))
print(x)
print(type(x))



# Getting the Data Type
# You can get the data type of any object by using the type() function:

x = 5
print(type(x))

x = 'Hello World'
print(type(x))

x = 32.32
print(type(x))

x = 1j
print(type(x))

x = [1, 2, 3, 4]
print(type(x))

x = (1, 3, 4)
print(type(x))

x = range(6)
print(type(x))

x = {'name': 'usman', 'age': 20}
print(type(x))

x = {'apple', 'banana', 'cherry'}
print(type(x))

x = frozenset({'apple', 'banan', 'mango'})
print(x)
print(type(x))

x = True
print(type(x))


# Lists are ordered and mutable collections used to store multiple items in a single variable.
a = [1, 2, 3]
print(a)
b = ["usman", "For", "me", 4, 5]
print(b[3])
print(b[-3])


# Tuples are ordered and immutable collections used to store multiple items in a single variable
t2 = ('usman', 'For', 'me', 1, 2)
print(t2[3])
print(t2[-3])


# Sets are unordered and mutable collections used to store unique elements.
s1 = {"a", "a", "b", "c", "b"}
print(s1)
s2 = {"usman", "imran", "ahmad"}
for i in s2:
    print(i)


# Dictionaries are used to store data in key:value pairs. Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.
d = {1: 'usman', 2: 'imran', 3: 'ali'}
print(d[1])    
print(d.get(2))


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

x = str('Hello world')
print(x)
print(type(x))

x = list(('apple', 'banana', 'mango'))
print(x)
print(type(x))

x = tuple(('apple', 'banana', 'mango'))
print(x)
print(type(x))


x = dict(name = 'usman', age = 20)
print(x)
print(type(x))






# variable type casting

x  =  int(2.2)
y = float(3)
z = str(33)

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))


# or simply
print(int(23.32))
print(float("78"))
print(str(323))







# 3.1. Using Python as a Calculator

# Let’s try some simple Python commands. Start the interpreter and wait for the primary prompt, >>>. (It shouldn’t take long.)

# 3.1.1. Numbers
# The interpreter acts as a simple calculator: you can type an expression into it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be used for grouping. For example:

print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
print(8 / 5)  # division always returns a floating-point number



# Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %:
print(17 / 3)   # classic division return na float
print(17 // 3)   # floor division discards the fractional part
print(17 % 3)   # the % operator returns the remainder of the division
print(5 * 3 + 2)    # floored quotient * divisor + remainder


# With Python, it is possible to use the ** operator to calculate powers

print(5 ** 2)
print(2 ** 7)


# The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:
height = 5 * 4
width = 10
print(height * width)


# In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:
tax = 12
price = 15.20
result = tax * price
print(result)
result = price + result
print(result)
result = round(result, 2)
print(result)



# A comparison between numbers of different types behaves as though the exact values of those numbers were being compared.

# All numeric types (except complex) support the following operations (for priorities of the operations

# Demonstrating Python's numeric operations

x = 10
y = 3

print("x + y  =", x + y)              # sum of x and y
print("x - y  =", x - y)              # difference of x and y
print("x * y  =", x * y)              # product of x and y
print("x / y  =", x / y)              # quotient of x and y (always float)
print("x // y =", x // y)             # floored quotient of x and y
print("x % y  =", x % y)              # remainder of x / y

print("-x     =", -x)                 # x negated
print("+x     =", +x)                 # x unchanged

print("abs(x) =", abs(-x))            # absolute value of x
print("abs(y) =", abs(-y))

print("int(x)   =", int(4.7))         # convert to integer
print("float(x) =", float(4))         # convert to floating point




# Bitwise Operations on Integer Types
# Bitwise operations only make sense for integers. The result of bitwise operations is calculated as though carried out in two’s complement with an infinite number of sign bits.

x = 2 
y = 5   

print("x       =", x, "->", bin(x))
print("y       =", y, "->", bin(y))


print("x | y   =", x | y, "->", bin(x | y))     # bitwise OR
print("x ^ y   =", x ^ y, "->", bin(x ^ y))     # bitwise XOR
print("x & y   =", x & y, "->", bin(x & y))     # bitwise AND


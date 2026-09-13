


'''Syntax
{key: value for (key, value) in iterable if condition}

key: The item to use as the dictionary key.
value: The item to use as the dictionary value.
iterable: Any sequence or collection to loop through.
condition (optional): Lets you include only certain items

'''
'''
Dictionary comprehension is used to create a dictionary in a short and clear way. It allows keys and values to be generated from a loop in one line. This helps in building dictionaries directly without writing multiple statements.
'''
# Example: This example creates a dictionary where numbers from 1 to 5 are used as keys and their squares are stored as values.


# Example
# Example
fruits = ['apple', 'banana', 'mango', 'cherry', 'lemon', 'melon']
newdict = {}
for fruit in fruits:
    if 'a' in fruit:
        newdict[fruit] = len(fruit)

print(newdict)

# now make it in dict comprehension
fruits = ['apple', 'banana', 'mango', 'cherry', 'lemon', 'melon']
newdict = {fruit: len(fruit) for fruit in fruits if 'a' in fruit}
print(newdict)




# another program 
fruits = ['apple', 'banana', 'mango', 'cherry', 'lemon', 'melon']
new_dict = {}
for fruit in fruits:
    if fruit != 'apple':
        new_dict[fruit] = len(fruit)

print(new_dict)


# dict comprehension
fruits = ['apple', 'banana', 'mango', 'cherry', 'lemon', 'melon']
new_dict = {fruit:len(fruit) for fruit in fruits if fruit != 'apple'}
print(new_dict)


# 
dicte = {}
for x in range(5):
    dicte[x] = x ** 2

print(dicte)
# 
dicte = {x: x**2 for x in range(5)}
print(dicte)


#another simple dictionary program
fruits = ['apple', 'banana', 'mango', 'cheryy', 'lemon', 'melon']
new_dict = {}
for x in fruits:
    if x != 'banana':
        new_dict[x] = x
    else:
        new_dict[x] = 'orange'

print(new_dict)


# dictionary comprehension
fruits = ['apple', 'banana', 'mango', 'cheryy', 'lemon', 'melon']
new_dict = {x: (x if x != 'banana' else 'orange') for x in fruits}
print(new_dict)



sq = {}
for x in range(1, 6):
    square = x**2       # calculate the sqaure of x 
    sq[x] = square      # add key-value pair to dictionary

print(sq)

# now make it a dictionary comprehension
sq = {x: x**2 for x in range(1, 6)}
print(sq)


# find the even number and add it to new list 
num = [1, 2, 3, 4, 5, 6]
res = {}
for x in num:
    if x % 2 == 0:
        res[x] = x
print(res)

# dict comprehension
num = [1, 2, 3, 4, 5, 6]
res = {x: x for x in num if x % 2 == 0}
print(res)


'''Explanation:
x takes values from 1 to 5 and x becomes the key
x**2 becomes the value
Each key and value pair is added to the dictionary in one line
'''


# Creating a Dictionary from Two Lists
# This method creates a dictionary by pairing each item from one list with the matching item from another list using zip().

keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  
d = {}
for k,v in zip(keys,values):
    d[k] = v
print(d)

#now the list comprehension of this for loop is 
keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  
d = {k:v for (k,v) in zip(keys, values)}
print(d)



# Example 2: This example maps a list of fruits to their name lengths
d = {fruit: len(fruit) for fruit in ['apple', 'banana', 'mango']}
print(d)

fruits = ['apple', 'banana', 'mango']
d = {}
for fruit in fruits:
    d[fruit] = len(fruit)

print(d)





# dictionary comprehension using conditional statements

a = {x:x**3 for x in range(10) if x % 4 == 0}
print(a)

# using for loop 
a = {}
for x in range(10):
    if x % 4 == 0:
        a[x] = x**3

print(a)



# nested dictionary comprehension



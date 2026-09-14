

# Python has two primitive loop commands:

# while loops
# for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
    print(i)
    i += 1

# break in loop stop execuation at specific point
i = 1
while i < 10:
    print(i)
    if i == 7:
        break
    i += 1


# continue statement skip the specific item in loop
i = 2
while i < 20:
    i += 1
    if i == 10:
        continue
    print(i)
    

# else in while looop
i = 1
while i < 9:
    print(i)
    i += 1

else:
    print('the loop is not longer to execute')









# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ['apple', 'banana', 'mango', 'cherry']
for x in fruits:
    print(x)


# For Statements 

words = ['dog', 'water', 'crocodile']
for w in words:
    print(w, len(w))


# looping through a string
for x in 'banana':
    print(x, end=" ")


# looping through string

for x in 'apple':
   print(x)


# break in for loop
fruits = ['apple', 'mango', 'banana', 'cherry', 'lemon']
for x in fruits:
   print(x)
   if x == 'banana':
      break

# continue statement
fruits = ['apple', 'mango', 'banana', 'cherry', 'lemon']
for fruit in fruits:
   if fruit == 'cherry':
      continue
   print(fruit)



# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['usman', 'hamid', 'khan', 'a', '32']
for i in range((len(a))):
    print(i, a[i])

# nested loop
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()



# enumerate function
seasons = ['autumn', 'summer', 'winter', 'spring']
print(list(enumerate(seasons)))

# lets take the start from the 1
print(list(enumerate(seasons, start=1)))


# break statement
students = ['usman', 'hamid', 'jawad', 'khan', 'ali', 'ahmad']
for i in students:
    if i == 'jawad':
        break
    print(i)

# continue
students = ['usman', 'hamid', 'jawad', 'khan', 'ali', 'ahmad']
for i in students:
    if i == 'khan':
        continue
    print(i)





# the range() function
# To loop through a set of code a specified number of times, we can use the range() function,

for x in range(10):
    print(x)

# specify the staring value by using the paremeter
for x in range(2,9):
    print(x)

# specify the steps by set the third parameterss
for x in range(2,9,2):
    print(x)



# else in for loop
for x in range(8):
    print(x)
else:
    print('the loop execution finish ')

# break in for loop using the else
for x in range(9):
    if x == 4:
        break
    print(x)
else:
    print('the loop finish execution')



# nested for loop
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'mango', 'banana']
for a in adj:
    for b in fruits:
        print(a, b)


# nested loops
i = [1,3,5]
j = [2,4,6]
for x in i:
   for y in j:
      print(x, y)





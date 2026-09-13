
# writing to files

'''Writing to files
To write to a file in python, you need to do two things:

Use the open(filename, mode) function in the write mode (“w”).
Use the file.write(text) function to actually write to the file. This function takes a string parameter to write to the file.'''


'''There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

Text and Binary Modes

In addition to the basic modes, you can specify how the file should be handled:

Text Mode       ("t"):
Default mode.
Opens the file in text mode.

Binary Mode     ("b"):
Opens the file in binary mode.
Useful for non-text files (e.g., images, executable files).
 
'''

# =======================================================================================

# let's go through each method step by step

# first create a file with 'x'
f = open('demo.txt', 'x')


# now open this file for writing in write mode 'w'
f = open('demo.txt', 'w')
f.write('this is the new demo file')
f.close()
# Checking File Properties
# Once the file is open, we can check some of its properties:
print('filename', f.name)
print('filemaode', f.mode)
print('isclose', f.closed)



# now append the data in this file 'a'
f = open('demo.txt', 'a')
f.write('this will append the new data')
f.write('\nthis is on second line')
f.close()

# now open the file in read mode
f = open('demo.txt', 'r')
print(f.read())
f.close()

# readline function
print(f.readline())

# open file in with statement
with open('demo.txt', 'r') as f:
    data = f.read()
    print(data)

# open file in readline()
with open('demo.txt') as f:
    print(f.readline())
    print(f.readline())


# Read Only Parts of the File
with open('demo.txt') as f:
    print(f.read(5))

# Loop through the file line by line:

with open('demo.txt') as f:
    for x in f:
        print(x)

# also you can read line by line using the object directly 
with open('demo.txt') as f:
    for line in f:
        print(line.strip())


# Reading All Lines into a List
# If you need to read all lines at once and store them in a list, you can use the readlines() method:
with open('demo.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())


# create a file and writing some text into it in function

def file():
    with open('newFile.txt', 'w') as f:
        f.write('this is first line \nthis is second line \nthis is thrid \nthis will be 4th')

    with open('newFile.txt', 'r') as f:
        print(f.read())

file()




# Handling exception when closing a file
try:
    with open('demo.txt', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError as e:
    print('error', e)
finally:
    f.close()

# another example
try: 
    myFile = open('newFile.txt', 'r')
    oneline = myFile.readline()
    print(oneline)
except FileNotFoundError as e:
    print('the file you are opening are not present please try another one', e)
finally:
    myFile.close()


# Overwrite Existing Content
# To overwrite the existing content to the file, use the w parameter:
with open('demo.txt', 'w') as f:
    f.write('this will overwrite (truncate) the text')
# now open and check if the text overwrite
with open('demo.txt') as f:
    print(f.read())



# deleting a file 
# To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove('demo.txt')


# check if file exist

import os 
if os.path.exists('demo.txt'):
    os.remove('demo.txt')
else:
    print("the files does not exist")


# remove any folder
import os
os.rmdir('myfolder_name')



# using while loop to print the content of file line by line

f = open("new.txt", "r")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()


# using for loop
f = open('new.txt', 'r')
for line in f:
    line = f.readline()
    print(line)
f.close()



# Write a program that reads a file containing a series of strings and displays the content of the file in reverse order, starting from the last line to the first.
with open('newFile.txt', 'r') as f:
    lines = f.readlines()
for line in reversed(lines):
    print(line.strip())



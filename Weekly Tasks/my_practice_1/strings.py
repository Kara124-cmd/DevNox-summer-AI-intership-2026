

# single line string
s = "I am Learning Python"
print(s)


# multi line string using triple single quotes of doubles qoutes
s = '''I'm a 
usman'''
print(s)


# accessing specific character in string
s = "ABCDEF"
print(s[0])   
print(s[4])

# string as an arrays
stre = 'Usman'
print(stre[1])

# looping through strings
for x in 'banana':
    print(x, end=" , ")

# loop through
s = "ABCDEF"
for char in s:
    print(char)


# calculate the length of string
a = 'usman'
print(len(a))


# check the certain character present in string
a = 'my name is usman'
print('name' in a)


# check if not 
a = 'this is visual studio code'
print('visual' not in a)


# check something which are present in the string
x = "i am a good boy, i practice python program on daily basis"
print('good' in x)

# or use it with if statement 
x = "i am a good boy, i practice python program on daily basis"
if 'good' in x:
    print('good is present in x ')



'''sting slicing '''
# Slicing in variables

# slicing
a = 'usman'
print(a[1:4])

# slicing from start
print(a[:5])

# slicing to end
print(a[2:])

# negative index
print(a[-2:-4])

# steps in string
print(a[: : -1])


s = "ABCDEF"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])

name = "UsmanImran"
print(name[2:6])

# starting from slice
name = "UsmanImran"
print(name[:5])

# ending to slice
name = "UsmanImran"
print(name[5:])

# using from negative indexing
name = "UsmanImran"
print(name[-5:-1])


# updating a string
s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  

print(s1)
print(s2)

# deleting a string
s = "ABC"
del s



# strings methods / modify strings
a = 'Usman Imran'
print(a.lower())


a = 'Usman Imran'
print(a.upper())


# remove whitespaces from beginning or end
a = ' Usman Imran'
print(a.strip())

# replace the string
a = 'Usman Imran'
print(a.replace('U', 'O'))

# split the string using any seperator
a = 'Usman, Imran'
print(a.split(','))






# string concatinations
a = 'Usman'
b = 'Imran'
c = a + b
print(c)


a = 'Usman'
b = 'Imran'
print(a + ' ' + b)




# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

name = 'Usman'
print(f'my name is : {name}')




# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value

price = 100
txt = f'The price of car is {price} dollars'
print(txt)


# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:



# Escape Characters
txt = 'It\'s alright.'
print(txt)

# this \\ quote will insert the single backslash in string
print('my name is Usman \\(backslash)')

# for new line "\n"
print('my name is Usman\nI am 20 years old')

# carriage return 
print('Hello\rWorld')

#tab 
print('hello\t world')

# backspace
print('Hello\b world')

# updating a string
s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  

print(s1)
print(s2)


# deleting a string
s = "ABC"
del s
print(s)






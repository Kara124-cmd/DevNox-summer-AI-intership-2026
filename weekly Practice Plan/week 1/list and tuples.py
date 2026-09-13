

# =============================  List =================================

'''
A list is a built-in data type that stores set of values, it can stores elements of different types
(int, float, string, etc)

List are mutable mean we can change the element in list
'''

marks = [32.4, 54.34, 15.4, 78.5, 66.8]
print(marks)
print(type(marks))
print(len(marks))
marks[0] = 40
print(marks)


# list slicing
student = ['Usman', 29, 43.2, 'manshera', 'pakistan', 'unversity student']
print(student)

print(student[1: 5])
print(student[: 5])
print(student[1: ])
print(student[-3: -1])
print(student[1 : 5 : 2])



# List Methods

lists = [2, 4, 6, 1, 8]
lists.append(3)             # add item at the last of list
print(lists)

lists.sort()               # make list sort in ascending order
print(lists)

lists.sort(reverse=True)   # list in descending order
print(lists)

lists.reverse()
print(lists)

lists.insert(0, 10)     # insert item at specific index
print(lists)

lists.sort()
print(lists)

lists.remove(3)              # delete a value at specific element
print(lists)

lists.pop(4)                   # pop value at the index
print(lists)






# =============================  List =================================

'''a built-in data type of different data 
immutable data type mean you cannot change ValueError
'''

tups = (1, 3, 5, 64.43, 'usman')
print(tups)
print(len(tups))
print(type(tups))



# Slicing in tuples

student = ('Usman', 29, 43.2, 'manshera', 'pakistan', 'unversity student')
print(student)

print(student[1: 5])
print(student[: 5])
print(student[1: ])
print(student[-3: -1])
print(student[1 : 5 : 2])



# tuples method

tupes = (2, 4, 6, 73, 32)
print(tupes.index(6))           # to search index for using elemnts

print(tupes.count(2))           # how many time a specific item occur in tuple





# ========================= practice Problem =============================================


# asks  user to enter the name of three movies and store them in a list
lists = []
for i in range(3):
    value = input(f'enter movies name {i + 1}')
    lists.append(value)

print(lists)


# check if a list contain the palindrome of element of not

lists = [1,2,3,2,1]
rev = lists[-1: -6 : -1]
if lists == rev:
    print('the list is palindrome')




mix = [1, 'abc', 'abc', 1]

rev_mix = mix.copy()
rev_mix.reverse()

if mix == rev_mix:
    print('this is palindrome')
else:
    print('this is not palindrom')



# count the number of student with grade 'A' in tuple

grade = ('c', 'd', 'a', 'b', 'c', 'a', 'd', 'a')
print(grade.count('a'))

# store above value in a list and sort them a to d

grade = ['c', 'd', 'a', 'b', 'c', 'a', 'd', 'a']
grade.sort()
print(grade)


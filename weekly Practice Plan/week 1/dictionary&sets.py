

# ========================== Dicionary ==============================

'''
dictionary are used to store data values in key:value pairs
they are unordered, mutable, don't allow duplicate keys'''

dict = {
    'name' : 'usman',
    'rollno' : 29,
    'marks' : [12, 32, 65]
}

print(dict)

# accesing the value of dict
print(dict['name'])
print(dict['marks'])

# changing value in dictionary
dict['name'] = 'Hamid'
print(dict['name'])

# added some value in dict
dict['surname'] = 'kara'
print(dict)


# Nested Dictionary
student = {
    'name' : 'usman',
    'subject' : {
        'phy' : 32,
        'chem' : 78,
        'math' : 43
    }
}
'''# print while dictionary
print(student)
#print all subjects of studetn
print(student['subject'])
# print specific subject marks of student
print(student['subject']['chem'])

'''

# method in dictionary

print(student.keys())       # this will show all the keys in dictionary
print(len(student))

print(student.values())       # return all values

print(student.items())       # return all the key_values pair

lists = list(student.items())    # type cast to the list
print(lists[1])                    # this will print the 2nd key-value pair








# Nested Dictionary
student = {
    'name' : 'usman',
    'subject' : {
        'phy' : 32,
        'chem' : 78,
        'math' : 43
    }
}
# mrthod to accessing the values in dictionary
print(student['name'])
print(student.get('name'))

student.update({'city' : 'manshera'})
print(student)

# we can add multiple elemetn in the dictionary we use 
new_dict = {'marks': 32, 'gender' : 'male'}
student.update(new_dict)
print(student)









# =========================================== Sets ============================================
'''
set is the collection unordered collection of elements
each element in the set must be unique & immutable'''

mix_set = {1, 2, 3, 1, 1, 'hello', 5, 'hello'}
print(mix_set)
print(type(mix_set))
print(len(mix_set))



# creating an empty set

sets = set()
print(type(sets))



# Methods in sets

sets = set()

sets.add(1)
sets.add(3)
sets.add(4)
sets.add(1)
sets.add((1,3,4))
print(sets)

# we cannot add the list and dictionary in sets because its immutable

sets.remove(1)
print(sets)

sets.clear()
print(len(sets))


# pop method remove the random value from the sets
num = {1, 3, 5, 4, 6, 3}
num.pop()
num.pop()
print(num)



# union and intersection
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

print(set1.union(set2))
print(set1.intersection(set2))




# store follwing word meaning in dicionary
# tabel : 'a peice of furniture', 'list of fact and figure'
# cat : 'a small animal'

dictionary = {
    'table': ['a peice of furniture', 'list of fact and figure'],
    'cat' : 'a small animal'
}
print(dictionary)



# given list of subject of student, one classroom required for one subject, how many classroon needed for all students

classroom  = {'python', 'java', 'c++', 'python', 'javascript', 'java', 'python', 'java', 'c++', 'c'}
print(classroom)
print(len(classroom))



# enter marks of threee subject from the user and store them in dictionary

dictionary = {}

for i in range(3):
    subject = input('enter your subject : ')
    marks = int(input('enter your marks : '))

    dictionary.update({subject : marks})
print(dictionary)


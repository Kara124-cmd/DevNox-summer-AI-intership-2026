
'''
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.'''

# Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# Now we can use the module we just created, by using the import statement:
import mymodule
mymodule.greeting('usman')



'''Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):'''

# save this in mymodule.py
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }


# Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1['age']
print(a)
mymodule.greeting('Hamid')


# naming re-naming a module
import mymodule as me
a = me.person1['country']
print(a)
me.greeting('Usman')



'''Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.'''

import platform
x = platform.system()
print(x)



# You can choose to import only parts from a module, by using the from keyword.
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
from mymodule import person1
print(person1['age'])




# print the date and time 
from datetime import datetime
now = datetime.now()
print(now)

from datetime import date
now = date(1993,12,23)
print(now)

from datetime import date
date = date.today()
print(date)



# random module
from random import random
print(random())


from random import random
li = []
for i in range(4):
    li.append(random())
print(li)

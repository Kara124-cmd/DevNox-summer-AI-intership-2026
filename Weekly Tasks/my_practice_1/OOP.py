


# create a simple class and thier object
class myclass:
   x = 5

obj1 = myclass()
print(obj1.x)

# multiple object   ==   
class myclass:
   x = 5
obj1 = myclass()
obj2 = myclass()
obj3 = myclass()

print(obj1.x)
print(obj2.x)
print(obj3.x)



# class is the blueprint for making objects

class Car:
    color = 'blue'
    brand = 'suzuki'

car1 = Car()
print(car1.color)
print(car1.brand)



# __init__ () function
# all clases have a function called __init__ which is alwasys executed when when the object of class being initiated

# Create a class named Person, use the __init__() method to assign values for name and age:

class person:
   def __init__(self, name, age):    #  The __init__() method is called automatically every time the class is being used to create a new object.
      self.name = name
      self.age = age

p1 = person('usman', 21)
print(p1.name)
print(p1.age)

# when we create a class without __init__ it looks like this
class person:
   pass
p1 = person()
p1.name = 'usaman'
p1.age = 21

print(p1.name)
print(p1.age)


# Set a default value in __init__ for the age parameter:
class person:
   def __init__(self, name, age = 21):
      self.name = name
      self.age = age

p1 = person('usman',)
print(p1.name)
print(p1.age)


class Student:
    Student_University = 'Hazara University'        # class attribute
    def __init__(self, name, marks):
        self.name = name                            # instance attribute
        self.marks = marks

    def welcome(self):
        print('welcome student')

s1 = Student('Usman', 98)
print(s1.name, s1.marks)
s2 = Student('ahmad', 78)
print(s2.name, s2.marks)
print(s1.Student_University)

s1.welcome()




# Create a Person class with multiple parameters:

class person:
   def __init__(self, name, age, city, country):
      self.name = name
      self.age = age
      self.city = city
      self.country = country

p1 = person('usman', 21, 'mansehra', 'Pakistan')
print(p1.name, p1.age, p1.city, p1.country)



class person:
   def __init__(self, name, age):
      self.name = name 
      self.age = age

   def greet(self):
      print('hello '+ self.name)

p1 = person('usman', 21)
print(p1.name, p1.age)
p1.greet()



# Access multiple properties using self:

class car:
   def __init__(self, brand, model, year):
      self.brand = brand
      self.model = model
      self.year = year

   def display_info(self):
      print(f'{self.brand} {self.model} {self.year}')

c1 = car('toyota', 'corolla', 2023)
c1.display_info()



# Call one method from another method using self:

class person:
   def __init__(self, name):
      self.name = name

   def greet(self):
      return 'Hello ' + self.name

   def welcome(self):
      message = self.greet()
      print(message + " welcome to our classs ")

p1 = person('usman')
p1.welcome()


# You can modify the value of properties on objects:

class person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = person('usman', 21)
print(p1.age)
p1.age = 26        # modify the object's property
print(p1.age)


# delete the age property

class person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = person('usman', 21)
print(p1.age)
del p1.age
print(p1.age)


# Class property vs instance property:

class person:
    specie = 'Human'     # class property
    def __init__(self, name, age):
       self.name = name             # intance property
       self.age = age 
p1 = person('usman', 21)
print(p1.name, p1.age)
print(p1.specie)



# When you modify a class property, it affects all objects:

class Person:
  lastname = "khan"

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)


# Add a new property to an object:

class Person:
   def __init__(self, name):
      self.name = name

p1 = Person('usman')
p1.age = 21
p1.city = 'Mansehra'

print(p1.age)
print(p1.city)


# create a student classs that takes name and marks of 3 subjects as argument in constructor that 
# create a method to print the average



# static method that don't use the self parameter (work at class level)   @staticmethod

class Student:
    Student_University = 'Hazara University'        # class attribute
    def __init__(self, name, marks):
        self.name = name                            # instance attribute
        self.marks = marks


    @staticmethod
    def hello():
        print('hello world')

s1 = Student('Usman', 98)
print(s1.name, s1.marks)
s2 = Student('ahmad', 78)
print(s2.name, s2.marks)
print(s1.Student_University)

s1.hello()





# Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class.
# Methods with Parameters
# Methods can accept parameters just like regular functions:

class Calculate:
   def add(self, a, b):
      return a + b

   def multipy(self,a, b):
      return a * b

c1 = Calculate()
print(c1.add(2, 3))
print(c1.multipy(3,5))


# A method that accesses object properties:

class Animal:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   def get_details(self):
      print(f'the name of animal is : {self.name} and age is : {self.age}')

a1 = Animal('Dog', 6)
print(a1.name, a1.age)
a1.get_details()



# The __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed:

# with __str__ method  
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__(self):
     return f"{self.name} : ({self.age})"
p1 = Person('Usman', 21)
print(p1)

# without __str__ method the program looks like
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = Person('usman', 21)
print(p1)


# delete a method
class Person:
   def __init__(self, name):
      self.name = name
   def greet(self):
      print("welocome", self.name)

p1 = Person('usman')

p1.greet()

del Person.greet

p1.greet()





#Abstraction
# Hiding the implementation detail of a class and only showing the essentail feature to the UserWarning

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print('Car Started ... ')

car1 = Car()
car1.start()




'''
 Python Polymorphism
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
'''


# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# For strings len() returns the number of characters:
x = "hello world"
print(len(x))

# For tuples len() returns the number of items in the tuple:
mytuple = ('apple', 'banana', 'cherry')
print(len(mytuple))

# For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))



'''
Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():'''

class Car:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model

   def move(self):
      print('drive!')

class Boat:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model

   def move(self):
      print('Sail!')

class Plane:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model

   def move(self):
      print('Fly!')

c1 = Car('ford', 'mustang')
b1 = Boat('ibiza', 'tourang')
p1 = Plane('boeing', '747')

for x in (c1, b1, p1):
   print(x.brand, x.model)
   x.move()



'''Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

'''
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model

   def move(self):
      print('Move!')

class Car(Vehicle):
   pass

class Boat(Vehicle):
   def move(self):
      print('Sail!')

class Plane(Vehicle):
   def move(self):
      print('Fly')

car1 = Car('Ford', 'Mustang')
boat1 = Boat('ibiza', 'tourang')
plane1 = Plane('boeing', '747')

for x in (car1, boat1, plane1):
   print(x.brand, x.model)
   x.move()






'''
Python Encapsulation
Encapsulation is about protecting data inside a class.

It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details of how your class works.'''

# Create a private class property named __age:

class Person:
   def __init__(self, name, age):
      self.name = name 
      self.__age = age

p1 = Person('usmana', 21)
print(p1.name)
print(p1.__age)

# Note: Private properties cannot be accessed directly from outside the class.

# Get Private Property Value
# To access a private property, you can create a getter method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())


# Set Private Property Value
# To modify a private property, you can create a setter method.

# The setter method can also validate the value before setting it:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("usman", 21)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())




# Use encapsulation to protect and validate data:
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(56)
print(student.get_grade())
print(student.get_status())



# Protected Properties
# Python also has a convention for protected properties using a single underscore _ prefix:

class Student:
   def __init__(self, name, age):
      self.name = name
      self._age = age

stu1 = Student('usman', 32)
print(stu1._age)

#encapsulation
# wrapping data and funtions into a single unit

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print('RS', amount, 'was debited')
        print('total balance = ', self.get_balance())

    def credit(self, amount):
            self.balance += amount
            print('RS', amount, 'was debited')
            print('total balance = ', self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(1000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(45500)
acc1.debit(10000)


# del is used to object property or object itself
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student('usman')
print(s1)
print(s1.name)

# delete the attribute property name 
# del s1.name
# print(s1.name)

# delete the object
del s1
print(s1)




# private attribue and method
# private attribute and method are meant to be used only within the class or not accessible from outside the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.number = acc_no
        self.__password = acc_pass

    def reset_pass(self):
        print(self.__password)

a1 = Account('1243', 'sbf23')
print(a1.number)
print(a1.reset_pass())







'''Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''



# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)   # no 'self', correct param names
        self.graduateyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduateyear)


# Create a Student, not a Person, since welcome() is a Student method
s1 = Student('Muhammad', 'Usman', 2027)
s1.printname()   # Muhammad Usman
s1.welcome()     # Welcome Muhammad Usman to the class of 2027




# inheritence 


# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)   # no 'self', correct param names
        self.graduateyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduateyear)


# Create a Student, not a Person, since welcome() is a Student method
s1 = Student('Muhammad', 'Usman', 2027)
s1.printname()   # Muhammad Usman
s1.welcome()     # Welcome Muhammad Usman to the class of 2027




# define a circle classs to create a circle with radius .

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return  (22/7) * self.radius ** 2

    def Perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(20)
print(c1.Area())
print(c1.Perimeter())



# create a class with Order which store item and price user dunder function() __gt__ to convery that ord1 > ord2 if the price of ord 1 > price of ord2
class Order:
    def __init__(self, item , price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order('chips', 23)
ord2 = Order('snake', 21)
print(ord1 > ord2)



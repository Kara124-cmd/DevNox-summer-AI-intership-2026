

# if statements
a = 39
b = 30
if a > b:
    print(f'{a} is greater than {b}')

 # another simple if statmet
num = 20 
if num > 0:
    print('The number is positive')

# multiple print statments in if block
age = 20
if age > 18:
    print('you are adult')
    print('you can vote')
    print('you have some legal rights')



# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.

logged_in = True
if logged_in:
    print('welcome back')








'''python Elif statement''' 
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

a = 12
b = 12
if a > b:
    print('a is greater than b ')
elif a == b:
    print('a is equal to b')


# multiple elif statement:
marks = int(input('enter the marks of student '))
if marks > 90:
    print('Excellent')
elif marks > 80:
    print('very good')
elif marks > 70:
    print('good')
elif marks > 50:
    print('average')
elif marks < 50:
    print('fail')


# else 
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")



# Validating user input:
username = 'usman'
if len(username) > 0:
    print(f'welcome, {username}')

else:
    print('Error! , please enter a valid usename')



# shorthand  if 
a = 10 
b = 4
if a > b: print('a is greater ')


# shortHand if_else
a = 10 
b = 5
print('a is greater ') if a > b else print(' b is greater')


# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

a = 4 
b = 1
bigger = a if a > b else b
print('the bigger is ', bigger)


# mutiple conditions on on lines
a = 20
b = 20
print('Greater') if a > b else print('=') if a == b else print('Not equal')



# multiple condition on one line

age = 18
print('you are eligible') if age > 18 else print('you have reached') if age == 18 else print('you can\'t vote')


# another example
x = 15 
y = 10
max_value = x if x > y else y
print('the maximum is : ', max_value)





# python logical operators in conditions 

# And operator &
a = 5
b = 2
c = 7
if a > b and c > a: 
   print('both conditions are true')

# or operator "|"
a = 5
b = 2
c = 7
if a > b or a > c:
   print('at least one condition are satisfieds')

# not operator
a = 2
b = 5
if not a > b:
   print('A is not greater than b')

# now combining and or and not 
age = 25
is_student = False
has_discount = True
if (age < 18 or age > 65) and not is_student or has_discount:
   print('Discount applies')


# more example 
username = 'usman'
passw = 'secret124'
is_verified = True
if username and passw and is_verified:
   print('login successfully')
else:
   print('try again')


# login credentials
username = 'usman'
password = 'usam21234'
is_verified = True

if username and password and is_verified:
    print('login successfully')

else:
    print('login failed')






# Nested If statement



x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



age = 24
has_liceneced = True
if age > 20:
    if has_liceneced:
      print('you are eligible for driving')
    else:
      print('Make a licenced first')
else:
   print('you are too yuong to driving')


# another nested if
score = 87
attendence = 85
is_assignment = True

if score > 85:
    if attendence > 90:
        if is_assignment:
         print('you have good acadmenic')
        else:
           print('you need to complete your assignment')
    else:
      print('passs but low attendace')
else:
   print('fail')


# grade calculation using nested if else
score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")



# one more example
username = "usman"
password = "secret123"
is_active = True

if username:
    if password:
        if is_active:
         print('login succesfull')
        else:
           print("please activate your account")
    else:
      print("your entered incorrect password")
else:
   print('the username you entered not available')



# The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.
day = 6
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:                     # default case
        print('nothing')



# combine values
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")




# another example

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))
print(http_error(418))
print(http_error(500))


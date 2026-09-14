

'''---------------------------------Python Data Types--------------------------------------'''


'''The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.'''

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:


n = 10
try:
   res = n / 0
except ZeroDivisionError:
   print('can\'t be divided by zero')



'''try: Runs the risky code that might cause an error.
except: Catches and handles the error if one occurs.
else: Executes only if no exception occurs in try.
finally: Runs regardless of what happens useful for cleanup tasks like closing files.'''

try: 
   n = 0
   res = 100 / n
except ZeroDivisionError:
   print('number cannot be divited by zero')

except ValueError:
   print('enter a valid number')

else:
   print('result is ', res)

finally:
   print('Execution complete')


# Example: This code handles ValueError and ZeroDivisionError with different messages.

try: 
   x = int('str')
   inv = 1 / x

except ValueError:
   print('Not valid ')

except ZeroDivisionError:
   print('zero has no inverse')


# multiple excpetions
 
a = ['10', 'twenty', 30]
try:
   total = int(a[0]) + int(a[1])

except (ValueError, TypeError) as e:
   print('Error', e)

except IndexError:
   print("index out or range")


# Example: This code tries dividing a string by a number, which causes a TypeError.
try:
   div = '100' / 20

except ArithmeticError:
   print('arithmatic problems')

except TypeError:
   print('this is type error')

except:
   print('something went wrong')



# Example: This code raises a ValueError if an invalid age is given.
def set(age):
   if age < 0:
      raise ValueError('age cannot be negative')
   print(f'the age is ', age)

try:
   set(6)
except ValueError as e:
   print(e)



# multiplication table
try:
   num = int(input('enter a number : '))
   print('multiplication table of ', num)

   for i in range(1, 11):
      print(f'{num} * {i} = {num * i}')

except ValueError:
   print('you entered invalid value, enter valid integer')


# division of number 

def div(a,b):
   try:
      result = a / b
   except ZeroDivisionError:
      print('number cannot be divide by zero')

   except TypeError:
      print('you entered invalid value')

   else:
      print('the result is ', result)

   finally:
      print('all the execution done succesfully')

div(4,"1")




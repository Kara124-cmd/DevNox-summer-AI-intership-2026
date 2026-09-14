

 # task 1
# Swap two numbers without a third variable; explain your approach in a comment.
a = 5
b = 7

a = a + b
b = a - b
a = a - b

print(a)
print(b)



   #task 2
# Write a program to check if a number is prime AND if a string is a palindrome
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# string is a palindrome
my_str = str(input('enter the string : '))
my_str = my_str.lower()
rev_str = my_str[::-1]
if my_str == rev_str:
    print('the string is palindrome ')
else:
    print('the string is not palidrome')






                                                    #task 3
# Print the Fibonacci series using a loop
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a + b
    print()
fib(20)


                                                    #task 3
# Print the Fibonacci series using using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")






                                   #task 4
# Build a small function library: temperature converter + simple area calculator (circle, rectangle).

# Temperature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Area Calculator

def circle_area(radius):
    return 3.14 * radius * radius

def rectangle_area(length, width):
    return length * width


print("Temperature Converter")
print("25°C =", celsius_to_fahrenheit(25), "°F")
print("77°F =", fahrenheit_to_celsius(77), "°C")

print("\nArea Calculator")
print("Circle Area =", circle_area(5))
print("Rectangle Area =", rectangle_area(4, 6))




# Write exception-safe code that keeps asking for input until a valid integer is entered.

def _valid_integer(prompt = 'Enter an integer : '):
    # while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            return value
        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            raise

number = _valid_integer("Please enter an integer: ")
print(f"{number} is the valid integer")




'''
MINI PROJECT
Command-line Student Grade Calculator — takes marks as input, computes grade using functions and conditionals, and handles invalid input gracefully with exceptions.
'''

def calculate_marks():
    while True:
        try:
            marks = int(input("Enter your marks (0-100): "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue
            return marks

        except ValueError:
            print("Invalid input! Please enter an integer.")

def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "Grade A"
    elif marks >= 80 and marks < 90:
        return "Grade B"
    elif marks >= 70 and marks < 80:
        return "Grade C"
    elif marks >= 60 and marks < 70:
        return "Grade D"
    elif marks >= 50 and marks < 60:
        return "Grade E"
    elif marks < 50 and marks == 0:
        return "Fail! keep strugling"
    else:
        print('enter marks between the ranges')

number = calculate_marks()
grade = calculate_grade(number)

print(f"\nMarks = {number}")
print(f"Result = {grade}")


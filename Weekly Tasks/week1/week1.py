


# reverse string without using built-in reverse function
name = 'usman'
rev = name[ : : -1]
print(rev)


# check if two strings of anagrams of each other

def check_anagram(s1, s2):
    s1_list = sorted(s1.lower())
    s2_list = sorted(s2)
    return s1_list == s2_list

str1 = 'Heart'
str2 = 'earth'
print(sorted(str1))
print(sorted(str2))
anagram = check_anagram(str1, str2)
print(anagram)



# write a function that returns second largest number in a list

def second_largest(n):
    n.sort()
    return n[-2]

numbers = [1, 3, 4, 6, 9, 2, 5, 11]
largest = second_largest(numbers)
print(largest)



# create a student class with name/marks attribute and a method to compute grade.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compute_grade(self,name, marks):
        if marks > 90 and marks <= 100:
            print(f'{name} marks is {marks} and the grade of student witll be : Grade A')
        elif marks > 70 and marks < 90:
            print(f'{name} marks is {marks} and the grade of student witll be : Grade B')
        elif marks > 60 and marks < 70:
            print(f'{name} marks is {marks} and the grade of student witll be : Grade C')
        elif marks > 50 and marks < 60:
            print(f'{name} marks is {marks} and the grade of student witll be : Grade D')

        else:
            print('Invalid marks')
student1 = student('alice', 100)
student1.compute_grade(student1.name, student1.marks)



# Handle division - by - zero and invalid input safely with try/except

try: 
    nominator = int(input('enter an number : '))
    denominator = int(input('enter another nummber : '))
    result = nominator / denominator
    print(int(result))

except ValueError:
    print('you entered the invalid input datatype')

except ZeroDivisionError:
    print('the number cannot be divisible by zero')




# simple to do list app (add/remove/view tasks) using functions and list

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)

def remove_task():
    view_tasks()
    if len(tasks) > 0:
        number = int(input("Enter task number to remove: "))
        if 1 <= number <= len(tasks):
            tasks.pop()
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

while True:
    print("\n== To-Do List ==")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")






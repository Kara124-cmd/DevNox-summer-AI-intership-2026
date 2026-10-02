class Student:
    def __init__(self, student_id, name, department):
        self.id = student_id
        self.name = name
        self.department = department

    def show(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)


student_list = []


def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        department = input("Enter Department: ").strip()

        if student_id == "" or name == "":
            print("Student ID and Name cannot be empty!")
            input("Press Enter to continue...")
            return

        if find_student(student_id) is not None:
            print("Student ID already exists!")
            input("Press Enter to continue...")
            return

        student = Student(student_id, name, department)
        student_list.append(student)

        print("Student added successfully!")
        input("Press Enter to continue...")

    except Exception as e:
        print("Error:", e)
        input("Press Enter to continue...")


def view_students():
    print("\n========== STUDENT RECORDS ==========")
    print("Total Students:", len(student_list))

    if len(student_list) == 0:
        print("No students found.")
    else:
        for number, student in enumerate(student_list, start=1):
            print("\nStudent", number)
            student.show()
            print("------------------------------------")

    input("\nPress Enter to return to Student Menu...")


def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    student = find_student(student_id)

    if student is not None:
        student_list.remove(student)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

    input("Press Enter to continue...")


def find_student(student_id):
    for student in student_list:
        if student.id == student_id:
            return student
    return None


def student_menu():
    while True:
        print("\n========== STUDENT MENU ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

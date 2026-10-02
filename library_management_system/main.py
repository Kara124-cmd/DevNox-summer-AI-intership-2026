import student_module
import librarian_module
import book_module


def main_menu():
    while True:
        print("\n======================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Student Management")
        print("2. Librarian Management")
        print("3. Book Management")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_module.student_menu()

        elif choice == "2":
            librarian_module.librarian_menu()

        elif choice == "3":
            book_module.book_menu()

        elif choice == "4":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice, please try again.")


try:
    main_menu()
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
except Exception as e:
    print("Unexpected error:", e)

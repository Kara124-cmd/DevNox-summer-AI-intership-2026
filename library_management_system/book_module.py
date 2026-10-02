import student_module


class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author

    def show(self):
        print("ID:", self.id)
        print("Title:", self.title)
        print("Author:", self.author)


book_list = []
borrow_list = []


def add_book():
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Title of Book: ").strip()
        author = input("Enter Name of Author: ").strip()

        if book_id == "" or title == "":
            print("Book ID and Title cannot be empty!")
            input("Press Enter to continue...")
            return

        if find_book(book_id) is not None:
            print("Book ID already exists!")
            input("Press Enter to continue...")
            return

        book = Book(book_id, title, author)
        book_list.append(book)

        print("Book added successfully!")
        input("Press Enter to continue...")

    except Exception as e:
        print("Error:", e)
        input("Press Enter to continue...")


def view_books():
    print("\n========== BOOK RECORDS ==========")
    print("Total Books:", len(book_list))

    if len(book_list) == 0:
        print("No books found.")
    else:
        for number, book in enumerate(book_list, start=1):
            print("\nBook", number)
            book.show()

            if is_book_borrowed(book.id):
                print("Status: Borrowed")
            else:
                print("Status: Available")

            print("---------------------------------")

    input("\nPress Enter to return to Book Menu...")


def delete_book():
    book_id = input("Enter Book ID to delete: ").strip()
    book = find_book(book_id)

    if book is None:
        print("Book not found!")
    elif is_book_borrowed(book_id):
        print("This book is currently borrowed.")
        print("Return it before deleting.")
    else:
        book_list.remove(book)
        print("Book deleted successfully!")

    input("Press Enter to continue...")


def find_book(book_id):
    for book in book_list:
        if book.id == book_id:
            return book
    return None


def is_book_borrowed(book_id):
    for record in borrow_list:
        if record["book_id"] == book_id:
            return True
    return False


def borrow_book():
    student_id = input("Enter Student ID: ").strip()
    book_id = input("Enter Book ID to borrow: ").strip()

    student = student_module.find_student(student_id)
    book = find_book(book_id)

    if student is None:
        print("Student not found!")
    elif book is None:
        print("Book not found!")
    elif is_book_borrowed(book_id):
        print("This book is already borrowed.")
    else:
        borrow_list.append({
            "student_id": student_id,
            "book_id": book_id
        })
        print(book.title, "has been borrowed by", student.name)

    input("Press Enter to continue...")


def return_book():
    student_id = input("Enter Student ID: ").strip()
    book_id = input("Enter Book ID to return: ").strip()

    for record in borrow_list:
        if record["student_id"] == student_id and record["book_id"] == book_id:
            borrow_list.remove(record)
            print("Book returned successfully!")
            input("Press Enter to continue...")
            return

    print("No matching borrow record found.")
    input("Press Enter to continue...")


def view_borrowed_books():
    print("\n========== BORROW RECORDS ==========")
    print("Total Borrow Records:", len(borrow_list))

    if len(borrow_list) == 0:
        print("No borrowed books found.")
    else:
        for number, record in enumerate(borrow_list, start=1):
            student = student_module.find_student(record["student_id"])
            book = find_book(record["book_id"])

            print("\nBorrow Record", number)
            print("Student ID:", record["student_id"])
            print("Student Name:", student.name if student else "Unknown")
            print("Book ID:", record["book_id"])
            print("Book Title:", book.title if book else "Unknown")
            print("----------------------------------")

    input("\nPress Enter to return to Book Menu...")


def book_menu():
    while True:
        print("\n========== BOOK MENU ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. View Borrow Records")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            view_borrowed_books()
        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")

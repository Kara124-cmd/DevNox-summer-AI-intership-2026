class Librarian:
    def __init__(self, librarian_id, name, contact):
        self.id = librarian_id
        self.name = name
        self.contact = contact

    def show(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Contact:", self.contact)


librarian_list = []


def add_librarian():
    try:
        librarian_id = input("Enter Librarian ID: ").strip()
        name = input("Enter Name: ").strip()
        contact = input("Enter Contact Number: ").strip()

        if librarian_id == "" or name == "":
            print("Librarian ID and Name cannot be empty!")
            input("Press Enter to continue...")
            return

        for librarian in librarian_list:
            if librarian.id == librarian_id:
                print("Librarian ID already exists!")
                input("Press Enter to continue...")
                return

        librarian = Librarian(librarian_id, name, contact)
        librarian_list.append(librarian)

        print("Librarian added successfully!")
        input("Press Enter to continue...")

    except Exception as e:
        print("Error:", e)
        input("Press Enter to continue...")


def view_librarians():
    print("\n========== LIBRARIAN RECORDS ==========")
    print("Total Librarians:", len(librarian_list))

    if len(librarian_list) == 0:
        print("No librarians found.")
    else:
        for number, librarian in enumerate(librarian_list, start=1):
            print("\nLibrarian", number)
            librarian.show()
            print("--------------------------------------")

    input("\nPress Enter to return to Librarian Menu...")


def delete_librarian():
    librarian_id = input("Enter Librarian ID to delete: ").strip()

    for librarian in librarian_list:
        if librarian.id == librarian_id:
            librarian_list.remove(librarian)
            print("Librarian deleted successfully!")
            input("Press Enter to continue...")
            return

    print("Librarian not found!")
    input("Press Enter to continue...")


def librarian_menu():
    while True:
        print("\n========== LIBRARIAN MENU ==========")
        print("1. Add Librarian")
        print("2. View Librarians")
        print("3. Delete Librarian")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_librarian()
        elif choice == "2":
            view_librarians()
        elif choice == "3":
            delete_librarian()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

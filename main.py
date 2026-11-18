import utils

def library_system():
    while True:
        print("Library Management System")
        print("1. View Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Edit Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            utils.view_books()
        elif choice == '2':
            utils.add_book()
        elif choice == '3':
            utils.remove_book()
        elif choice == '4':
            utils.update_book()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

library_system()



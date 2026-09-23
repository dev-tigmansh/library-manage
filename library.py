library = [[101, "To Kill a Mockingbird", "Harper Lee", "Available"],[102, "1984", "George Orwell", "Available"],[103, "The Great Gatsby", "F. Scott Fitzgerald", "Issued"]]

while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1) Display All Books")
    print("2) Add a Book")
    print("3) Issue a Book")
    print("4) Return a Book")
    print("5) Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == '1':
        print("LIBRARY BOOKS")
        for book in library:
            print("ID: " + str(book[0]) + " | Title: " + book[1] + " | Author: " + book[2] + " | Status: " + book[3])
    elif choice == '2':
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        
        # Append a new nested list directly
        library.append([book_id, title, author, "Available"])
        print("Book added successfully!")

    elif choice == '3':
        book_id = int(input("Enter Book ID to issue: "))
        found = False
        for book in library:
            if book[0] == book_id:
                found = True
                if book[3] == "Available":
                    book[3] = "Issued"
                    print(f"Issued", str(book[1]), "successfully.")
                else:
                    print(str(book[1]), 'is already issued.')
                break
        if not found:
            print("Book ID not found.")

    elif choice == '4':
        book_id = int(input("Enter Book ID to return: "))
        found = False
        for book in library:  
            if book[0] == book_id:
                found = True
                if book[3] == "Issued":
                    book[3] = "Available"
                    print("Returned", str(book[1]), "sucessfully.")
                else:
                    print(f"'{book[1]}' was not issued.")
                break
        if not found:
            print("Book ID not found.")

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please select between 1 and 5.")

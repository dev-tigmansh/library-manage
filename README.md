# library-manage system

A simple command-line program written in Python that lets a user manage a small library — view books, add new ones, issue them, and return them. Everything runs in a terminal using a menu the user picks from by typing a number.

// What it does:

When you run the program, you get a menu with five options:

1. **Display All Books** — prints every book in the library along with its ID, title, author, and current status (Available or Issued).
2. **Add a Book** — asks for an ID, title, and author, then adds it to the library as "Available".
3. **Issue a Book** — asks for a Book ID. If that book exists and is available, its status changes to "Issued". If it's already issued, or the ID doesn't exist, you get a message saying so.
4. **Return a Book** — same idea as issuing, but in reverse. If the book was issued, it goes back to "Available".
5. **Exit** — ends the program.

The menu keeps showing up in a loop until option 5 is chosen.

// How the data is stored:

The library is just a Python list of lists. Each book is stored as:

```
[book_id, title, author, status]
```

For example:

```python
[101, "To Kill a Mockingbird", "Harper Lee", "Available"]
```

There's no database or file involved — everything lives in memory while the program is running, and the list is preloaded with three books to start:

| ID  | Title                  | Author               | Status    |
|-----|-------------------------|------------------------|-----------|
| 101 | To Kill a Mockingbird   | Harper Lee             | Available |
| 102 | 1984                    | George Orwell          | Available |
| 103 | The Great Gatsby        | F. Scott Fitzgerald    | Issued    |

// Running it:

You just need Python 3 installed. Then run:

```
python library.py
```

(or whatever you've named the file), and follow the on-screen menu.

//  Notes/things to keep in mind:

- Book IDs are expected to be whole numbers — entering text where an ID is expected will crash the program, since there's no input validation.
- Issuing/returning is matched purely by Book ID, so IDs should be unique when adding new books (the program doesn't currently check for duplicates).
- Data isn't saved anywhere — once you exit, everything resets back to the original three books next time you run it.

// Possible improvements:

- Input validation (e.g., handling non-numeric IDs gracefully instead of crashing).
- Checking for duplicate IDs when adding a book.
- Saving/loading the library to a file (like a CSV or JSON) so data persists between runs.
- Search functionality (by title or author).

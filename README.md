# Book-Store-Database-Application
## Description
This project is a Book Management System built using Python and the Tkinter library. It allows users to manage a collection of books by providing functionality to view, search, add, update, and delete book records stored in a SQLite database. The graphical user interface enables easy management of the book information, such as title, author, year of publication, and ISBN.

![Demo](https://github.com/nahili-ansha/Book-Store-Database-Application/blob/main/Book_Store_Database_APP.png
)

## Features
- **View All Records:** Users can view all book entries stored in the database.
- **Search for Books:** Users can search for books by title, author, year, or ISBN.
- **Add New Book:** New book entries can be added to the database.
- **Update Book Details:** Existing book records can be updated.
- **Delete Book Entry:** Allows deletion of selected book records.
- **Interactive UI:** The graphical user interface is created using Tkinter for a seamless user experience.

## Technologies

- **Python 3.x:**
  - The main programming language used to develop the application.
  - Provides the runtime environment for the system.

- **Tkinter:**
  - Standard Python library for creating graphical user interfaces (GUI).
  - Used to build an interactive UI for the Book Management System.
  - Allows the creation of widgets like buttons, labels, and entry boxes.

- **SQLite:**
  - A lightweight, self-contained SQL database engine.
  - Used to store, retrieve, and manage book information.

## Project Structure
- **frontend.py**: The main script containing the graphical user interface and interaction logic for the Book Management System.
- **backend.py**: Handles all database operations, including connecting to the database, performing CRUD operations (Create, Read, Update, Delete), and other functions related to data handling.

## Usage
1. Ensure that both `frontend.py` and `backend.py` are in the same directory.
2. Run the `frontend.py` script:
   ```sh
   python frontend.py

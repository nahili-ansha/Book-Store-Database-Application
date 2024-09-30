import sqlite3

# Database connection
def connect():
    # Establish a connection to the SQLite database 
    conn = sqlite3.connect("books.db")

     # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Create the 'book' table if it doesn't exist, with columns: id, title, author, year, and isbn
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year text, isbn integer)")

    # Commit the changes to the database
    conn.commit()

     # Close the connection to the database
    conn.close()

# Add Entry 
def insert(title, author, year, isbn):
     # Establish a connection to the SQLite database 
    conn = sqlite3.connect("books.db")

     # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Insert a new record into the 'book' table with the provided title, author, year, and isbn values
    # The 'NULL' allows SQLite to auto-generate the 'id' as it's the primary key
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))

    # Commit the changes to the database
    conn.commit()

     # Close the connection to the database
    conn.close()

# View All
def view():
     # Establish a connection to the SQLite database 
    conn = sqlite3.connect("books.db")

     # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Select and retrieve all records from the 'book' table
    cur.execute("SELECT * FROM book ")

    # Fetch all rows returned
    rows = cur.fetchall()

    # Close the connection to the database
    conn.close()

    # return the rows
    return rows

# Search Entry
def search(title = "", author = "", year = "", isbn = ""):
    # Establish a connection to the SQLite database 
    conn = sqlite3.connect("books.db")

     # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Select and retrieve all records from the 'book' table
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))

    # Fetch all rows returned
    rows = cur.fetchall()

    # Close the connection to the database
    conn.close()

    # return the rows
    return rows

# Delete Entry
def delete(id):
    # Establish a connection to the SQLite database 
    conn = sqlite3.connect("books.db")

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Delete the row with specified id
    cur.execute("DELETE FROM book WHERE id=?", (id, ))

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()

# Update Entry
def update(id, title, author, year, isbn):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect("books.db")

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Update the row with specified id
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()




connect()


#insert("The Book", "John David", 1967, 9131231686)
#delete(2)
#update(1,"The moon", "John Smooth", 1917, 99999)
#print(view())
#print(search(author = "John Smith"))
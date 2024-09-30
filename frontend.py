"""
A program that stores book information
Title, Author
Year, ISBN

Users can:

View all records
Search an entry
Add entry
Update entry
Delete entry
Close
"""
from tkinter import *
import backend

# this function will expect "event" to be passed
def get_selected_row(event):
    index = list1.curselection()[0]
    print(index)


# view all
def view_command():
    # iterate through the list of tuples or rows returned by view()
    list1.delete(0,END)
    for row in backend.view():
        # add them to the list box
        list1.insert(END, row)

# search
def search_command():
    list1.delete(0,END)
    # iterate through the list of tuples returned by search()
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

# Add Entry
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


window = Tk()
window.title("Book Store")
window.configure(bg = "lightblue")

# Labels
label1 = Label(window, text = "Title", bg = "lightblue")
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Author", bg = "lightblue")
label2.grid(row = 0, column = 2)

label3 = Label(window, text = "Year", bg = "lightblue")
label3.grid(row = 1, column = 0)

label4 = Label(window, text = "ISBN", bg = "lightblue")
label4.grid(row = 1, column = 2)

# Entries
title_text = StringVar()
entry1 = Entry(window, textvariable = title_text)
entry1.grid(row = 0, column = 1)

author_text = StringVar()
entry2 = Entry(window, textvariable = author_text)
entry2.grid(row = 0, column = 3)

year_text = StringVar()
entry3 = Entry(window, textvariable = year_text)
entry3.grid(row = 1, column = 1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable = isbn_text)
entry4.grid(row = 1, column = 3)

# ListBox
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2 )

# ScrollBar
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = scrollbar1.set)
scrollbar1.configure(command = list1.yview)

# blind function takes event type & function to bind with
list1.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
b1 = Button(window, text = "View all", width = 12, activebackground= "blue", cursor = "hand1", command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, activebackground= "blue", cursor = "hand1", command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, activebackground= "blue", cursor = "hand1", command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12, activebackground= "blue", cursor = "hand1")
b4.grid(row = 5, column = 3 )

b5 = Button(window, text = "Delete", width = 12, activebackground= "blue", cursor = "hand1")
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, activebackground= "blue", cursor = "hand1")
b6.grid(row = 7, column = 3)


window.mainloop()


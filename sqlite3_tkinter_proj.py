''' INTERACTIVE PLANNER -- July 2022
--- create an application that saves notes to a database & displays notes
--- expand into a more full featured calendar
    Clawson, Carrillo, Soun, Miller July 2022
'''

import tkinter as tk
from tkinter import WORD
from tkinter import Menu
import sqlite3
from datetime import datetime

connection = sqlite3.connect('sqlite3_tkinter_proj.db')
cursor = connection.cursor()

# need to add handling to check if db file exists or not
# if already exists, use the next line to create a SQLite3 TABLE
# cursor.execute('CREATE TABLE entries (id INTEGER PRIMARY KEY, date TEXT, note TEXT)')


# create main window (root window)
root = tk.Tk(className='Interactive Planner BETA')
root.geometry("500x500")

#--- FRAME WIDGETS ---
# frames will be displayed based on menu navigations
# need to find best way to move between frames. modularize ? build a function?
record_frame = tk.Frame(root, bg='#F6EED2')
splash_frame = tk.Frame(root, bg='#F6EED2')
helpp_frame = tk.Frame(root, bg='orange')
about_frame = tk.Frame(root, bg='yellow')


#--- MENU BAR WIDGET ---
# menu bar functions
def destroy(): # closes root window
    root.destroy()

def splash(): # show previously taken notes here
    record_frame.forget()
    splash_frame.pack(expand=True, fill=tk.BOTH)
def new(): # create a new note
    splash_frame.forget()
    record_frame.pack(expand=True, fill=tk.BOTH)

def search():
    print("insert search logic via SQL commands")

def helpp():
    print("open new window for help? perhaps a website ")

def about():
    print("about")

# create the file menu 
menubar = tk.Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="My Notes", underline=0, command=splash)
filemenu.add_command(label="New", underline=0, command=new)
filemenu.add_command(label="Search", underline=0, command=search)
filemenu.add_separator()
filemenu.add_command(label="Exit", underline=1, command=destroy)
menubar.add_cascade(label="File", menu=filemenu, underline=0)

# create the help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", underline=0, command=helpp)
helpmenu.add_command(label="About...", underline=0, command=about)
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)
root.config(menu=menubar)


#--- TEXT WIDGET ---
message="Insert note or event here ..."
text_box = tk.Text(record_frame, height=0, width=0, wrap=WORD)
text_box.insert('end', message)
text_box.config(state='normal')
text_box.pack(expand=True, fill=tk.BOTH)


#--- BUTTON WIDGET ---
def submit(): # submit a note
    # do shit here, called below using 'command=submit' parameter
    date = datetime.now()
    data = text_box.get(1.0, 'end')
    if len(data) <=1: #tkinter seems to adda \n by default, rly annoying ??
        print("No data to submit")
    else:
        cursor.execute('INSERT INTO entries(date, note) VALUES(?, ?)', (date, data,))
        connection.commit()
        text_box.delete(1.0, 'end')
        record_frame.forget()
        splash_frame.pack(expand=True, fill=tk.BOTH)
        print("A note was submitted")

    
def cancel(): # cancel note-taking
    record_frame.forget()
    splash_frame.pack(expand=True, fill=tk.BOTH)


submit_button = tk.Button(record_frame, text='Submit', command=submit)
cancel_button = tk.Button(record_frame, text='Cancel', command=cancel)
submit_button.pack()
cancel_button.pack()


# pack splash_frame upon startup
# create label for splash page
splash_label = tk.Label(splash_frame, text='Welcome to this note-taking aplication, comrade.')
splash_frame.pack(expand=True, fill=tk.BOTH)
splash_label.pack(pady=10)


#--- MAIN LOOP --- displays the window continuously
root.mainloop()

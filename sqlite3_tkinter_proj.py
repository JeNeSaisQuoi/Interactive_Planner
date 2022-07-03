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



#--- MENU BAR ---

def destroy(): # closes root window
    root.destroy()
    
def search():
    return "insert search logic via SQL commands"

def helpp():
    return "open new window for help? perhaps a website "

def about():
    return "about"

menubar = tk.Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Search", command=search)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=destroy)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpp)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)


#--- TEXT WIDGET ---
message="Hey fuck you"
text_box = tk.Text(root, height=0, width=0, wrap=WORD)
text_box.insert('end', message)
text_box.config(state='normal')
text_box.pack(expand=True, fill=tk.BOTH)


#--- BUTTON WIDGET ---
def submit():
    # do shit here, called below using 'command=submit' parameter
    date = datetime.now()
    data = text_box.get(1.0, 'end')
    if len(data) <=1: #tkinter seems to adda \n by default, rly annoying ??
        print("No data found to submit")
    else:
        cursor.execute('INSERT INTO entries(date, note) VALUES(?, ?)', (date, data,))
        connection.commit()
        text_box.delete(1.0, 'end')
        print("A note was submitted")

button = tk.Button(root, text='Submit', command=submit)
button.pack()

#--- MAIN LOOP --- displays the window continuously
root.mainloop()

''' INTERACTIVE PLANNER -- July 2022
--- create an application that saves notes to a database & displays notes
--- expand into a more full featured calendar
    Clawson, Carrillo, Soun, Miller July 2022
'''

import tkinter as tk
from tkinter import WORD
import sqlite3
from datetime import datetime

connection = sqlite3.connect('sqlite3_tkinter_proj.db')
cursor = connection.cursor()

# need to add handling to check if db file exists or not
# if it doesn't exist, use the next line to create a SQLite3 TABLE
# cursor.execute('CREATE TABLE entries (id INTEGER PRIMARY KEY, date TEXT, note TEXT)')


# create main window (root window)
root = tk.Tk(className='Interactive Planner BETA')
root.geometry("500x500")

# create textbox widget
message="Hey fuck you"
text_box = tk.Text(root, height=0, width=0, wrap=WORD)
text_box.insert('end', message)
text_box.config(state='normal')
text_box.pack(expand=True, fill=tk.BOTH)

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
        

# create button widget
button = tk.Button(root, text='Submit', command=submit)
button.pack()

# run the main loop to display the window continuously
root.mainloop()

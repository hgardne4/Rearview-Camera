"""
Henry Gardner
Rear-view Camera for any car

Dislpay file that deals with the user interface

Notes on Tkinter (from documentation):
    - each widgit is represented by a Python object
    - there is a widgit hierarchy 
    - NEED to manually add each widgit to the frame using geometery manager like .grid()

"""

from tkinter import *
from tkinter import ttk
import gpsd
import gps
import os
import json

# initialize Tk and the Tcl interpreter, in addition to creating the root "toplevel" window
root = Tk()
root.geometry("500x500")
# create the frame widget, which sits inside the root window
frame = ttk.Frame(root, padding=10)
frame.pack()

mmenu = Menu(frame)
mmenu.add_command(label="Exit", command = root.destroy)

root.config(menu = mmenu)

gpsd.connect()
output = gps.get_gps_data()
print(json.dumps(output, indent = 2))
ttk.Label(frame, text="hello").grid(column=0,row=0)
#ttk.Button(frame, text="exit", command=root.destroy).grid(column=1,row=1)
root.mainloop()


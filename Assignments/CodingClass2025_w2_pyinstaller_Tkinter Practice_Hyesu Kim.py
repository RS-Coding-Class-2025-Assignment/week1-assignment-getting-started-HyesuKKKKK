
#W2 Pyinstaller Practice : simple GUI
#pip install pyinstaller
#pyinstaller --version

import tkinter as tk
from tkinter import ttk

def example_function():
    print("You has submitted your name!")
root = tk.Tk()
root.title("Tkinter Example")

#Label
ttk.Label(root, text="Enter your name:").grid(row=0, column=0, padx=5, pady=5, sticky="W" )

#Entry field
name_entry=ttk.Entry(root,width=30)
name_entry.grid(row=0, column=1,padx=5, pady=5)

#Button
ttk.Button(root, text="Submit", command=example_function).grid(row=0,column=2,padx=5,pady=5)

root.mainloop()
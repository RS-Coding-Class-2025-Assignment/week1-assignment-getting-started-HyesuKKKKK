#%%#
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Celcius to Fahrenheit")
root.geometry("400x200")

def ConvertT(C):
    C =float(C)
    f = C * 9/5 + 32
    return f

def Convert():
    C = Entry_Cels.get()
    result = ConvertT(C)
    Label_res.config(text=f"Result: {result}˚F")

Label_Cels = tk.Label(root, text="Enter Celsius:")
Label_Cels.grid(row=0, column=0, padx= 5, pady= 5)
Entry_Cels = tk.Entry(root, width=20)
Entry_Cels.grid(row=0, column=1, padx=5, pady=5)
Button_Conv = tk.Button(root, text="Convert", command=Convert)
Button_Conv.grid(row=1, column=0, columnspan=2, pady=10)

Label_res = tk.Label(root, text=f"Result:_______˚F")
Label_res.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()

# %%

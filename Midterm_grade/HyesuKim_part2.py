#%%
import tkinter as tk
from tkinter import ttk
import time
import threading

root = tk.Tk()
root.title("Progressbar_Hyesu")
root.geometry("400x150")

stop_thread=False

progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progressbar.pack()
label_progress= tk.Label(root, text="0%")
label_progress.pack(padx=5, pady=5)

def start_progress():
    for i in range(101):
        global stop_thread
        if stop_thread:
            break
        progressbar["value"]=i
        label_progress.config(text=f"{i}%")
        time.sleep(1.2)
        root.update()
        
def start():
    global stop_thread
    stop_thread = False
    progressbar["value"]=0
    t = threading.Thread(target = start_progress)
    t.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop():
    global stop_thread
    stop_thread = True
    progressbar["value"]=0
    t = threading.Thread(target = start_progress)
    t.start()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)



start_button = tk.Button(root, text="Start", command=start)
start_button.pack(padx=5, pady=5)
stop_button = tk.Button(root, text="Stop", command = stop)
stop_button.pack(padx=5, pady=5)


start_button.config(state=tk.NORMAL)
stop_button.config(state=tk.DISABLED)



root.mainloop()


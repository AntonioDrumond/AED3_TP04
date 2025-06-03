import tkinter as tk
from tkinter import ttk


def check_input():
    var = var_entry.get()
    print(var)


# Define screens
## Root
root = tk.Tk()
root.title("Visualizador Hash Extensivel")
root.geometry("100x300+500+100")

# Define buttons
close = tk.Button(root, text="Quit", command=root.destroy)
close.pack()

var_entry = ttk.Entry(root)
var_entry.pack()

tk.Button(
    root,
    text="print",
    command=check_input,
    width=18,
).pack(pady=10, padx=30, fill="x")

# Initialize main screen
root.mainloop()

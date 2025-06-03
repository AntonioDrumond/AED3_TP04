import tkinter as tk
from tkinter import ttk


def insert_key():
    var = var_entry.get()
    var_entry.delete(0, 10000)
    try:
        var = int(var)
    except:
        print("ERRO: Input não é um número")
    else:
        print(f"inserting key: {var}")


def remove_key():
    var = var_entry.get()
    var_entry.delete(0, 10000)
    try:
        var = int(var)
    except:
        print("ERRO: Input não é um número")
    else:
        print(f"removing key: {var}")


# Define screens
## Root
root = tk.Tk()
root.title("Visualizador Hash Extensivel")
root.geometry("100x300+500+100")

# Define buttons
close = tk.Button(root, text="Quit", command=root.destroy)

var_entry = ttk.Entry(root)

ins_button = tk.Button(
    root,
    text="Inserir",
    command=insert_key,
)

rm_button = tk.Button(
    root,
    text="Remover",
    command=remove_key,
)

# Pack buttons
var_entry.pack()
ins_button.pack()
rm_button.pack()
close.pack(side=tk.BOTTOM)

# Initialize main screen
root.mainloop()

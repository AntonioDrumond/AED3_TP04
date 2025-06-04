import tkinter as tk
from tkinter import ttk


def destroy_all():
    root.destroy()
    buckets.destroy()
    directory.destroy()


def insert_key():
    trem = tk.Label(
        buckets,
        text=f"cont: {var_entry.get()}",
    )
    trem.pack()
    var_entry.delete(0, 10000)


def insert_key_te():
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
root.geometry("100x300+300+100")
## Directory
directory = tk.Tk()
directory.title("Diretório")
directory.geometry("200x400+800+150")
## Buckets
buckets = tk.Tk()
buckets.title("Buckets")
buckets.geometry("500x200+1300+150")

# Define labels
title = tk.Label(root, text="Visualizador\nde Hash\nExtensivel")

# Define buttons

close = tk.Button(
    root,
    text="Sair",
    # command=root.destroy
    command=destroy_all,
)

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
title.pack()
var_entry.pack()
ins_button.pack(fill=tk.X, padx=5, pady=5)
rm_button.pack(fill=tk.X, padx=5)
close.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

# Initialize main screen
root.mainloop()
buckets.mainloop()
directory.mainloop()

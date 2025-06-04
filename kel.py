import tkinter as tk
from tkinter import ttk, messagebox

class Table:
    
    """Grade de Entry-widgets que pode ser modificada em tempo de execução."""
    def __init__(self, master, data, headers=None):
        self.master = master
        self.data = data  # Store original data for reference
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows else 0
        self.cells = []  # matriz de Entry
        self.headers = headers
        
        self.create_table()
        
    def create_table(self):

        # Clear existing widgets
        for widget in self.master.winfo_children():
            widget.destroy()
            
        # Configure grid weights
        for i in range(self.rows + 1):  # +1 for header row
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.master.grid_columnconfigure(j, weight=1)

        # Add headers if provided
        if self.headers:
            for j, header in enumerate(self.headers):
                lbl = tk.Label(
                    self.master, text=header, 
                    font=("Arial", 12, "bold"),
                    relief="ridge", 
                    bg="#f0f0f0",
                    padx=5, pady=2
                )
                lbl.grid(row=0, column=j, sticky="nsew", padx=1, pady=1)
            row_offset = 1  # Start data rows after header
        else:
            row_offset = 0
            
        # Add data rows
        self.cells = []  # Reset cells list
        for i, row in enumerate(self.data):
            linha_widgets = []
            for j, value in enumerate(row):
                e = tk.Entry(
                    self.master, width=15, fg="blue",
                    font=("Arial", 12, "bold"),
                    justify="center"
                )
                e.grid(row=i + row_offset, column=j, sticky="nsew", padx=1, pady=1)
                e.insert(tk.END, value)
                linha_widgets.append(e)
            self.cells.append(linha_widgets)
    
    def add_row(self, row_data=None):
        """Add a new row to the table"""
        if row_data is None:
            # Create empty row if no data provided
            row_data = [""] * self.cols
            
        self.data.append(row_data)
        self.rows += 1
        self.create_table()  # Rebuild the table
        
    def set_value(self, row, col, value):
        """Substitui o conteúdo da célula [row][col] (índices base-1 para o usuário)."""
        if not (1 <= row <= self.rows and 1 <= col <= self.cols):
            raise IndexError("Linha ou coluna fora do intervalo.")
        cell = self.cells[row-1][col-1]
        cell.config(state="normal")      # permite edição
        cell.delete(0, tk.END)
        cell.insert(tk.END, value)
        cell.config(state="readonly")    # trava novamente
        
#######################################################################################      
        
def main():
    
    dados = [
        (128, 1, "Raj",       "Mumbai", 19, 20),
        (256, 2, "Aaryan",    "Pune",   18, 21),
        (384, 3, "Vaishnavi", "Mumbai", 20, 50),
        (512, 4, "Rachna",    "Mumbai", 21, 40),
        (640, 5, "Shubham",   "Delhi",  21, 8),
    ]

    root = tk.Tk()
    root.title("Visualizador Hash Extensível")
    root.geometry("260x360+300+120")
    
    dir = tk.Toplevel(root)
    dir.title("Diretório")
    dir.geometry("260x360+590+120")

    buckets = tk.Toplevel(root)
    buckets.title("Buckets")
    buckets.geometry("620x280+880+120")

    # ---------------- tabela ----------------
    headers = ["Endereço", "P'", "N", "Chave 1", "Chave 2", "Chave 3"]
    tabela = Table(buckets, dados, headers=headers)

    # ---------------- controles ----------------
    frm_controls = ttk.LabelFrame(root, text="Inserir valor")
    frm_controls.pack(fill="x", padx=8, pady=8)

    ttk.Label(frm_controls, text="Linha:").grid(row=0, column=0, padx=2, pady=4, sticky="e")
    spin_row = tk.Spinbox(frm_controls, from_=1, to=tabela.rows, width=5, justify="center")
    spin_row.grid(row=0, column=1, padx=2, pady=4)

    ttk.Label(frm_controls, text="Coluna:").grid(row=0, column=2, padx=2, pady=4, sticky="e")
    spin_col = tk.Spinbox(frm_controls, from_=1, to=tabela.cols, width=5, justify="center")
    spin_col.grid(row=0, column=3, padx=2, pady=4)

    ttk.Label(frm_controls, text="Valor:").grid(row=1, column=0, padx=2, pady=4, sticky="e")
    entry_val = ttk.Entry(frm_controls, width=18)
    entry_val.grid(row=1, column=1, columnspan=3, padx=2, pady=4, sticky="we")

    def inserir_valor():
        try:
            linha   = int(spin_row.get())
            coluna  = int(spin_col.get())
            valor   = entry_val.get()
            if valor == "":
                raise ValueError("Valor vazio")
            tabela.set_value(linha, coluna, valor)
            entry_val.delete(0, tk.END)
        except (ValueError, IndexError) as err:
            messagebox.showerror("Erro", f"Entrada inválida:\n{err}")

    ttk.Button(frm_controls, text="Inserir", command=inserir_valor)\
        .grid(row=2, column=0, columnspan=4, pady=(6, 4), sticky="we")

    def add_new_row():
        tabela.add_row()
        spin_row.config(to=tabela.rows)
        
    ttk.Button(root, text="Adicionar Linha", command=add_new_row)\
        .pack(fill="x", padx=8, pady=4)

    ttk.Button(root, text="Sair", command=root.destroy)\
        .pack(fill="x", padx=8, pady=(0, 8))

    root.mainloop()

if __name__ == "__main__":
    main()


#ANOTACOES
#You can also add pre-filled rows by passing data to add_row(), like:
#tabela.add_row([6, "New Name", "New City", 25])
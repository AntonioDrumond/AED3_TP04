import tkinter as tk
from tkinter import ttk, messagebox
import ExtendibleHash as EH;
from table import Table

#######################################################################################      

def main():

    he = EH.ExtendibleHash() 

    # ---------------- Windows ----------------

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
    tabela = Table(buckets, headers=headers)

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

    def mandar_pra_tabela(x, y, valor):
        try:
            linha   = int(x)
            coluna  = int(y)
            if valor == "":
                raise ValueError("Valor vazio")
            tabela.set_value(linha, coluna, valor)
            entry_val.delete(0, tk.END)
        except (ValueError, IndexError) as err:
            messagebox.showerror("Erro", f"Entrada inválida:\n{err}")

    def inserir_valor():
        valor   = entry_val.get()
        try:
            valor = int(valor)
        except:
            messagebox.showerror("Erro", f"Entrada inválida:")
        else:
            # aqui descobrir as coordenadas
            mandar_pra_tabela(1,1, valor)

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

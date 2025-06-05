import tkinter as tk
from tkinter import ttk, messagebox
import ExtendibleHash as EH
from table import Table

##################################### FUNÇÕES #####################################

def center_windows(root, dir, buckets):
    """Center all windows on screen with equal spacing"""
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Window dimensions
    root_width = 180
    root_height = 400
    dir_width = 350
    dir_height = 400
    buckets_width = 600
    buckets_height = 400
    
    # Calculate total width needed
    total_width = root_width + dir_width + buckets_width
    spacing = (screen_width - total_width) // 4  # Equal spacing on sides and between windows
    
    # Calculate positions
    root_x = spacing
    root_y = (screen_height - root_height) // 2
    
    dir_x = root_x + root_width + spacing
    dir_y = root_y
    
    buckets_x = dir_x + dir_width + spacing
    buckets_y = root_y
    
    # Set geometries
    root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")
    dir.geometry(f"{dir_width}x{dir_height}+{dir_x}+{dir_y}")
    buckets.geometry(f"{buckets_width}x{buckets_height}+{buckets_x}+{buckets_y}")

##################################### MAIN #####################################    

def main():

    he = EH.ExtendibleHash() 

    # ---------------- Windows ----------------

    root = tk.Tk()
    root.title("Visualizador Hash Extensível")
    #root.geometry("260x360+300+120")

    dir = tk.Toplevel(root)
    dir.title("Diretório")
    #dir.geometry("260x360+590+120")

    buckets = tk.Toplevel(root)
    buckets.title("Buckets")
    #buckets.geometry("620x280+880+120")
    
    # Center and size all windows
    center_windows(root, dir, buckets)

    # ---------------- tabelaS ----------------
    
    #BUCKETS
    headersB = ["Endereço", "P'", "N", "Chave 1", "Chave 2", "Chave 3"]
    tabela = Table(buckets, headers=headersB)
    tabela.add_row();
    
    #DIRETÓRIO
    headersD = ["Hash", "Endereço"]
    tabela_dir = Table(dir, headers=headersD)
    tabela_dir.add_row();

    # ---------------- controles ----------------
    
    frm_controls = ttk.LabelFrame(root, text="Inserir valor")
    frm_controls.pack(fill="x", padx=8, pady=8)
    
    # Add a label to display "Profundidade global = X" in the dir window
    profundidade_label = ttk.Label(dir, text="Profundidade global: 0", anchor="center", font=("Arial", 12))
    profundidade_label.grid(row=0, column=0, pady=10, sticky="n")  # Use grid instead of pack

    def update_profundidadeDIR():
        # Update the label text dynamically based on the variable X
        X = 5
        profundidade_label.config(text=f"Profundidade global: {X}")

    #ttk.Label(frm_controls, text="Linha:").grid(row=0, column=0, padx=2, pady=4, sticky="e")
    #spin_row = tk.Spinbox(frm_controls, from_=1, to=tabela.rows, width=5, justify="center")
    #spin_row.grid(row=0, column=1, padx=2, pady=4)

    #ttk.Label(frm_controls, text="Coluna:").grid(row=0, column=2, padx=2, pady=4, sticky="e")
    #spin_col = tk.Spinbox(frm_controls, from_=1, to=tabela.cols, width=5, justify="center")
    #spin_col.grid(row=0, column=3, padx=2, pady=4)

    ttk.Label(frm_controls, text="Valor:").grid(row=1, column=0, padx=2, pady=4, sticky="e")
    entry_val = ttk.Entry(frm_controls, width=18)
    entry_val.grid(row=1, column=1, columnspan=3, padx=2, pady=4, sticky="we")

    #def mandar_pra_tabela(x, y, valor):
        #try:
            #linha   = int(x)
            #coluna  = int(y)
            #if valor == "":
                #raise ValueError("Valor vazio")
            #tabela.set_value(linha, coluna, valor)
            #entry_val.delete(0, tk.END)
        #except (ValueError, IndexError) as err:
            #messagebox.showerror("Erro", f"Entrada inválida:\n{err}")

    def inserir_valor():
        valor = entry_val.get()
        try:
            valor = int(valor)
        except:
            messagebox.showerror("Erro", f"Entrada inválida:")
        else:
            he.insert(valor);
            tab = formatar_tabela();
            tabela.update_data(tab);
            print(he)
            update_profundidadeDIR()
    
    def formatar_tabela():

        pos = he.getRefs();

        res = []*len(pos);

        i = 0;
        
        for pi in pos:

            lis = [];

            if (type(pi) == tuple):
                pi = pi[0];

            bk = he.dir[pi];
            n = bk.i;
            p = bk.local_depth;

            lis.append(i);
            lis.append(p);
            lis.append(n);

            for reg in bk.regs:
                lis.append((reg));
        
            i += 1;
            res.append(lis);

        return (res);

    ttk.Button(frm_controls, text="Inserir", command=inserir_valor)\
            .grid(row=2, column=0, columnspan=4, pady=(6, 4), sticky="we")

    def add_new_row():
        tabela.add_row()
        spin_row.config(to=tabela.rows)

    #ttk.Button(root, text="Adicionar Linha", command=add_new_row)\
            #.pack(fill="x", padx=8, pady=4)

    ttk.Button(root, text="Sair", command=root.destroy)\
            .pack(fill="x", padx=8, pady=(0, 8))

    root.mainloop()

if __name__ == "__main__":
    main()


#ANOTACOES
#You can also add pre-filled rows by passing data to add_row(), like:
#tabela.add_row([6, "New Name", "New City", 25])

import tkinter as tk
from tkinter import ttk, messagebox
import ExtendibleHash as EH
from table import Table

##################################### TAMANHO E POSIÇÃO DAS JANELAS #####################################

def center_windows(root, dir, buckets):
    """Center all windows on screen with equal spacing"""
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Window dimensions
    root_width = 180
    root_height = 400
    dir_width = 283
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
    
    root_header_frame = ttk.Frame(root)
    root_header_frame.pack(fill="x", padx=8, pady=(8, 0))
    
    hash_label = ttk.Label(
        root_header_frame,
        text="Hash: - % 2^p = -",  # Initial state
        anchor="center",
        font=("Arial", 12)
    )
    hash_label.pack(pady=10)

    dir = tk.Toplevel(root)
    dir.title("Diretório")

    buckets = tk.Toplevel(root)
    buckets.title("Buckets")
    
    # Center and size all windows
    center_windows(root, dir, buckets)
    
    # Create a frame in dir window to hold the label (won't be destroyed)
    dir_header_frame = ttk.Frame(dir)
    dir_header_frame.grid(row=0, column=0, sticky="nsew")
    
    # Global depth label - stays in the header frame
    profundidade_label = ttk.Label(
        dir_header_frame, 
        text="Profundidade global: 0", 
        anchor="center", 
        font=("Arial", 12)
    )
    profundidade_label.pack(pady=10)
    
    # Create a frame for the directory table (below the header)
    dir_table_frame = ttk.Frame(dir)
    dir_table_frame.grid(row=1, column=0, sticky="nsew")

    # ---------------- tabelaS ----------------
    
    #BUCKETS
    headersB = ["Endereço", "P'", "N", "Chave 1", "Chave 2", "Chave 3"]
    tabela = Table(buckets, headers=headersB)
    tabela.add_row();
    
    #DIRETÓRIO
    headersD = ["Hash", "Endereço"]
    tabela_dir = Table(dir_table_frame, headers=headersD)
    tabela_dir.add_row();

    # ---------------- INSERÇÃO ----------------
    
    def update_profundidadeDIR():
        x = he.dir_size
        profundidade_label.config(text=f"Profundidade global: {x}")
    
    frm_controls = ttk.LabelFrame(root, text="Inserir valor")
    frm_controls.pack(fill="x", padx=8, pady=8)

    ttk.Label(frm_controls, text="Valor:").grid(row=1, column=0, padx=2, pady=4, sticky="e")
    entry_val = ttk.Entry(frm_controls, width=18)
    entry_val.grid(row=1, column=1, columnspan=3, padx=2, pady=4, sticky="we")
            
    def inserir_valor():
        valor = entry_val.get()
        try:
            valor = int(valor)
            
            resultado_hash = he.hash(valor)
            
            he.insert(valor)
            tab = formatar_tabela()
            tabela.update_data(tab)
            update_profundidadeDIR()
            
            try:
                formatted_dir = formatarDIR()
                tabela_dir.update_data(formatted_dir)
            except Exception as e:
                messagebox.showerror("Erro DIR", f"Erro ao atualizar diretório: {str(e)}")
                
            hash_label.config(text=f"Hash: {valor} % 2^p = {resultado_hash}")
            
            entry_val.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida: deve ser um número inteiro")
    
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
    
    def formatarDIR():
        bucket_numbers = he.formatedRefs()  
        hashs = list(range(len(bucket_numbers)))
        # Convert zip to list of lists
        return [[h, b] for h, b in zip(hashs, bucket_numbers)]

    ttk.Button(frm_controls, text="Inserir", command=inserir_valor)\
            .grid(row=2, column=0, columnspan=4, pady=(6, 4), sticky="we")    

    # ---------------- BUSCA ----------------
    
    def buscar_valor():
        #mostrar a hash do valor
        #dar um hilight na linha do diretorio
        #dar um hilight na linha do bucket
        #mostrar caixa de aviso se achar, mostrando numero do bucket e posicao da chave
        #mostrar caixa de aviso se não achar, mostrando que não foi encontrado
        x = 2
    
    frm_controls = ttk.LabelFrame(root, text="Buscar valor")
    frm_controls.pack(fill="x", padx=8, pady=8)
    
    ttk.Label(frm_controls, text="Valor:").grid(row=1, column=0, padx=2, pady=4, sticky="e")
    entry_search = ttk.Entry(frm_controls, width=18)
    entry_search.grid(row=1, column=1, columnspan=3, padx=2, pady=4, sticky="we")
    
    ttk.Button(frm_controls, text="Buscar", command=buscar_valor)\
            .grid(row=2, column=0, columnspan=4, pady=(6, 4), sticky="we")
    
    # ---------------- OUTROS ----------------
    
    ttk.Button(root, text="Sair", command=root.destroy)\
            .pack(fill="x", padx=8, pady=(0, 8))
    
    root.mainloop()

if __name__ == "__main__":
    main()
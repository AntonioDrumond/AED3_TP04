import tkinter as tk

class Table:

    """Grade de Entry-widgets que pode ser modificada em tempo de execução."""
    def __init__(self, master, headers=None):
        self.master = master
        # self.data = data  # Store original data for reference
        self.data = []
        # self.rows = len(data)
        self.rows = 1
        # self.cols = len(data[0]) if self.rows else 0
        self.cols = 6
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
        

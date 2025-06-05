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
        self.cols = len(headers) if (headers) else 6
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
    
    def update_data(self, new_data):
        """
        Completely replaces table data with new list of lists
        Args:
            new_data: List of lists with the new row data
        """
        # Validate input is list of lists
        if not all(isinstance(row, list) for row in new_data):
            raise TypeError("Input must be a list of lists")
            
        self.data = [row.copy() for row in new_data]  # Create copy to avoid reference issues
        self.rows = len(self.data)
        
        # Update column count if we have data
        if self.rows > 0:
            self.cols = len(self.data[0])
            # Validate all rows have same number of columns
            if not all(len(row) == self.cols for row in self.data):
                raise ValueError("All rows must have the same number of columns")
        elif self.headers:
            self.cols = len(self.headers)
            
        self.create_table()  # Rebuild the table

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

    def highlight_row(self, row_index, color="green", duration=2500):
        """Highlight a specific row temporarily"""
        # Adjust for header row if present
        adjusted_row = row_index + 1 if self.headers else row_index
        
        # Highlight each cell in the row
        for col in range(self.cols):
            self.cells[row_index][col].config(background=color)
        
        # Remove highlight after duration
        if duration > 0:
            self.master.after(duration, lambda: self.remove_highlight(row_index))
    
    def remove_highlight(self, row_index):
        """Remove highlight from a row"""
        adjusted_row = row_index + 1 if self.headers else row_index
        
        for col in range(self.cols):
            self.cells[row_index][col].config(background='white')
        

class Register:

    # ======== Atributos ======== #

    ID : int;
    data : str;

    # ======== Construtor ======== #

    def __init__(self, ID=-1, data=""):
        self.ID = ID;
        self.data = data;

    # ======== Metodos ======== #

        # "To String"
    def __repr__(self):
        return (f"'ID: {self.ID}, data: {self.data}'");

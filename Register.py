class Register:

    # ======== Atributos ======== #

    ID : int;

    # ======== Construtor ======== #

    def __init__(self, ID=-1):
        self.ID = ID;

    # ======== Metodos ======== #

        # "To String"
    def __repr__(self):
        return (f"{self.ID}");

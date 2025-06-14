from Register import Register;

class Bucket:

    # ======== Atributos ======== #

    n : int;              # Quantidade maxima de entidades no bucket
    i : int;              # Index no bucket
    local_depth : int;    # Profundidade local do bucket
    regs : list;

    # ======== Construtor ======== #
    def __init__ (self, depth, qnt=3):

        if (qnt < 1):
            print ("ERRO: A quantidade minima de elementos no bucket deve ser maior do que 1!");
        else:
            self.n = qnt;
            self.i = 0;
            self.regs = ['']*self.n;
            self.local_depth = depth;

    # ======== Metodos ======== #

        # Inserir novo registro no bucket
    def insert (self, ID : int):

        res = -1;

        if (self.i >= self.n):
            print ("ERRO: O bucket esta cheio!");
        else:
            self.regs[self.i] = Register(ID);
            res = self.i;
            self.i += 1;
            
            # Sort the bucket contents after insertion!!!!!!!!!!!!!1
            self.regs = sorted(self.regs[:self.i], key=lambda reg: reg.ID) + self.regs[self.i:]
    
        return (res);
    
        # Encontra um registro usando ID
    def find (self, ID):
        res : Register = None;

        i = 0;
        var = 0
        
        while (i < self.i):
            if (self.regs[i].ID == ID):
                res = self.regs[i];
                var = i
                i = self.i;
            i += 1;
 
        return ((res, var+1));

        # Verificar se o bucket esta cheio
    def isFull (self):
        return (self.i >= self.n);

        # Verificar se o bucket esta vazio
    def isEmpty (self):
        return (self.i > 0);

        # "To string"
    def __repr__(self):
        return (f"{{ Reg = {self.regs}, local_depth = {self.local_depth} }}");

from Bucket import Bucket;
from Register import Register;

class ExtendibleHash:

    # ======== Atributos ======== #

    dir_size : int;
    pow_size : int;
    dir : list;
    dref : list;

    # ======== Construtor ======== #

    def __init__(self):
        self.dir = [Bucket(0)];
        self.dir_size = 0;
        self.pow_size = 1;
        self.dref = [False];

    # ======== Metodos ======== #

        # Calcular hash
    def hash (self, ID):
        return ( int (ID % self.pow_size) );

        # Duplicar diretorio
    def dupDir (self):
        for i in range(self.pow_size):
            self.dir.append(self.dir[i]);
        
        self.dir_size += 1;
        self.pow_size = (pow(2, self.dir_size));
    
        print ("Dir increased!");

        # Inserir novo registro
    def insert (self, ID, data):

        hash = self.hash(ID);
        bk = self.dir[hash];

        if (bk.isFull() == True):
            self.dupBucket(bk, hash);
            bk = self.dir[self.hash(ID)];
        
        bk.insert(ID, data);
        
        # Duplicar bucket
    def dupBucket (self, bk, pos):

        print("Bucket duplicated!");

        new_depth = bk.local_depth + 1;

        if (new_depth > self.dir_size):
            self.dupDir();

        aux1 = Bucket(new_depth);
        aux2 = Bucket(new_depth);
    
        for i in range(bk.i):
            
            id = bk.regs[i].ID;

            if (id != -1):
                
                data = bk.regs[i].data;
                hash = self.hash(id);

                if (hash == pos):
                    aux1.insert(id, data);
                else:
                    aux2.insert(id, data);
    
        buf = int (pos + (self.pow_size/2));
        self.dir[pos] = aux1;
        self.dir[buf] = aux2;

        # Encontrar registro
    def find (self, ID):

        res : Register = None;

        hash = self.hash(ID);

        if (hash <= self.dir_size):
            bk = self.dir[hash];
            res = bk.find(ID);
        
        if (res == None):
            print ("Nome nao encontrado!");
            res = "''";

        return (res);

        # "To string"
    def __str__(self):
        str = f"dir_size = {self.dir_size}\ndir = [\n";
        rdup = [];

        for bk in self.dir:
            status = True;

            for used in rdup:
                status = status and (bk != used);

            if (status):
                str = str + "\t" + repr(bk) + "\n";

            rdup.append(bk);
        
        str += "]\n";
        return (str);

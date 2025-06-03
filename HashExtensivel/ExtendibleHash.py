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
            self.dir.append(self.dir[i]); # Copiar referencias
        
		# Aumentar tamanho do diretorio
        self.dir_size += 1;
        self.pow_size = (pow(2, self.dir_size));

        # Inserir novo registro
    def insert (self, ID, data):

        hash = self.hash(ID);	# Hash do registro
        bk = self.dir[hash];	# Bucket a ser inserido

        if (bk.isFull() == True):		
            self.dupBucket(bk, hash);		# Duplicar bucket
            bk = self.dir[self.hash(ID)];	# Recalcular bucket a ser inserido
        
        bk.insert(ID, data);	# Inserir registro
        
        # Duplicar bucket
    def dupBucket (self, bk, pos):

        new_depth = bk.local_depth + 1; # Calcular nova profundidade

        if (new_depth > self.dir_size):	# Se a pronfundidade local for maior do que a do diretorio
            self.dupDir();				# Duplicar diretorio

		# Criar buckets temporarios
        aux1 = Bucket(new_depth);	# Bucket original
        aux2 = Bucket(new_depth);	# Bucket novo
    
        for i in range(bk.i):
            
            id = bk.regs[i].ID;	# Copiar id

            if (id != -1):		# Verificar se o registro e valido
                
                data = bk.regs[i].data; 	# Copia os dados do registro
                hash = self.hash(id);		# Calcula a nova hash do registro

				# Reinserir registro
                if (hash == pos):
                    aux1.insert(id, data);	# Original
                else:
                    aux2.insert(id, data);	# Novo
    
        buf = int (pos + (self.pow_size/2)); 	 # Calcula a posicao do novo bucket

		# Alterar buckets do diretorio
        self.dir[pos] = aux1;	
        self.dir[buf] = aux2;

        # Encontrar registro
    def find (self, ID):

        res : Register = None;

        hash = self.hash(ID);

        if (hash < self.pow_size):
            bk = self.dir[hash];
            res = bk.find(ID); 		# Procura registro no bucket
        
        if (res == None):
            res = "''";

        return (res);

        # "To string"
    def __str__(self):
        str = f"dir_size = {self.dir_size}\ndir = [\n";

        rdup = []; 		# Lista de buckets ja encontrados 

		# Retornar todos os buckets no diretorio
        for bk in self.dir:

            status = True;

			# Ignorar referencias duplas
            for used in rdup:
                status = status and (bk != used); 	# Se nao for uma duplicata

            if (status):
                str = str + "\t" + repr(bk) + "\n";
				rdup.append(bk); 					# Adicionar bucket na lista
        
        str += "]\n";
        return (str);

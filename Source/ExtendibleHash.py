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
        # funcao do puddo de aumentar diretorio
    #def dupDir (self):
        #for i in range(self.pow_size):
            #self.dir.append(self.dir[i]); # Copiar referencias
        
		# Aumentar tamanho do diretorio
        #self.dir_size += 1;
        #self.pow_size = (pow(2, self.dir_size));

        # Nova função de aumentar o diretorio
    def dupDir(self):
    # Aumentar tamanho do diretorio
        self.dir_size += 1
        self.pow_size = (pow(2, self.dir_size))
        # Copiar referencias
        old_dir = self.dir.copy()
        self.dir += old_dir

        # Inserir novo registro
    def insert (self, ID):

        hash = self.hash(ID);	# Hash do registro
        bk = self.dir[hash];	# Bucket a ser inserido

        status = bk.isFull();

        if (status == True):		
            self.dupBucket(bk, hash);		# Duplicar bucket
            bk = self.dir[self.hash(ID)];	# Recalcular bucket a ser inserido
        
        bki = bk.insert(ID);	# Inserir registro
    
        return ((hash, bki,));
    # funcao antiga do puddo de duplicar bucket
    def dupBucketPuddo (self, bk, pos):
        new_depth = bk.local_depth + 1; # Calcular nova profundidade

        if (new_depth > self.dir_size):	# Se a pronfundidade local for maior do que a do diretorio
            self.dupDir();				# Duplicar diretorio

        # Criar buckets temporarios
        aux1 = Bucket(new_depth);	# Bucket original
        aux2 = Bucket(new_depth);	# Bucket novo
    
        for i in range(bk.i):
            
            id = bk.regs[i].ID;	# Copiar id

            if (id != -1):		# Verificar se o registro e valido
                
                hash = self.hash(id);		# Calcula a nova hash do registro

                # Reinserir registro
                if (hash == pos):
                    aux1.insert(id);	# Original
                else:
                    aux2.insert(id);	# Novo
    
        buf = int (pos + (self.pow_size/2)); 	 # Calcula a posicao do novo bucket

        # Alterar buckets do diretorio
        self.dir[pos] = aux1;	
        self.dir[buf] = aux2;

    def dupBucket(self, bk, pos):
        new_depth = bk.local_depth + 1  # Calcular nova profundidade

        if new_depth > self.dir_size:  # Se a profundidade local for maior do que a do diretorio
            self.dupDir()  # Duplicar diretorio

        # Criar buckets temporarios
        aux1 = Bucket(new_depth)  # Bucket original
        aux2 = Bucket(new_depth)  # Bucket novo

        # Reinserir registros nos novos buckets
        for i in range(bk.i):
            id = bk.regs[i].ID
            if id != -1:
                hash = self.hash(id)
                if (hash & (1 << (new_depth - 1))) == 0:
                    aux1.insert(id)
                else:
                    aux2.insert(id)

        # Atualizar referencias no diretorio
        for i in range(self.pow_size):
            # Se o bucket antigo estava referenciado aqui e o bit relevante for 0, aponta para aux1, senão aux2
            if self.dir[i] == bk:
                if (i & (1 << (new_depth - 1))) == 0:
                    self.dir[i] = aux1
                else:
                    self.dir[i] = aux2
        # Encontrar registro
    def find (self, ID):

        res = None;

        hash = self.hash(ID);

        if (hash < self.pow_size):
            bk = self.dir[hash];
            res = bk.find(ID); 		# Procura registro no bucket

        return (res);

        # Apaga o registro
    def delete (self, ID):

        res = False;
    
        reg = self.find(ID);

        if (reg != None):
            reg.ID = -1;
            res = True;
    
        return (res);

        # Encontra as referencias dos buckets guardando as duplicatas em tuplas
    def getRefs (self):

        rdup = []; 		# Lista de buckets ja encontrados
        res = [];       # Lista de posicoes
        i = 0;          # index
        
        for bk in self.dir:

            status = True;
            other = -1;

            j = 0;
            n = len(rdup);
            while (j < n and status == True):
                status = status and (bk != rdup[j]);    # Se o bucket nao estiver na lista
                other = j;                              # Guarda a posicao da primeira referencia no diretorio
                j += 1;
    
            if (status == True):    # Se nao estiver na lista
                res.append(i);    # Adiciona posicao
                rdup.append(bk);    # Adiciona bucket na lista
            
            else:                           # Se estiver na lista
                res[other] = (other, i);    # Cria uma tupla para as duas posicoes
            
            i += 1;
    
        return (res);

    # Referencias do diretorio formatadas
    def formatedRefs (self):

        ref = self.getRefs();
        res = [0]*self.pow_size

        i = 0;
        for r in ref:
            if (type(r) == tuple):
                for y in r:
                    res[y] = i;
            else:
                res[r] = i;

            i += 1;
    
        return (res);

        # "To string"
    def __str__(self):

        res = f"dir_size = {self.dir_size}\ndir = [\n";

        refs = self.getRefs();      # Econtra referencias

        n = len(refs);
        for i in range(n):
            pos = refs[i];
            res = f"{res}\t{pos}\t->\t";    # Referencias dos buckets

            if (type(pos) == tuple):
                pos = pos[0];

            res = f"{res}{ repr( self.dir[pos] ) }\n";  # Bucket correspondente
        
        res += "]\n";

        return (res);

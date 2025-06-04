import ExtendibleHash as EH;

# ======== Metodo principal ======== #

if __name__ == "__main__":
	hash = EH.ExtendibleHash();
	print(f"Insert: \n\n{hash}");
	hash.insert(1, "Davi");
	print(hash);
	hash.insert(2, "Ferreira");
	print(hash);
	hash.insert(3, "Puddo");
	print(hash);
	hash.insert(4, "Nao sei");
	print(hash);
	hash.insert(5, "Nada");
	print(hash);
	hash.insert(6, "Tonin");
	print(hash);
	hash.insert(7, "Quel");
	print(hash);
	hash.insert(8, "Aura");
	print(hash);

	print("\n\nDelete: \n\ndelete(8)\n");
	hash.delete(8);
	print(hash);
	print("delete(8)\n");
	hash.delete(8);
	print(hash);

	print ("\n\nUpdate: \n\nupdate(5, hahaha)\n");
	hash.update(5, "hahaha");
	print(hash)

	print ("Find: \n\n");
	print(f"find(1)={hash.find(1)}");
	print(f"find(20)={hash.find(20)}");

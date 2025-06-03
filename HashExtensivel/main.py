import ExtendibleHash as EH;

# ======== Metodo principal ======== #

if __name__ == "__main__":
	hash = EH.ExtendibleHash();
	print(hash);
	hash.insert(1, "Davi");
	print(f"find={hash.find(2)}");
	print(hash);
	hash.insert(2, "Ferreira");
	print(hash);
	hash.insert(3, "Puddo");
	print(hash);
	hash.insert(4, "Nao sei");
	print(hash);
	print(f"find={hash.find(20)}");

import ExtendibleHash as EH;

# ======== Metodo principal ======== #

if __name__ == "__main__":
	hash = EH.ExtendibleHash();
	print(f"Insert: \n\n{hash}");
	hash.insert(1);
	print(hash);
	hash.insert(2);
	print(hash);
	hash.insert(3);
	print(hash);
	hash.insert(4);
	print(hash);
	hash.insert(5);
	print(hash);
	hash.insert(6);
	print(hash);
	hash.insert(7);
	print(hash);
	hash.insert(8);
	print(hash);

	print("\n\nDelete: \n\ndelete(8)\n");
	hash.delete(8);
	print(hash);
	print("delete(8)\n");
	hash.delete(8);
	print(hash);

	print ("Find: \n\n");
	print(f"find(1)={hash.find(1)}");
	print(f"find(20)={hash.find(20)}");

	print(f"\n\n\n{hash.formatedRefs()}");

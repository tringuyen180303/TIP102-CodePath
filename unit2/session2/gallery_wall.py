def organize_exhibition(collection):
    unique_collections = {}
    for art_name in collection:
        if art_name not in unique_collections:
            unique_collections[art_name] = 0
        unique_collections[art_name] += 1
    answer = []
    
    while unique_collections:
        row = []
        for name in list(unique_collections.keys()):
            row.append(name)
            unique_collections[name] -= 1
            if unique_collections[name] == 0:
                del unique_collections[name]
        answer.append(row)

    print(unique_collections)
    return answer

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))
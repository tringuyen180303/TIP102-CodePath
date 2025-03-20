def is_authentic_collection(art_pieces):
    numbers_check = {}
    max_number = 0
    for i in art_pieces:
        if i not in numbers_check:
            max_number = max(i, max_number)
            numbers_check[i] = 0
        numbers_check[i] += 1
    checked = True
    for i in art_pieces:
        if i in numbers_check and i != max_number and numbers_check[i] == 1:
            print("Condition 1")
            continue
        elif i == max_number and numbers_check[i] == 2:
            print("Condition 2")
            continue
        else:
            checked = False
    return checked



collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
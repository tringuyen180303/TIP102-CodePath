def build_skyscrapers(floors):
    skyscaper = 1
    for i in range(len(floors)):
        for j in range(i+1, len(floors)):
            if floors[j] > floors[i]:
                break
            elif floors[j] < floors[i]:
                skyscaper += 1
                break
    return skyscaper
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
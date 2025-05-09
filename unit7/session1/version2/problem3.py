def find_last_building(n, k):
    
    buildings = [i for i in range(1, n +1 )]
    return helper(buildings, k, 0)
    

def helper(buildings, k, idx):
    print(buildings)
    if len(buildings) == 1:
        return buildings[0]
    idx = (idx + k - 1) % len(buildings)
    print("idx", idx)
    print(buildings[idx])
    buildings.pop(idx)
    return helper(buildings, k, idx)



print(find_last_building(5, 2))
#print(find_last_building(6, 5))
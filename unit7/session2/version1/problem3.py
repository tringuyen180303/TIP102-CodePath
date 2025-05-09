def find_frequency_positions(transmissions, target_code):
    low = 0
    high = len(transmissions) - 1
    min_occ = -1
    last_occ = -1
    # 5, 7, 7, 8, 8, 10]
    # 5, 7, 7, 8, 8, 10
    while low <= high:
        mid = (low + high) // 2
        print("mid", mid)
        if transmissions[mid] > target_code:
            high = mid - 1
            
        elif transmissions[mid] < target_code :
            low = mid + 1
            
        else:
            min_occ = mid
            high = mid - 1
    low, high = 0, len(transmissions) - 1
    while low <= high:
        mid = (low + high) // 2
        print("mid", mid)
        if transmissions[mid] > target_code:
            high = mid - 1
            
        elif transmissions[mid] < target_code :
            low = mid + 1
            
        else:
            last_occ = mid
            low = mid + 1
            
    return (min_occ, last_occ)

'''
n = 5 - 1
mid = 5// 2 = 2
[5,7,7,8,8,10]
 0 1 2 3 4  5
[8,8,10]
 3 4  5

mid = 3//2 = 1

 7,8,8,10]






'''


print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
def check_stock(inventory, part_id):
    low = 0
    high = len(inventory) - 1
    if low >= high:
        return False
    mid = (low + high) // 2
    #print("mid", mid)
    if part_id == inventory[mid]:
        return True
    elif part_id < mid:
        return check_stock(inventory[:mid], part_id)
    else:
        return check_stock(inventory[mid+1:], part_id)

print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100))
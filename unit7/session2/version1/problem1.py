def check_stock(inventory, part_id):
    low = 0
    high = len(inventory) - 1

    while low <= high:
        mid = (high + low) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            low = mid + 1
        else: high = mid - 1
    return False
print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))
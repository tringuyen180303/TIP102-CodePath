def can_split_coffee(coffee, n):
    sum = sum_of_volume(coffee)

    return sum % n == 0
    

def sum_of_volume(coffee):

    if len(coffee) == 0:
        return 0
    return coffee[0] + sum_of_volume(coffee[1:])


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
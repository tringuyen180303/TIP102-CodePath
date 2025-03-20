def min_swaps(s):
    balance = 0
    swaps = 0
    for char in s:
        if char == "[":
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                swaps += 1
                balance = 1
    return balance // 2 

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  
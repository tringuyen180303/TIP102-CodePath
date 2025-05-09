def longest_trident_sequence(gems):
    return helper(gems, 0,  0)

def helper(gems, m, n):

    
    if not gems:
        return m
    
    if len(gems) == 1:
        return m
    
    if gems[1] - 1 == gems[0]:
        n += 1
        m = max(m, n)
    else:
        n = 1
    return helper(gems[1:],m, n)

print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 9, 1, 2]))
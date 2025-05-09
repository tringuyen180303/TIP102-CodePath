def next_greatest_letter(letters, target):
    low = 0
    high = len(letters) - 1
    lowests_score = 100000
    lowests_char = letters[0]
    while low <= high:
        mid = (low + high) // 2
        diff = ord(letters[mid]) - ord(target)
            
        if diff <= 0:
            low = mid +  1
            
        else:
            high = mid - 1
            lowests_char = letters[mid]
    return lowests_char
    
letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))
print(ord("a") - ord("e"))
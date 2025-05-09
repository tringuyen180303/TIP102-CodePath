def sort_crystals(crystals):
    if len(crystals) <= 1:
        return crystals
    
    mid = len(crystals) // 2
    left = sort_crystals(crystals[:mid])
    right = sort_crystals(crystals[mid:])

    return merge(left, right)


def merge(left, right):
    results = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    while i < len(left):
        results.append(left[i])
        i += 1
    
    while j < len(right):
        results.append(right[j])
        j += 1
    return results



print(sort_crystals([5, 2, 3, 1]))
print(sort_crystals([5, 1, 1, 2, 0, 0]))
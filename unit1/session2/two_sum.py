def two_sum(nums, targerts):
    dicts = {}
    for i, num in enumerate(nums):
        diff = targerts - num
        if diff not in dicts:
            dicts[num] = i
        else:
            return [dicts[diff], i]
    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
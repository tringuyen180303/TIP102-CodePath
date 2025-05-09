def maximuSubArrayLen(nums, k):
    # nums [1, 0, 1, 5, -2, 3]; k = 3
    # output = 4

    total = 0
    prefix_map = {0:-1}
    res = 0
    for idx, num in enumerate(nums):
        total += num
        if total - k in prefix_map:
            res = max(res, idx - prefix_map[total - k])
        if total not in prefix_map:
            prefix_map[total] = idx
    return res
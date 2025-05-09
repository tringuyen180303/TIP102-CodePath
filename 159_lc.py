def longest_substring_two_distinct(s):
    """
    s = "eceba" = 3
    s = "ccaabbb" = 5
    """

    seen_indexes = {}
    left = 0
    n = len(s)
    res = 0
    for right in range(n):
        c = s[right]
        seen_indexes[c] = right
        if len(seen_indexes) == 3:
            min_idx = min(seen_indexes.values())
            del seen_indexes[s[min_idx]]
            left = min_idx + 1
        res = max(res, right - left + 1)
    return res
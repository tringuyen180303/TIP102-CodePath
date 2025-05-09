def longest_substring(s, k):
    return divide_and_conquer(s, k)
def divide_and_conquer(s, k):
    if len(s) < k:
        return 0
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
    print(freq_map)

    for char in freq_map:
        if freq_map[char] < k:
            return max(divide_and_conquer(sub_str, k) for sub_str in s.split(char))
            #break
            #for sub_str in s.split(k):
            #    print(sub_str)
            #print(sub_str for sub_str in s.split(k))
    return len(s)


print(longest_substring("tatooine", 2))
print(longest_substring("chewbacca", 2))
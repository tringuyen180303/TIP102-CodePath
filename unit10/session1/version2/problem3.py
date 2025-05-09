def identify_celebrity(trust, n):
    dictionary = {}
    contestants = set()
    for pair in trust:
        a, b = pair[0], pair[1]
        contestants.add(a)
        dictionary[b] = dictionary.get(b, 0) + 1
    max_val = max(dictionary.values())
    possible_celeb = [k for k, v in dictionary.items() if v == max_val][0]

    if possible_celeb not in contestants and max_val == n -1:
        return possible_celeb
    return -1



trust1 = [[1,2]]
trust2 = [[1,3],[2,3]]
trust3 = [[1,3],[2,3],[3,1]]

print(identify_celebrity(trust1, 2))
print(identify_celebrity(trust2, 3))
print(identify_celebrity(trust3, 3))
"""
Example Output:

2
3
-1
"""
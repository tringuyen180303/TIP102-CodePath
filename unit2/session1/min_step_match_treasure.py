def counting_pirates_action_minutes(logs, k):
    dictionary = {}
    for an in logs:
        if an[0] not in dictionary:
            dictionary[an[0]] = set()
        dictionary[an[0]].add(an[1])
    array = [0 for i in range(k)]
    for i in dictionary:
        array[len(dictionary[i])-1] += 1
    print(dictionary)
    return array
        



logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
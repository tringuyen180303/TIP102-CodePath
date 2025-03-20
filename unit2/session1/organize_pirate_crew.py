def organize_pirate_crew(group_sizes):
    dictionary = {}
    answers = []

    for pirate_id, size in enumerate(group_sizes):
        if size not in dictionary:
            dictionary[size] = []
            dictionary[size].append(pirate_id)
        else:
            dictionary[size].append(pirate_id)
        if len(dictionary[size]) == size:
            answers.append(dictionary[size])
            dictionary[size] = []
    return answers


group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]
print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
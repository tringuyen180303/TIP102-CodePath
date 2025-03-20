def beauty_sum(collection):
    total_sum = 0
    for i in range(len(collection)):
        visited = {}
        for j in range(i, len(collection)):
            if collection[j] not in visited:
                visited[collection[j]] = 0
            visited[collection[j]] += 1
            print(visited)
            max_freq = max(visited.values())
            min_freq = min(visited.values())
            total_sum += max_freq - min_freq
    return total_sum

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

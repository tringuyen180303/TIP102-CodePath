def find_path(venue_map, target):
    visited = set()
    result = []
    path = []
    

    def dfs(node):
        visited.add(node)
        path.append(node)
       #print("path", path)
        if node == target:
            #print("node", node)
            #print("p", path)
            #return path
            #result = path.copy()
            #print("res", result)
            result.append(path.copy())
            #return result
        for neighbor in venue_map[node]:
            if neighbor not in visited:
                dfs(neighbor)
        path.pop()
    dfs(0)
    return result[0]
venue_map = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1, 5],
    [2],
    [3]
]

print(find_path(venue_map, 5))
print(find_path(venue_map, 2))
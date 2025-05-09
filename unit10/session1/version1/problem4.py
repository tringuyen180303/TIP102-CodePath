def get_all_destinations(flights, start):
    stack = []
    visited = set()
    visited.add(start)
    stack.append(start)
    result = []
    result.append(start)
    for i in flights[start]:
        if i not in visited:
            dfs_helper(flights, i, visited, result)
    return result
def dfs_helper(flights, start, visited, result):
    if start not in visited:
        visited.add(start)
        result.append(start)
        for neighor in flights.get(start, []):
            dfs_helper(flights, neighor, visited, result)
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
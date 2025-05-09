def num_airline_regions(is_connected):
    n = len(is_connected)
    visited = [False] * n
    regions = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(is_connected, visited, i)
            regions += 1
    return regions
def dfs(is_connected, visited, start):
    for v, conn in enumerate(is_connected[start]):
        if conn and not visited[v]:
            visited[v] = True
            dfs(is_connected, visited, v)
        

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 
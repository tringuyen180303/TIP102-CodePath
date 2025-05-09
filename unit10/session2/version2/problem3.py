def has_rivalry_loop(rivalries):
    visited = [False] * len(rivalries)

    def dfs(rivalry, parent):
        visited[rivalry] = True

        for v in rivalries[rivalry]:
            if not visited[v]:
                if dfs(v, rivalry):
                    return True
            elif v != parent:
                return True
        return False
    
    for node in range(len(rivalries)):
        if not visited[node]:
            if dfs(node, -1):
                return True
    return False
     
# def has_rivalry_loop(rivalries):
#     visited = [False] * len(rivalries)
#     path = [False] * len(rivalries)

#     def dfs(rivalry):
#         visited[rivalry] = True
#         path[rivalry] = True

#         for neighbor in rivalries[rivalry]:
#             if path[neighbor]:
#                 return True
#             if not visited[neighbor]:
#                 if dfs(neighbor):
#                     return True
#         path[rivalry] = False
#         return False
#     for i in range(len(rivalries)):
#         if not visited[i] and dfs(i):
#             return False
#     return True



rivalries_1 = [
    [1],
    [0, 2],
    [1, 3],
    [2]
]

rivalries_2 = [
    [1],
    [2],
    [3],
    [0]
]

print(has_rivalry_loop(rivalries_1))  
print(has_rivalry_loop(rivalries_2)) 
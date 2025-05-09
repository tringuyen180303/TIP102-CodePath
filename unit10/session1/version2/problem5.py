def have_connection(celebs, start_celeb, target_celeb):

    def dfs(celebs, start_celeb):
        visited = [False] * len(celebs)
        return dfs_help(celebs, start_celeb, visited, target_celeb)
    def dfs_help(celebs, node, visited, target):
        if visited[node] == False:
            visited[node] = True
            if node == target:
                return True
            for v, known in enumerate(celebs[node]):
                if known and visited[v] == False:
                    if dfs_help(celebs, v, visited, target):
                        return True
        return False
    return dfs(celebs, start_celeb)
celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))
def have_connection(celebs, start_celeb, target_celeb):
    from collections import deque
    queue = deque()
    visited = [False] * len(celebs)
    queue.append(start_celeb)

    while queue:
        celeb = queue.popleft()
        if celeb == target_celeb:
            return True
        for v, known in enumerate(celebs[celeb]):
            if known and visited[v] == False:
                queue.append(v)
                visited[v] = True
    return False


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
"""You are in charge of scheduling celebrity arrival times for a red carpet event. To make things easy, you want to split the group of n celebrities labeled from 1 to n into two different arrival groups.

However, your boss has just informed you that some celebrities don't get along, and celebrities who dislike each other may not be in the same arrival group. Given the number of celebrities who will be attending n, and an array dislikes where dislikes[i] = [a, b] indicates that the person labeled a does not get along with the person labeled b, return True if it is possible to split the celebrities into two arrival periods and False otherwise.
"""

# Bi partie grapgh

def can_split(n, dislikes):
    graph = {i :[] for i in range(1, n + 1)}
    print(graph)
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

    color = [0] * (n+1)

    def dfs(node, current_color):
        color[node] =  current_color
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                if not dfs(neighbor, -current_color):
                    return False
            elif color[neighbor] == current_color:
                return False
        return True
    for celebrity in range(1, n+1):
        if color[celebrity] == 0:  # If the celebrity is uncolored
            if not dfs(celebrity, 1):  # Start with color 1
                return False
    return True


dislikes_1 = [[1, 2], [1, 3], [2, 4]]
dislikes_2 = [[1, 2], [1, 3], [2, 3]]

print(can_split(4, dislikes_1))
print(can_split(3, dislikes_2))
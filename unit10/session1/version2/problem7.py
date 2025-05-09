"""Problem 7: Gossip Chain
In Hollywood, rumors spread rapidly among celebrities through various connections. Imagine each celebrity is represented as a vertex in a directed graph, and the connections between them are directed edges indicating who spread the latest gossip to whom.

The arrival time of a rumor for a given celebrity is the moment the rumor reaches them for the first time, and the departure time is when all the celebrities they could influence have already heard the rumor, meaning they are no longer involved in spreading it.

Given a list of edges connections representing connections between celebrities and the number of celebrities in the the graph n, find the arrival and departure time of the rumor for each celebrity in a Depth First Search (DFS) starting from a given celebrity start.

Return a dictionary where each celebrity in connections is a key whose corresponding value is a tuple (arrival_time, departure_time) representing the arrival and departure times of the rumor for that celebrity. If a celebrity never hears the rumor their arrival and departure times should be (-1, -1).
"""

# def rumor_spread_times(connections, n, start):
#     id_map = {}
#     for a, b in connections:
#         if a not in id_map:
#             id_map[a] = len(id_map)
#         if b not in id_map:
#             id_map[b] = len(id_map)

#     m = len(id_map)                     # number of vertices

#     # ---------- undirected adjacency matrix ----------
#     adj = [[0]*m for _ in range(m)]
#     for a, b in connections:
#         i, j = id_map[a], id_map[b]
#         adj[i][j] = adj[j][i] = 1

#     # ---------- DFS with arrival / departure ----------
#     times   = {name: [-1, -1] for name in id_map}
#     visited = [False]*m
#     clock   = [1]                       # mutable counter
#     rev     = {v: k for k, v in id_map.items()}

#     print(adj)
#     print("---" * 30)
#     print("id_map", id_map)
#     print("---" * 30)
#     print("rev", rev)
#     print("---" * 30)

#     def dfs(u):
#         visited[u] = True
#         name = rev[u]
#         times[name][0] = clock[0]       # arrival
#         clock[0] += 1  # id = 5

#         for v, has_edge in enumerate(adj[u]):
#             if has_edge and not visited[v]:
#                 dfs(v)

#         times[name][1] = clock[0]       # departure
#         clock[0] += 1

#     if start in id_map:                 # run DFS only if the start exists
#         dfs(id_map[start])

#     # lists → tuples
#     return {k: tuple(v) for k, v in times.items()}

from collections import defaultdict

def rumor_spread_times(connections, n, start):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
    
    # Step 2: Initialize arrival and departure dictionaries with default values (-1)
    arrival = {}
    departure = {}
    all_celebrities = set([u for u, _ in connections] + [v for _, v in connections])
    
    for celeb in all_celebrities:
        arrival[celeb] = -1
        departure[celeb] = -1
    
    # Step 3: DFS Function to track time
    time = [0]  # Keep track of the time as a list so it's mutable in the dfs

    def dfs(celeb):
        # Set arrival time
        time[0] += 1
        arrival[celeb] = time[0]
        
        # Explore all neighbors
        for neighbor in graph[celeb]:
            if arrival[neighbor] == -1:  # Only visit if not already visited
                dfs(neighbor)
        
        # Set departure time
        time[0] += 1
        departure[celeb] = time[0]
    
    # Step 4: Start DFS from the given starting celebrity
    if start in all_celebrities:
        dfs(start)
    
    # Step 5: Return the results
    result = {celeb: (arrival[celeb], departure[celeb]) for celeb in all_celebrities}
    return result
connections = [
    ["Amber Gill", "Greg O'Shea"],
    ["Amber Gill", "Molly-Mae Hague"],
    ["Greg O'Shea", "Molly-Mae Hague"],
    ["Greg O'Shea", "Tommy Fury"],
    ["Molly-Mae Hague", "Tommy Fury"],
    ["Tommy Fury", "Ovie Soko"],
    ["Curtis Pritchard", "Maura Higgins"]
]

print(rumor_spread_times(connections, 7, "Amber Gill"))
"""
Example Output:

{
    "Amber Gill": (1, 12),
    "Greg O'Shea": (2, 11),
    "Molly-Mae Hague": (3, 8),
    "Tommy Fury": (4, 7),
    "Ovie Soko": (5, 6),
    "Curtis Pritchard": (-1, -1),
    "Maura Higgins": (-1, -1)
}
"""
"""There are n airports numbered from 0 to n - 1 and n - 1 direct flight routes between airports such that there is exactly one way to travel between any two airports (this network forms a tree). Last year, the aviation authority decided to orient the flight routes in one direction due to air traffic regulations.

Flight routes are represented by connections, where connections[i] = [airport_a, airport_b] represents a one-way flight route from airport airport_a to airport airport_b.

This year, there will be a major aviation event at the central hub (airport 0), and many flights need to reach this hub.

Your task is to reorient some flight routes so that every airport can send flights to airport 0. Return the minimum number of flight routes that need to be reoriented.

It is guaranteed that after the reordering, each airport will be able to send a flight to airport 0.
"""
def min_reorient_flight_routes(n, connections):
    graph = [[] for i in range(n)]
    directed_edges = set()
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
        directed_edges.add((a,b))
    count = 0
    def dfs(airport, parent):
        nonlocal count
        for neighbor in graph[airport]:
            if neighbor == parent:
                continue
            if (airport, neighbor) in directed_edges:
                count += 1
            dfs(neighbor, airport)
    dfs(0, -1)
    return count
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

print(min_reorient_flight_routes(n, connections))
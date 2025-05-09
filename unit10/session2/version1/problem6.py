def find_all_flight_routes(flight_routes):
    visited = [False] * len(flight_routes)
    path = []
    result = []
    def dfs(node):
        path.append(node)
        print("path", path)
        if node == len(flight_routes) - 1:
            result.append(path.copy())
        else:
            for neighbor in flight_routes[node]:
                dfs(neighbor)
        print("pop",path.pop())
    dfs(0)
    return result

flight_routes_1 = [[1, 2], [3], [3], []]

print(find_all_flight_routes(flight_routes_1))

flight_routes_2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(find_all_flight_routes(flight_routes_2))
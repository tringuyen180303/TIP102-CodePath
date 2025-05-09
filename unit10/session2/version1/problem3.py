"""Given an adjacency dictionary of flights flights where each key is an airport i and flights[i] is an array indicating that there is a flight from destination i to each destination in flights[i], return an array with the flight path from a given source location to a given destination location.

If there are multiple flight paths from the source to destination, return any flight path.
"""
def get_itinerary(flights, source, dest):
    
    def dfs(flights, start, dest):
        visited = set()
        #path = []
        return  dfs_helper(flights, start, visited, [], dest)
        
    def dfs_helper(flights, node, visited, path, dest):
        if node not in visited:
            visited.add(node)
            path.append(node)
            if node == dest:
                return path
            for neighbor in flights.get(node):
                results = dfs_helper(flights, neighbor, visited, path, dest)
                if results:
                   return path
        return None
    return dfs(flights, source, dest)
    # def dfs_helper(node, dest, visited, path):
    #     if node in visited:              # already explored
    #         return None
    #     visited.add(node)
    #     path.append(node)

    #     if node == dest:                 # found the goal
    #         return path           # ★ return a copy of full path

    #     for neighbor in flights.get(node, []):
    #         result = dfs_helper(neighbor, dest, visited, path)
    #         print("result", result)
    #         if result:                   # ★ propagate successful route
    #             return path
    #     # print("path po", path.pop())
    #     #path.pop()                       # back-track
    #     return None

    # # ---------- start the DFS from source ----------
    # route = dfs_helper(source, dest, set(), [])   # ★
    # return route if route else []

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))
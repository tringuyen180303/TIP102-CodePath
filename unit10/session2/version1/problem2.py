def min_flights_to_expand(flights):
    
    def dfs(flights):
        visited = set()
        regions = 0
        for node in (flights.keys()):
            if node not in visited:
                dfs_help(flights, node, visited)
                regions += 1
                print("node", node)
                print("regions", regions)
        return regions - 1
    
    def dfs_help(flights, node,visited):
        if node not in visited:
            visited.add(node)
            for neighbor in flights.get(node):
                dfs_help(flights, neighbor, visited)
    
    return dfs(flights)
            


flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD', 'MNS'],
    'MNS' : ["ATL"],
    'POR' : ['BOS'],
    'BOS' : ['POR']
}

print(min_flights_to_expand(flights))
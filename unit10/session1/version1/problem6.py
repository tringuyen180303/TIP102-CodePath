def find_itinerary(boarding_passes):
    from collections import defaultdict
    adj = defaultdict(list)
    departures = set()
    arrivals = set()
    for dep, arr in boarding_passes:
        adj[dep].append(arr)
        departures.add(dep)
        arrivals.add(arr)
    
    start = (departures - arrivals).pop()
    print(adj)
    res = []
    def dfs(adj, airport, result):
        while adj[airport]:
            next_airport = adj[airport].pop()
            dfs(adj, next_airport, result)
        result.append(airport)
    dfs(adj, start, res)
    return res[::-1]
boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))
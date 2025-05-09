from collections import deque
def get_all_destinations(flights, start):
    queue = deque()
    visited = set()
    visited.add(start)
    result = [start]
    queue.append(start)
    print("vistied", visited)
    while queue:
        city = queue.popleft()

        for neighbor in flights.get(city, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                result.append(neighbor)
    return result



flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
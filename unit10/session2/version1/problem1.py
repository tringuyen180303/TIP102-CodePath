
# DFS approacch
def calculate_cost(flights, start, dest):
    visited = set()
    def dfs(current, total):
        if current == dest:
            return total
        for neighbor, cost in flights.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, total + cost)
                if result != -1:
                    return result
        return -1
    
    return dfs(start, 0)
    
# BFS
def calculate_cost(flights, start, dest):
    from collections import deque
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    cost_dictionary = {start: 0}
    while queue:
        city = queue.popleft()
        for neighbor, cost in flights.get(city, []):
            if neighbor not in cost_dictionary:
                cost_dictionary[neighbor] = cost_dictionary[city] + cost
            if neighbor == dest:
                return cost_dictionary[neighbor]
            queue.append(neighbor)
    return -1
    # pq = deque([start])
    # cost_dict = {start: 0}

    # while pq:
    #     city = pq.popleft()
    #     for neighbor, cost in flights.get(city, []):
    #         if neighbor not in cost_dict:
    #             cost_dict[neighbor] = cost_dict[city] + cost
    #         if neighbor == dest:
    #             return cost_dict[neighbor]
    #         pq.append(neighbor)
    # return -1
        
        

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))
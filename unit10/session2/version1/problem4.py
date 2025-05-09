def can_complete_flight_training(num_courses, flight_prerequisites):
    from collections import defaultdict
    id_map = {}
    idx = 0
    for flightA, flightB in flight_prerequisites:
        if flightA not in id_map:
            id_map[flightA] = idx
            idx += 1
        if flightB not in id_map:
            id_map[flightB] = idx
            idx += 1
    print(id_map)

    graph = [[] for _ in range(num_courses)]
    for course, preq in flight_prerequisites:
        id= id_map.get(course)
        preq_id = id_map.get(preq)
        graph[id].append(preq_id)
    
    visited = [False] * num_courses
    path = [False] * num_courses

    def hasCycle(course):
        #id = id_map.get(course)
        visited[course] = True
        path[course] = True
        for preq in graph[course]:
            if path[preq]:
                return True
            if not visited[preq]:
                if hasCycle(preq):
                    return True
        path[course] =  False
        return False
    
    for i in range(num_courses):
        if not visited[i] and hasCycle(i):
            return False
    return True
flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))
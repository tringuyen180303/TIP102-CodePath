from collections import deque

def counting_flights(flights, start, dest):
    n = len(flights)
    dist = [-1] * n
    #print(dist)

    dist[start] = 0

    q = deque([start])
    while q:
        u = q.popleft()
        if u == dest:
            print(dist)
            return dist[u]
        print(f"flights{u}", flights[u])
        for v, hasflight in enumerate(flights[u]):
            if hasflight and dist[v] == -1:
                dist[v] = dist[u] + 1
                print(f"distu{u}", dist[u])
                print(f"distv{v}", dist[v])
                q.append(v)
    
    return -1
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]
print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
"""Hollywood is hosting a major talent summit, and representatives from all production studios across various cities must travel to the capital city, Los Angeles (city 0). There is a tree-structured network of cities consisting of n cities numbered from 0 to n-1, with exactly n-1 two-way roads connecting them. The roads are described by the 2D array roads, where roads[i] = [a, b] indicates a road connecting city a and city b.

Each studio has a car with limited seats, as described by the integer seats, which indicates the number of people that can travel in one car. Representatives can either drive their own car or join another car along the way to save fuel.

The goal is to calculate the minimum number of liters of fuel needed for all representatives to travel to the capital city for the summit. Each road between cities costs one liter of fuel to travel.

Write a function that returns the minimum number of liters of fuel required for all representatives to reach the summit.
"""
import math
def minimum_fuel(roads, seats):
    graph = [[] for i in range(len(roads)+1)]
    
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    total = [0]
    def dfs(city, parent):
        representative = 1
        for neighbor in graph[city]:
            if neighbor != parent:
                res_from_subtree = dfs(neighbor, city)
                representative += res_from_subtree
                total[0] += math.ceil(res_from_subtree / seats)
        return representative
    dfs(0, -1)
    return total[0]




roads_1 = [[0,1],[0,2],[0,3]]
seats_1 = 5

roads_2 = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats_2 = 2

print(minimum_fuel(roads_1, seats_1))  # Output: 3
print(minimum_fuel(roads_2, seats_2))  # Output: 7
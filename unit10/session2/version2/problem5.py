"""Problem 5: Maximizing Star Power Under Budget
You are the producer of a big Hollywood film and want to maximize the star power of the cast. Each collaboration between two celebrities has a star power value, and each celebrity demands a fee to be part of the project. You want to maximize the total star power of the cast while ensuring that the total cost of hiring these celebrities stays under a given budget.

You are given a graph where:

Each vertex represents a celebrity.
Each edge between two celebrities represents a collaboration, with two weights:
The star power (benefit) they bring when collaborating.
The cost to hire them both for the project.
The graph is given as a dictionary collaboration_map where each key is a celebrity and the corresponding value is a list of tuples. Each tuple contains a connected celebrity, the star power of that collaboration, and the cost of the collaboration. Given a start celebrity, target celebrity, and maximum budget, return the maximum star power it is possible for you film to have from start to target.
"""
def find_max_star_power(collaboration_map, start, target, budget):
    max_power = [0]
    visited = set()
    def dfs(node, new_budget, new_power):
        visited.add(node)
        print("node", node)
        print("new budget", new_budget)
        if node == target:
            max_power[0] = max(max_power[0], new_power)
            print("max_power", max_power)
            return
        for neighbor in collaboration_map.get(node, []):
            celeb, celeb_pow, celeb_cost = neighbor
            if celeb not in visited and new_budget + celeb_cost <= budget:
                dfs(celeb,new_budget + celeb_cost, new_power + celeb_pow)
        visited.remove(node)
    dfs(start, 0, 0)
    return max_power[0]
        
# def find_max_star_power(collaboration_map, start, target, budget):
#     max_star_power = [0]  # To store the maximum star power found

#     def dfs(current, current_star_power, current_cost, visited):
#         # If we reach the target, update the maximum star power
#         if current == target:
#             max_star_power[0] = max(max_star_power[0], current_star_power)
#             return

#         # Explore neighbors
#         for neighbor, star_power, cost in collaboration_map.get(current, []):
#             if neighbor not in visited and current_cost + cost <= budget:
#                 visited.add(neighbor)
#                 dfs(neighbor, current_star_power + star_power, current_cost + cost, visited)
#                 visited.remove(neighbor)  # Backtrack

#     # Start DFS from the start celebrity
#     visited = set([start])
#     dfs(start, 0, 0, visited)
    
#     return max_star_power[0]

# collaboration_map = {
#     "Leonardo DiCaprio": [("Brad Pitt", 40, 300), ("Robert De Niro", 30, 200)],
#     "Brad Pitt": [("Leonardo DiCaprio", 40, 300), ("Scarlett Johansson", 20, 150)],
#     "Robert De Niro": [("Leonardo DiCaprio", 30, 200), ("Chris Hemsworth", 50, 350)],
#     "Scarlett Johansson": [("Brad Pitt", 20, 150), ("Chris Hemsworth", 30, 250)],
#     "Chris Hemsworth": [("Robert De Niro", 50, 350), ("Scarlett Johansson", 30, 250)]
# }

collaboration_map = {
    "Leonardo DiCaprio": [("Brad Pitt", 40, 300), ("Robert De Niro", 30, 200)],
    "Brad Pitt":         [("Leonardo DiCaprio", 40, 300), ("Scarlett Johansson", 20, 150)],
    "Robert De Niro":    [("Leonardo DiCaprio", 30, 200), ("Chris Hemsworth", 50, 350)],
    "Scarlett Johansson":[("Brad Pitt", 20, 150), ("Chris Hemsworth", 30, 250)],
    "Chris Hemsworth":   [("Robert De Niro", 50, 350), ("Scarlett Johansson", 30, 250)],
}

print(find_max_star_power(collaboration_map, "Leonardo DiCaprio", "Chris Hemsworth", 750))
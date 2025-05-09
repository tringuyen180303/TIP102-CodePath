def bidirectional_flights(flights):
    """
    flights: List[List[int]] where flights[i] is the list of destinations
             reachable directly from i.
    Returns True if for every i→j edge there is also a j→i edge.
    """
    # Convert each adjacency list to a set for O(1) lookups
    flight_sets = [set(neigh) for neigh in flights]
    print(flight_sets)
    # for i, neigh in enumerate(flight_sets):
    #     for j in neigh:
    #         # If j is out of bounds or i not in flights[j], it's not bi-directional
    #         if j < 0 or j >= len(flights) or i not in flight_sets[j]:
    #             return False
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


# Example usage:

# Example 1: fully bidirectional
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]
print(bidirectional_flights(flights1))  # True

# Example 2: missing 2→1

print(bidirectional_flights(flights2))  # False  (0→2 exists but 2→0 does not or 2→1 exists but 1→2 does not)

# Example 3: empty graph or single node with no flights
print(bidirectional_flights([]))    # True
print(bidirectional_flights([[]]))  # True

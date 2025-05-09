"""Problem 1: Escape to the Safe Haven
You've just learned of a safe haven at the bottom right 
corner of the city represented by an m x n matrix grid. 
However, the city is full of zombie-infected zones.
 Safe travel zones are marked on the grid as 1s and infected zones 
 are marked as 0s. Given your current position as a tuple in the form (row, column), return True if you can reach the safe haven traveling only through safe zones and False otherwise. From any zone (cell) in the grid you may move up, down, left, or right.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe 
your solution has the stated time and space complexity. Assume the 
input tree is balanced when calculating time and space complexity.
"""
def can_move_safely(position, grid):
    safe_heaven = (len(grid)-1, len(grid[0])-1)
    print("safe heaven", safe_heaven)
    visited = set()

    def dfs(pos, visited):
        visited.add(pos)
        if pos == safe_heaven:
            return True
        for neighbor in find_neighbors(pos):
            if neighbor not in visited:
                print("neighbors", neighbor)
                res = dfs(neighbor, visited)
                if res:
                    return True
        visited.remove(pos)
        return False
        
    
    def find_neighbors(pos):
        row, col = pos
        R, C = len(grid), len(grid[0])
        res = []
        # Up
        if 0 <= row - 1 and grid[row-1][col]:
            res.append((row-1, col))
        # Down
        if row + 1 < R and grid[row+1][col]:
            res.append((row+1, col))
        # LEFT
        if 0 <= col -1and grid[row][col-1]:
            res.append((row, col-1))
        if col + 1 < C and grid[row][col+1]:
            res.append((row, col+1))
        return res
    #print(find_neighbors(position))
    return dfs(position, visited)


grid = [
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)

print(can_move_safely(position_1, grid))
print(can_move_safely(position_2, grid))
print(can_move_safely(position_3, grid))

"""
True
Example 1 Explanation: Can follow the path (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
(2, 2) -> (3, 2) -> (3, 3) -> (3, 4)

True
Example 2 Explanation: Although we start in an unsafe position, we can immediately
arrive in a safe position and from there safely travel to the bottom right corner (3, 4).

False
"""
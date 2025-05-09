"""Having arrived at the safe haven, you are immediately put to work evaluating how many civilians can be evacuated to the safe haven. Given an m x n grid representing the city, return a list of tuples of the form (row, column) representing every starting position in the grid from which there exists a valid path of safe zones (1s) to the safe haven in the bottom-right corner of the grid.

If the starting cell has value 0, they are considered infected and cannot reach the safe haven.
"""
def list_all_escape_routes(grid):
    safe_heaven = (len(grid)-1, len(grid[0])-1)
    print("safe heaven", safe_heaven)
    visited = set()
    R, C = len(grid), len(grid[0])
    def dfs(pos, visited):
        visited.add(pos)
        if pos == safe_heaven:
            return True
        for neighbor in find_neighbors(pos):
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True
        visited.remove(pos)
        return False
    
    def find_neighbors(pos):
        row, col = pos
        res = []
        if row - 1 >= 0 and grid[row-1][col]:
            res.append((row-1, col))
        if row + 1 < R and grid[row+1][col]:
            res.append((row+1, col))
        if col - 1 >= 0 and grid[row][col-1]:
            res.append((row, col-1))
        if col + 1 < C and grid[row][col+1]:
            res.append((row, col+1))
        return res
    path = []
    for row in range(R):
        for col in range(C):
            visited = set()
            if grid[row][col] and dfs((row, col), visited):
                path.append((row, col))
    return path




grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

print(list_all_escape_routes(grid))
"""
Example Output:

[(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]
"""
"""The zombie infection is spreading rapidly! Given a city represented as a 2D grid where 0 represents an obstacle where neither humans nor zombies can live, 1 represents a human safe zone and 2 represents a zone that has already been infected by zombies, determine how long it will take for the infection to spread across the entire city.

The infection spreads from each infected zone to its adjacent safe zones (up, down, left, right) in one hour. Return the number of hours it takes for all safe zones to be infected. If there are still safe zones remaining after the infection has spread everywhere it can, return -1.
"""

def time_to_infect(grid):
    def find_neighbors(pos):
        row, col = pos
        res = []
        if row - 1 >= 0 and grid[row-1][col] == 1:
            res.append((row-1, col))
        if row + 1 < R and grid[row+1][col] == 1:
            res.append((row+1, col))
        if col - 1 >= 0 and grid[row][col-1] == 1:
            res.append((row, col-1))
        if col + 1 < C and grid[row][col+1] == 1:
            res.append((row, col+1))
        return res
    
    from collections import deque
    R, C = len(grid), len(grid[0])
    humans = 0
    zombie_pos = []
    for row in range(R):
        for col in range(C):
            if grid[row][col] == 1:
                humans += 1
            if grid[row][col] == 2:
                zombie_pos = [row, col]
    print("zom", zombie_pos)
    queue = deque()
    queue.append(tuple(zombie_pos))
    hour = 0
    if humans == 0:
            return hour
    while queue and humans:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            
            neighbors = find_neighbors(node)
            for neighbor in neighbors:
                grid[neighbor[0]][neighbor[1]] = 2
                humans -= 1
                queue.append(neighbor)
        print("updated grid", grid)
        hour += 1
        print("hour", hour)
    return hour if humans == 0 else -1
        

    


grid_1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]]

grid_2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]]

grid_3 = [[0,2]]

print(time_to_infect(grid_1))
print(time_to_infect(grid_2))
print(time_to_infect(grid_3))
"""
Example Output:

4
Example 1 Explanation: See image included above. 

-1
Example 2 Explanation: The safe zone in the bottom left corner (row 2, column 0) 
is never infected because infection only happens up, left, right, and down.

0
Example 3 Explanation: Since there are already no safe zones at minute 0, the answer is just 0"""
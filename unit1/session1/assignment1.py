def local_maximums(grid):
    n = len(grid)
    #print(n)
    for i in range(n-2):
        for j in range(n-2):
            center_around(grid, i, j)

def center_around(grid, i, j):
    for i in range(i-1, i+2):
        for j in range(j-1, j+2):
            print(grid[i][j])

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)
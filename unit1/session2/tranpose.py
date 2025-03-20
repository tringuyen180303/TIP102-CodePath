
def transpose(matrix):
    if not matrix:
        return []
    cols = len(matrix[0])
    rows = len(matrix)
    print(cols, rows)
    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            new_matrix[c][r] = matrix[r][c]
            #print(matrix[r][c])
    #         new_matrix[r][c] = matrix[r][c]
    print(new_matrix)
    return new_matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)
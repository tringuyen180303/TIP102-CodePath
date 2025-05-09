def is_mutual(celebrities):
    if not celebrities:
        return True
    
    for i in range(len(celebrities)):
        for j in range(len(celebrities[i])):
            if celebrities[i][j] != celebrities[j][i]:
                return False
    return True

    
celebrities1 = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))
"""
True
False
"""
from collections import defaultdict
def find_center(terminals):
    dictionary = dict()
    for terminal in terminals:
        for num in terminal:
            if num in dictionary:
                return num
            else:
                dictionary[num] = 1
    return -1

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))
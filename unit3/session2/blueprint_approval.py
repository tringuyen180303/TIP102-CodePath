from collections import deque
def blueprint_approval(blueprints):
    sorted_array = sorted(blueprints)
    queue = deque()
    for i in sorted_array:
        queue.append(i)
    return list(queue)



print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 
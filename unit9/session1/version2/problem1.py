class Room():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
from collections import deque, defaultdict
def map_hotel(hotel):
    level_map = defaultdict(list)
    queue = deque()

    queue.append([hotel, 0])

    while queue:
        node, level = queue.popleft()
        level_map[level].append(node.val)

        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])
    return dict(level_map)
    # if hotel is None:
    #     return None
    # queue = deque()

    # queue.append([hotel, 0])
    # level_map = defaultdict(list)
    # while queue:
        
    #     pop_out, level = queue.popleft()

    #     if pop_out:
    #         level_map[level].append(pop_out.val)
    #         queue.append([pop_out.left, level + 1])
    #         queue.append([pop_out.right, level + 1])
    # return dict(level_map)


    
"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \ 
 301                302
"""

hotel = Room("Lobby", 
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))
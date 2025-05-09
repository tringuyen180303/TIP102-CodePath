class Room():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque 


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def reverse_odd_levels(hotel):
    queue = deque()
    res = []

    queue.append(hotel)
    even = True

    while queue:
        level_size = len(queue)
        current_queue = deque()
        for _ in range(level_size):
            node = queue.popleft()
            print("node", node.val)
            if even:
                current_queue.append(node.val)
            else:
                current_queue.appendleft(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        print("current queue", current_queue)
        for val in current_queue:
            res.append(val)
        even = not even
    return res
"""
        Lobby
      /      \
     102     101
     / \     /  \
   201 202 203 204 
"""
hotel = Room("Lobby", 
            Room(102, Room(201), Room (202)), 
                Room(101, Room(203), Room(204)))

# Using print_tree() function included at the top
class Room():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque 


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def reverse_odd_levels(hotel):
    queue = deque()
    res = []

    queue.append(hotel)
    even = True

    while queue:
        level_size = len(queue)
        current_queue = deque()
        for _ in range(level_size):
            node = queue.popleft()
            print("node", node.val)
            if even:
                current_queue.append(node.val)
            else:
                current_queue.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        print("current queue", current_queue[0])
        for val in current_queue:
            res.append(val)
        even = not even
    return res
"""
        Lobby
      /      \
     102     101
     / \     /  \
   201 202 203 204 
"""
hotel = Room("Lobby", 
            Room(102, Room(201), Room (202)), 
                Room(101, Room(203), Room(204)))

# Using print_tree() function included at the top
print(reverse_odd_levels(hotel))


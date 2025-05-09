class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

from collections import deque, defaultdict

def count_cursed_hallways(hotel, current_location, room_number):
    def find_path(node, target, path):
        if node is None:
            return False
        if node.val == target:
            return True
        path.append("L")
        if find_path(node.left, target, path):
            return True
        path.pop()
        path.append('R')
        if find_path(node.right, target, path):
            return True
        path.pop()
        return False
    
    path_to_s = []
    path_to_t = []
    find_path(hotel, current_location, path_to_s)
    find_path(hotel, room_number,     path_to_t)
    print(path_to_s)
    print(path_to_t)

    # find common LCA
    i = 0
    while (i < len(path_to_s) and i < len(path_to_t) and path_to_s == path_to_t[i]):
        i += 1
    print("i", i)

    # 3) To go from s up to LCA: one 'U' per remaining step in path_to_s
    up_moves = ['U'] * (len(path_to_s) - i)
    # 4) Then follow the remainder of path_to_t down
    down_moves = path_to_t[i:]
    return ''.join(up_moves + down_moves)
    

    

"""
       5
      / \
     1   2 
    /   / \
   3   6   4
"""
# Using build_tree() function included at top of page
room_nums = [5,1,2,3,None,6,4]
hotel1 = build_tree(room_nums)

print(count_cursed_hallways(hotel1, 3, 6))

"""

UURL
Explanation: The shortest path is: 3 -> 1 -> 5 -> 2 -> 6
Example Usage 2:

Example tree 'hotel2' with arrows of showing shortest path
"""
"""
  2
 /
1
"""
hotel2 = TreeNode(1, TreeNode(2))

print(count_cursed_hallways(hotel2, 1, 2))
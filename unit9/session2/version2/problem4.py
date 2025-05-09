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

# def array_to_bst(rooms):

#     def level(root, data):
#         if root is None:
#             root = TreeNode(data)
#             return root
#         if data > root.val:
#             root.right = level(root.right, data)
#         elif data < root.val:
#             root.left = level(root.left, data)
#         return root

#     if len(rooms) == 0:
#         return None
    
#     root = None
#     for i in range(len(rooms)):
#         root = level(root, rooms[i])
#     return root

def array_to_bst(rooms):
    if not rooms:
        return None
    mid = len(rooms) // 2
    root = TreeNode(rooms[mid])
    root.left = array_to_bst(rooms[:mid])
    root.right = array_to_bst(rooms[mid+1:])
    return root

rooms = [4, 7, 13, 666, 1313]

# Using print_tree() function included at top of page
print_tree(array_to_bst(rooms))

[13, 7, 1313, 4, None, 666]
"""
Balanced Tree:
       13
      /  \
    7    1313 
  /       / 
 4       666

[13, 4, 666, None, 7, 1313] is also an acceptable answer.

        13
      /  \
     4   666 
      \     \   
       7    1313
    """
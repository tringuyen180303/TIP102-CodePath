class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right
from collections import deque
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

def zigzag_icing_order(cupcakes):
    queue = deque()
    result = []
    left_to_right = True

    queue.append(cupcakes)

    while queue:
        level_size = len(queue)
        current_queue = deque()

        for i in range(level_size):
            node = queue.popleft()
            if left_to_right:
                current_queue.append(node.val)
            else:
                current_queue.appendleft(node.val)
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        for val in current_queue:
            result.append(val)
        left_to_right = not left_to_right
    return result





    # queue = deque()
    # list = []
    # left_to_right = True
    # queue.append(cupcakes)
    # left_to_right = True
    # while queue:
    #     level_size = len(queue)
    #     current_level = deque()
    #     for _ in range(level_size):
    #         node = queue.popleft()
    #         if left_to_right:
    #             current_level.append(node.val)
    #         else:
    #             current_level.appendleft(node.val)
            
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)

    #     list.extend(current_level)
    #     left_to_right = not left_to_right

    # return list
                

"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))
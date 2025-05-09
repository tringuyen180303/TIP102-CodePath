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

def vertical_inventory_display(root):
    if root is None:
        return []
    
    cols = defaultdict(list)
    min_col = max_col = 0

    queue = deque()
    queue.append([root, 0])

    while queue:
        node, col = queue.popleft()

        cols[col].append(node.val)

        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if node.left:
            queue.append([node.left, col - 1])
        if node.right:
            queue.append([node.right, col + 1])
    return [cols[c] for c in range(min_col, max_col + 1)]

"""
         Bread
       /       \
   Croissant    Donut
                /   \
             Bagel Tart
"""
# Using build_tree() function included at the top of the page
inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))  

inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, "Cake"]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory2))  
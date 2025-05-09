class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right
from collections import deque, defaultdict
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

# Using build_tree() function included at top of page
cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", "A", "B", "C", "D", "E", "F", None, None, "Chocolate", "Red Velvet"]
display = build_tree(cupcake_flavors)

def add_row(display, flavor, depth):
    if depth == 1:
        return TreeNode(flavor, left=display)
    
    def dfs(node, level):
        if not node:
            return
        if level == depth - 1:
            left = node.left
            right = node.right

            node.left = TreeNode(flavor, left=left)
            node.right = TreeNode(flavor, right=right)
        else:
            dfs(node.left, level+1)
            dfs(node.right, level+1)
    dfs(display, 1)
    return display


            
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Red Velvet
"""



# Using print_tree() function included at top of page
print(print_tree(display))
print_tree(add_row(display, "Mocha", 4))
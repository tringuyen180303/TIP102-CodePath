class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
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

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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


def lca_youngest_children(root):
    pass

"""
                Isadora the Hexed
                /                \
            Thorne               Raven
           /      \             /      \
      Dracula     Doom      Hecate    Wraith
                 /    \      
             Gloom   Mortis
"""
# Using build_tree() function included at top of the page
members = ["Isadora the Hexed", "Thorne", "Raven", "Dracula", "Doom", "Hecate", "Wraith", None, None, "Gloom", "Mortis"]
family1 = build_tree(members)

"""
              Grandmama Addams
              /              \
        Gomez Addams        Uncle Fester
                \
            Wednesday Addams
"""
members = ["Grandmama Addams", "Gomez Addams", "Uncle Fester", None, "Wednesday Addams"]
family2 = build_tree(members)

print(lca_youngest_children(family1))
print(lca_youngest_children(family2))
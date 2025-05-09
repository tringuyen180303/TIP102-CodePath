class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

from collections import deque 

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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
# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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

def remove_species(ecosystem, name):
    if ecosystem is None:
        return None
    
    if ecosystem.val < name:
        ecosystem.right = remove_species(ecosystem.right, name)
    elif ecosystem.val > name:
        ecosystem.left = remove_species(ecosystem.left, name)
    else:
        if ecosystem.left is None:
            return ecosystem.right
        elif ecosystem.right is None:
            return ecosystem.left
        
        new_ecosystem = ecosystem.left
        while (new_ecosystem.right):
            new_ecosystem = new_ecosystem.right
        ecosystem.val = new_ecosystem.val
        ecosystem.left = remove_species(ecosystem.left, new_ecosystem.val)
    return ecosystem

values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(values)

# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Lionfish"))

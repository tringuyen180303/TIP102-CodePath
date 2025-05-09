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

def purge_hotel(hotel):
    res = []

    def dfs(root, array):
        if root is None:
            return
        if root.left is None and root.right is None:
            array.append(root.val)
            return None
        if root.left or root.right:
            root.right = dfs(root.right, array)
            root.left = dfs(root.left, array)
        return root
    while hotel:
        current_arraay = []
        hotel = dfs(hotel, current_arraay)
        res.append(current_arraay)


    return res



"""
      👻
     /  \
   😱   🧛🏾‍♀️
  /  \
 💀  😈
"""


# Using build_tree() function included at the top of the page
guests = ["👻", "😱", "🧛🏾‍♀️", "💀", "😈"]
hotel = build_tree(guests)

# Using print_tree() function included at the top of the page
print_tree(hotel)
print(purge_hotel(hotel))
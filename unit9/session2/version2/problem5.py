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

def count_cursed_hallways(hotel, target_sum):
    hashmap = {0:1}
    total = 0
    res = 0
    def dfs(root):
        nonlocal res, total
        if root is None:
            return 0
        
        total += root.val
        print("root", root.val)
        print("total", total)
        #if total - target_sum in hashmap:
        res += hashmap.get(total - target_sum, 0)
        hashmap[total] = hashmap.get(total, 0) + 1
        dfs(root.left)
        dfs(root.right)
        hashmap[total] -= 1
        total -= root.val

    dfs(hotel)
    return res

"""
        10
       /  \
      /    \ 
     5      -3
    / \       \
   3   2      11
  / \   \
 3  -2   1
"""
# Using build_tree() function included at top of page
room_numbers = [10,5,-3,3,2,None,11,3,-2,None,1]
hotel = build_tree(room_numbers)

print(count_cursed_hallways(hotel, 8))
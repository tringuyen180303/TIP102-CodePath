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

def count_cookie_paths(root, target_sum):
    if root is None:
        return 0
    hashmap = {0:1}
    res = 0
    prefix_sum = 0
    def dfs(root):
        nonlocal prefix_sum
        nonlocal res
        if root is None:
            return 0
        dfs(root.left)
        prefix_sum += root.val
        if prefix_sum - target_sum in hashmap:
            print("prefix sum", prefix_sum)
            print("target sum", target_sum)
            print(hashmap.get(prefix_sum - target_sum))
            res += hashmap.get(prefix_sum - target_sum)
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
        dfs(root.right)
    dfs(root)
    print(hashmap)


    
    return res
    

    


cookie_nums = [8, 4, 12, 2, 6, None, 10]
cookies2 = build_tree(cookie_nums)
cookie_nums = [10, 5, 8, 3, 7, 12, 4]
cookies1 = build_tree(cookie_nums)
print(count_cookie_paths(cookies1, 22)) 
print(count_cookie_paths(cookies2, 14)) 


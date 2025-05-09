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

class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def larger_order_tree(order_tree, order):
    if not order_tree:
        return None

    queue = deque()
    queue.append(order_tree)

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.val == order.val:
                if i == level_size - 1:
                    return None
                else:
                    return queue[0]
        
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return None
    # queue = deque()
    # levels = 0

    # dictionary = defaultdict(list)

    # queue.append([order_tree,0 ])

    # while queue:
    #     level_size = len(queue)
    #     founded_level = -1
    #     for i in range(level_size):
    #         node, level = queue.popleft()
    #         dictionary[level].append(node.val)
    #         if order.val == node.val:
    #             founded_level = level
    #             print("founded level", founded_level)
    #             print("order", order.val)
    #             print("node", node.val)
    #         if node.left:
    #             queue.append([node.left, level + 1])
    #         if node.right:
    #             queue.append([node.right, level + 1])
            
    #     if founded_level >= 0:
    #         #print("founded level", founded_level)
    #         if order == len(dictionary[level]) - 1:
    #             #print("order", order)
    #             #print("len", len(dictionary[level]) - 1)
    #             return None
    #         else:
    #             idx = -1
    #             for i, name in enumerate(dictionary[level]):
    #                 if name == order.val:
    #                     idx = i
    #                     print("idx", idx)
    #             return dictionary[level][idx+1]
    # print(dictionary)
    # return None
    
        






"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)
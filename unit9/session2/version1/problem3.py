class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_popular_cookie_combo(root):
    dict = {}

    def dfs(node):
        if node is None:
            return 0
        subtotal = node.val + dfs(node.left) + dfs(node.right)
        dict[subtotal] = dict.get(subtotal, 0) + 1
        return subtotal
    dfs(root)
    if not dict:
        return []
    
    max_freq = max(dict.values())
    return [s for s, freq in dict.items() if freq == max_freq]
    
    print(dict)

"""
       5
      / \
     2  -3
"""
cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

"""
       5
      / \
     2  -5
"""
cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))  
print(most_popular_cookie_combo(cookies2))  
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


def build_cookie_tree(descriptions):
    if descriptions is None:
        return []
    
    root = TreeNode(descriptions[0][0])

    def find_node(root, name):
        if root is None:
            return None
        if root.val == name:
            return root
        left = find_node(root.left, name)
        if left:
            return left
        return find_node(root.right, name)
    
    
    def dfs(node, array):
        node_to_find = array[0]
        finded = find_node(node, node_to_find)
        if array[2] == 1:
            finded.left = TreeNode(array[1])
        else:
            finded.right = TreeNode(array[1])
    
    for array in descriptions:
        dfs(root, array)
    
    #print_tree(root)
    #exit()
    res = []
    def preorder(root):
        if root is None:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return res
    
descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print(build_cookie_tree(descriptions1))
#print_tree(build_cookie_tree(descriptions1))
#print_tree(build_cookie_tree(descriptions2))

    
    
    


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


descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
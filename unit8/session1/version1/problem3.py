class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):

    return helper(root)

def helper(node):
    if node is None:
        return []
    return helper(node.left) + helper(node.right) + [node.val]
#     if root.left:
#         return survey_tree(root.left)
#     elif root.right:
#         return survey_tree(root.right)
#     else:
#         return list.append(root.val)


    
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))
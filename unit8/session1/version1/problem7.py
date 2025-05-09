class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    # total = 0
    # if root is None:
    #     return total
   
    # if root.val > threshold:
    #     total += 1
    # return count_old_growth(root.left, threshold) + count_old_growth(root.right, threshold)
    return helper(root, threshold, 0)
def helper(root, threshold, total):
    if root is None:
        return total

    if root.val > threshold:
        return helper(root.left, threshold, total) + 1 + helper(root.right, threshold, total)
    return helper(root.left, threshold, total) + helper(root.right, threshold, total)

"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)), 
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))
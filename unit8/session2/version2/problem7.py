class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def combine_loot(root1, root2):
    list = []
    curr1 = root1
    curr2 = root2

    values = []
    def inorder(pearls):
        if not pearls:
            return []
        return inorder(pearls.left) + [pearls.val] + inorder(pearls.right)
    list1 = inorder(root1)
    list2 = inorder(root2)
    print(list1)
    print(list2)

    combined = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

"""
    Fork                Coin
   /    \              /    \
Coin    Statue     Anchor   Mirror
"""
root1 = TreeNode("Fork", TreeNode("Coin"), TreeNode("Statue"))
root2 = TreeNode("Coin", TreeNode("Anchor"), TreeNode("Mirror"))


"""
    Fork             Necklace
        \              /    
       Necklace     Fork   
"""
root3 = TreeNode("Fork", None, TreeNode("Necklace"))
root4 = TreeNode("Necklace", TreeNode("Fork"))

print(combine_loot(root1, root2))
print(combine_loot(root3, root4))
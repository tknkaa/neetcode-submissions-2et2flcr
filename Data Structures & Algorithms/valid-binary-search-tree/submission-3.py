# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        max_val = 10000
        min_val = -10000
        self.dfs(root, max_val, min_val)
        return self.valid
    
    def dfs(self, root: Optional[TreeNode], max_val: int, min_val: int):
        if root is None:
            return
        elif not (min_val < root.val < max_val):
            self.valid = False
        else:
            self.dfs(root.left, root.val, min_val)
            self.dfs(root.right, max_val, root.val)
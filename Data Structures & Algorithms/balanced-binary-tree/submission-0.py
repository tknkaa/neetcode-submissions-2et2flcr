# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ok = True
        self.depth(root)
        return self.ok
        
    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if abs(left_depth - right_depth) > 1:
            self.ok = False
        return max(left_depth, right_depth) + 1
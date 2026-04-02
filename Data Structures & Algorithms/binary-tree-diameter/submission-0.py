# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.ans
    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if self.ans < left_depth + right_depth:
            self.ans = left_depth + right_depth
        return max(left_depth, right_depth) + 1
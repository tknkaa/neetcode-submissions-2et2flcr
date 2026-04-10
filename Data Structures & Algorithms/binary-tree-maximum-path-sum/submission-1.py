# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_sum = max(self.dfs(root.left), 0)
        right_sum = max(self.dfs(root.right), 0)
        if left_sum + root.val + right_sum > self.max_sum:
            self.max_sum = left_sum + root.val + right_sum
        return max(left_sum, right_sum) + root.val
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = root
        self.dfs(root, k)
        return self.answer.val
    def dfs(self, root: Optional[TreeNode], k: int):
        if root is None:
            return
        self.dfs(root.left, k)
        self.count += 1
        if self.count == k:
            self.answer = root
            return
        self.dfs(root.right, k)

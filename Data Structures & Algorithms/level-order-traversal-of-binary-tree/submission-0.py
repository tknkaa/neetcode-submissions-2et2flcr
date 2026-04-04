# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans: List[List[int]] = []
        q = deque()
        if root is not None:
            q.append(root)
        while len(q) > 0:
            ans.append(list(map(self.extract, q)))
            size = len(q)
            for _ in range(0, size):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return ans
    def extract(self, node: Optional[TreeNode]):
        if node is None:
            return None
        else:
            return node.val
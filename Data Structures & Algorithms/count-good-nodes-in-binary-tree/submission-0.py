# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans: List[int] = []
        if root is None:
            return 0
        max_val = root.val
        self.recursive(root, max_val)
        return len(self.ans)
    def recursive(self, root: TreeNode, max_val: int) -> None:
        if root is None:
            return None
        print(root.val, max_val)
        if max_val <= root.val:
            self.ans.append(root.val)
            max_val = root.val
        self.recursive(root.left, max_val)
        self.recursive(root.right, max_val)
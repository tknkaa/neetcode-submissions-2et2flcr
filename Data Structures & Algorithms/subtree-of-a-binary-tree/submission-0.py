# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ok = False
        return self.recursive(root, subRoot)
    
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def recursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root is subRoot
        if self.sameTree(root, subRoot):
            self.ok = True
            return True
        return self.recursive(root.left, subRoot) or self.recursive(root.right, subRoot)
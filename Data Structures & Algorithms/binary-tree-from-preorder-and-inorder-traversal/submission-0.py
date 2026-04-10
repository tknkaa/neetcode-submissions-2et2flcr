# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(root.val)
        left_preorder = preorder[1:(pos + 1)]
        left_inorder = inorder[:pos]
        right_preorder = preorder[(pos + 1):] if pos < len(preorder) - 1 else []
        right_inorder = inorder[(pos + 1):] if pos < len(inorder) - 1 else []
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p_visited: List[TreeNode] = []
        self.q_visited: List[TreeNode] = []
        self.search_p(root, p)
        self.search_q(root, q)

        common = []
        while len(self.p_visited) > 0 and len(self.q_visited) > 0:
            a = self.p_visited.pop(0)
            b = self.q_visited.pop(0)
            if a == b:
                common.append(a)
        return common[-1]

    def search_p(self, root: TreeNode, p: TreeNode) -> None:
        self.p_visited.append(root)
        if root.val == p.val:
            return
        elif root.val < p.val:
            self.search_p(root.right, p)
        else:
            self.search_p(root.left, p)
    def search_q(self, root: TreeNode, q: TreeNode) -> None:
        self.q_visited.append(root)
        if root.val == q.val:
            return
        elif root.val < q.val:
            self.search_q(root.right, q)
        else:
            self.search_q(root.left, q)
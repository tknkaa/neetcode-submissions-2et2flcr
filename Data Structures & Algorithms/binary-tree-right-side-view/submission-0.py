# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = deque()
        ans = []
        if root is not None:
            nodes.append(root)
        while len(nodes) > 0:
            size = len(nodes)
            ans.append(nodes[-1].val)
            for _ in range(0, size):
                node = nodes.popleft()
                left_node = node.left
                right_node = node.right
                if left_node is not None:
                    nodes.append(left_node)
                if right_node is not None:
                    nodes.append(right_node)
        return ans
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)

        copy_prev = dummy

        memo = {}

        current = head

        while current != None:
            copy_current = Node(current.val)
            copy_prev.next = copy_current
            memo[current] = copy_current
            current = current.next
            copy_prev = copy_current

        for node in memo.keys():
            if node.random:
                copied = memo[node]
                copied.random = memo[node.random]

        return dummy.next
        
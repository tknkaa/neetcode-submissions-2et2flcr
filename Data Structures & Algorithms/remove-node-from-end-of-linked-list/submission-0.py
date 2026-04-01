# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        slow = dummy
        slow.next = head
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        print(slow.val)
        if slow and slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return dummy.next
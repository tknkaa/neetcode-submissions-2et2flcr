# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next if head != None else head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse
        prev = None
        curr = second
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge
        head1 = head
        head2 = prev
        tmp = head1
        dummy = ListNode(-1)
        curr = dummy
        while head1 != None and head2 != None:
            print(head1.val, head2.val)
            curr.next = head1
            head1 = head1.next
            curr.next.next = head2
            head2 = head2.next
            curr = curr.next.next

        if head1:
            curr.next = head1

        
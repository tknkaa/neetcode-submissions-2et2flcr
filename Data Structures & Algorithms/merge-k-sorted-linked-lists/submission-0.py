# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            i = 1
            tmp = lists[0]
            while i < len(lists):
                tmp = self.mergeTwoList(tmp, lists[i])
                i += 1
            return tmp
        
    def mergeTwoList(self, l0: Optional[ListNode], l1: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while l0 != None and l1 != None:
            if l0.val < l1.val:
                current.next = l0
                current = current.next
                l0 = l0.next
            else:
                current.next = l1
                current = current.next
                l1 = l1.next
        if l0 != None:
            current.next = l0
        else:
            current.next = l1
        return dummy.next
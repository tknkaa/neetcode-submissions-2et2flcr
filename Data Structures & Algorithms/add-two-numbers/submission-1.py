# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        kuriagari = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + kuriagari
            if sum >= 10:
                sum -= 10
                kuriagari = 1
            else:
                kuriagari = 0
            current.next = ListNode(sum)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        if l1 != None:
            while l1 != None:
                sum = l1.val + kuriagari
                if sum >= 10:
                    sum -= 10
                    kuriagari = 1
                else:
                    kuriagari = 0
                current.next = ListNode(sum)
                current = current.next
                l1 = l1.next
        if l2 != None:
            while l2 != None:
                sum = l2.val + kuriagari
                if sum >= 10:
                    sum -= 10
                    kuriagari = 1
                else:
                    kuriagari = 0
                current.next = ListNode(sum)
                current = current.next
                l2 = l2.next 
        if kuriagari == 1:
            current.next = ListNode(1)          


        return dummy.next

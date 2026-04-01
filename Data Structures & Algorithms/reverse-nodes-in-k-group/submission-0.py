# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        curr_head = head

        while True:
            curr_tail = get_kth(prev_tail, k)
            # print(curr_tail.val)
            if curr_tail == None:
                break
                
            prev = prev_tail
            curr = curr_head

            while curr != curr_tail:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # curr == curr_tail
            next_head = curr.next
            curr_tail.next = prev
            prev_tail.next = curr_tail

            curr_head.next = next_head
            prev_tail = curr_head

            curr_head = next_head
        
        return dummy.next
            


def get_kth(prev_tail: Optional[ListNode], k: int) -> Optional[ListNode]:
    curr = prev_tail
    while k > 0:
        curr = curr.next
        if curr == None:
            return None
        k -= 1
    return curr
                    

                
        
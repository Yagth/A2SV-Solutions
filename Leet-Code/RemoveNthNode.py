# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        curr  = head
        prev  = dummy
        length = 0

        while curr:
            curr = curr.next
            length += 1
        
        i    = length - n
        curr = dummy.next
        for j in range(i):
            prev = curr
            curr = curr.next

        prev.next = curr.next
        return dummy.next

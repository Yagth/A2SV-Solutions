# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = prev.next if prev != None else None

        while curr != None:
            if prev.val == curr.val:
                prev.next = curr.next
                curr      = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        size = 0

        while curr != None:
            size += 1

            curr = curr.next
        while size > 0:
            curr = head
            i = size
            while i > 1:
                temp = curr.val
                curr.val = curr.next.val
                curr.next.val = temp
                curr = curr.next
                i -= 1
            size-=1
        return head


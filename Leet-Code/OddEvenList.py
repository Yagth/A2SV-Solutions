# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead  = head
        curr     = head
        prevNode = None
        index    = 1

        while curr != None:
            if index % 2 != 0:
                if prevNode != None:
                    prevNode.next = curr.next
                    curr.next     = oddHead.next
                    oddHead.next  = curr
                    oddHead       = curr
                    curr          = prevNode.next
                else:
                    prevNode = curr
                    curr     = curr.next
            else:
                prevNode = curr
                curr     = curr.next
            
            index += 1
        return head

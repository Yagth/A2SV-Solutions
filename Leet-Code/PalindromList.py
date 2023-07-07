# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palList = []
        node = head

        while node != None:
            palList.append(node.val)
            node = node.next
        
        start = 0
        end   = len(palList)-1

        while start <= end:
            if palList[start] != palList[end]:
                return False
            start += 1
            end   -= 1
        return True

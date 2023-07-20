# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        k = k % length if length > 0 else 0
        while k > 0:
            #Rotating the linked list
            curr = head
            temp = curr.val if curr else -200
            while curr and curr.next:
                temp, curr.next.val = curr.next.val, temp
                curr = curr.next
            if head:
                head.val = temp
            k -= 1
        return head 

# Alternative answer

# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
#         if not head:
#             return None
        
#         lastElement = head
#         length = 1
#         # get the length of the list and the last node in the list
#         while ( lastElement.next ):
#             lastElement = lastElement.next
#             length += 1

#         # If k is equal to the length of the list then k == 0
#         # ElIf k is greater than the length of the list then k = k % length
#         k = k % length
            
#         # Set the last node to point to head node
#         # The list is now a circular linked list with last node pointing to first node
#         lastElement.next = head
        
#         # Traverse the list to get to the node just before the ( length - k )th node.
#         # Example: In 1->2->3->4->5, and k = 2
#         #          we need to get to the Node(3)
#         tempNode = head
#         for _ in range( length - k - 1 ):
#             tempNode = tempNode.next
        
#         # Get the next node from the tempNode and then set the tempNode.next as None
#         # Example: In 1->2->3->4->5, and k = 2
#         #          tempNode = Node(3)
#         #          answer = Node(3).next => Node(4)
#         #          Node(3).next = None ( cut the linked list from here )
#         answer = tempNode.next
#         tempNode.next = None
        
#         return answer


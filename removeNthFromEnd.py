# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        first = head 
        second = head
        
        for i in range(n):
            first = first.next
        
        if not first:
            return second.next
            
        while(first.next):       #to be in position to delete a node
            first = first.next
            second = second.next     
        
        #deletion process 
        second.next = second.next.next
        
        return head
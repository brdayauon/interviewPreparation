# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        current = head
        
        if current == None:
            return None
        
        current.next = self.removeElements(current.next, val)
        
        if current.val == val:
            return current.next
        
        return current
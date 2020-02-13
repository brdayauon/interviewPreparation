# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        has_Cycle = False
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
            if slow == fast:
                has_Cycle = True 
                break 
                
        
        if not has_Cycle:
            return None
        
        while head != fast:
            head = head.next 
            fast = fast.next 
            
        return head 
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        totalSum = 0
        largestLength = 0
        seenSum = {}
        
        for i in range(len(nums)):
            totalSum += nums[i]
            
            if totalSum == k:
                largestLength = i + 1
                
            requiredNumber = totalSum - k
            if requiredNumber in seenSum:
                largestLength = max(largestLength, i - seenSum[requiredNumber])
            
            if totalSum not in seenSum:
                seenSum[totalSum] = i
        return largestLength
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1 
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        if l2.val <= l1.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
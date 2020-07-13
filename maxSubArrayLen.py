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
        
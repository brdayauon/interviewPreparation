class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0
        
        for i in nums:
            prevMax, currMax = max(currMax + i, prevMax), prevMax
            
        return prevMax
        
        
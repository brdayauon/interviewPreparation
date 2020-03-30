class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        maxProf = 0
        minPrice = prices[0]
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProf:
                maxProf = prices[i] - minPrice
                
        return maxProf



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        
        right = 1
        for i in range (len(nums)-2,-1,-1):
            right *= nums[i+1]
            res[i] *= right
        return res
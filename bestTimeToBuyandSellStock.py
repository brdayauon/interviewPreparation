class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i]-minPrice > maxProfit:
                maxProfit += prices[i] - minPrice
                
        return maxProfit
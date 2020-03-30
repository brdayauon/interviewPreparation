class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        diffCandy = set(candies)
        
        
        return min(len(diffCandy), len(candies)//2)
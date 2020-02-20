class Solution:
    def isPerfectSquare(self, num: int) -> bool:    
        if num < 2:
            return True
        left = 0
        right = num 
         
        while left <= right:
            x = left + (right - left) // 2
            
            if x*x == num:
                return True
            elif x*x < num:
                left = x + 1
            else:
                right = x - 1
                
        return False
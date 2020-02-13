from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        
        for i in nums:
            frequency[i] += 1
            
        for i,keys in frequency.items():
            if keys == 1:
                return i
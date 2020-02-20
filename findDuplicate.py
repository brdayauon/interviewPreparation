class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs = {}
        
        for numbers in nums:
            if numbers not in hs:
                hs[numbers] = 1
            else:
                return numbers
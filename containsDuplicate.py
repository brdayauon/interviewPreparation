class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        
        for i in nums:
            if i not in hs:
                hs[i] = i
            else:
                return True
            
        return False
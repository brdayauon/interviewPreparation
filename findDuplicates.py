class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hs = {} 
        res = []
        
        for i in nums:
            if i not in hs:
                hs[i] = 1
            else:
                res.append(i)
        return res
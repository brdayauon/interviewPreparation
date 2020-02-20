class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hs = {}
        res = []
        
        for i in nums:
            if i not in hs:
                hs[i] = 1
            else:
                hs[i] += 1 
        
        for i in hs:
            if hs[i] > len(nums) // 3:
                res.append(i)
       # res.sort()
        return res
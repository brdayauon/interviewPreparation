class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i,keys in enumerate(nums):
            if target-keys in hm:
                return [hm[target-keys], i]
            
            else:
                hm[keys] = i
                
            
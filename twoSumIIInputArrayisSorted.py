class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        
        for i,keys in enumerate(numbers):
            if target-keys in hm:
                return [hm[target-keys]+1,i+1]
            else:
                hm[keys] = i
                
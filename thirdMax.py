class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums)) #gets rid of duplicates
        
        nums.sort(reverse=True)
        
        if len(nums) == 3:  #example 1
            return min(nums)
        elif len(nums) == 0:  #edge case
            return -1
        elif len(nums) < 3: #example 2
            return max(nums) 
        
        nums.pop(0)  #gets rid of nums[0]
        nums.pop(0)
        return nums[0]
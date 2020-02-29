class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pivot],nums[i] = nums[i], nums[pivot]
                pivot += 1
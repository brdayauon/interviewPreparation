class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)    #After reversing all numbers 
        self.reverse(nums, 0, k-1)          #After reversing first k numbers 
        self.reverse(nums,k,len(nums)-1)    #After revering last n-k numbers  
        
        
    def reverse(self, nums: List[int], start, end):
        while (start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
            
            
    #k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.
    
    
    
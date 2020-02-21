class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.qSort(nums, 0, len(nums)-1)
    
    def qSort(self, arr: List[int], low, high):
        if low < high:
            pi = self.partition(arr,low,high)
            self.qSort(arr,low,pi-1)
            self.qSort(arr,pi+1,high)
            
    def partition(self, arr: List[int], low, high):
        pivot = arr[high]
        
        i = low - 1
        
        for j in range(low,high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        
        return i + 1
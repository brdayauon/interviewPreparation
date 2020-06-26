class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        max = 5000
        res = []
        arr.sort()
        
        
        for i in range(0,len(arr)):
            if max - arr[i] > 0:
                max -= arr[i]
                res.append(arr[i])
                
        return len(res)
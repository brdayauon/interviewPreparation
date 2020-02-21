class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        res = [] 
        
        for i in nums:
            if i not in hs:
                hs[i] = 1
            else:
                hs[i] += 1 
        
        print (hs)
        sorted_res = sorted(hs, key=lambda x : hs[x])     # Sort hashmap based on values
        sorted_res =  sorted_res[::-1]                      # Reverse the list

        for i in range(0,k):
            res.append(sorted_res[i])
            
        return res
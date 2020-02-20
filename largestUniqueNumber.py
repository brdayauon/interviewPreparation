class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        hs = {}
        res = []
        
        
        for i in A:
            if i not in hs:
                hs[i] = 1
            else:
                hs[i] += 1 
                
        for i in hs:
            if hs[i] == 1:
                res.append(i)
                
        if len(res) == 0:
            return -1
        
        res.sort()
        
        return res[-1]
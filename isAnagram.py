class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        hs1 = {}
        
        if len(s) != len(t):
            return False
        
        for letters in s:
            if letters not in hs:
                hs[letters] = 1
            else:
                hs[letters] += 1
                
        for letters in t:
            if letters not in hs1:
                hs1[letters] = 1
            else:
                hs1[letters] += 1
    
        if hs == hs1:
            return True
        
        return False
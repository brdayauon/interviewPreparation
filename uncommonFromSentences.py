

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        res = []        
        hm = {}
        ab = A.split() + B.split()
        
        for words in ab:
            if words not in hm:
                hm[words] = 1
            else:
                hm[words] += 1
        
        for k,v in hm.items():
            if v == 1:
                res.append(str(k))
                
        return res

        
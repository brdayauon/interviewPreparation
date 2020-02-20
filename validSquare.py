class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        hs = set()
        
        if self.isSame(p1,p2) or self.isSame(p1,p3) or self.isSame(p1, p4) or self.isSame(p2,p3) or self.isSame(p3, p4) or self.isSame(p2,p4):
            return False
        
        hs.add(self.dis(p1,p2))
        hs.add(self.dis(p1,p3))
        hs.add(self.dis(p1,p4))
        hs.add(self.dis(p2,p3))
        hs.add(self.dis(p2,p4))
        hs.add(self.dis(p3,p4))
        
        return len(hs) == 2
        
    def isSame(self, p1: List[int], p2: List[int]):
        return p1[0] == p2[0] and p1[1] == p2[1]
        
    def dis(self, p1: List [int], p2: List[int]):
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
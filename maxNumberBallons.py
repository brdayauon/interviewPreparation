import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hs = collections.Counter(text)
        
        return min(hs['a'],hs['b'],hs['l']//2, hs['o']//2, hs['n'])
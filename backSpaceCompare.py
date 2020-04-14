class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #have two stacks
        s = []
        t = [] 
        
        #iterate through the two strings
        for i in range(0,len(S)):
            if S[i] == "#" and len(s) == 0:
                continue
            if S[i] == "#":
                s.pop()
                continue
            s.append(S[i])
            
            
        for i in range(0,len(T)):
            if T[i] == "#" and len(t) == 0:
                continue
            if T[i] == "#":
                t.pop()
                continue
            t.append(T[i])
        
        
        return t == s
            
        #"xywrrmp"
        #"xywrrmu#p"
            
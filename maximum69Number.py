class Solution:
    def maximum69Number (self, num: int) -> int:
        number = list(str(num))
      
        
        for i in range(0,len(number)):            
            if number[i] != "9":
                number[i] = "9"
                break
                
        return int(''.join(number))
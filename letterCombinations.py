class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a','b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []
        def backtrack(combination, next_digits):
            #no more digits to check
            if len(next_digits) == 0:
                output.append(combination)
            #still to check
            else:
                for letters in phone[next_digits[0]]:
                    backtrack(combination + letters, next_digits[1:])
                    
        
        if digits:
            backtrack("", digits)
            
        return output
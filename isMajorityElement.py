class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        majorityElement = len(nums) // 2
        
        hs = {}     #initialize hashset/hashmap
        res = []    #initialize empty list
        
        for numbers in nums:   #iterate through the list 
            if numbers not in hs: #if numbers not in hs set to 1
                hs[numbers] = 1
            elif numbers in hs: #if it already in hashset/map, increment it
                hs[numbers] += 1
                
        for numbers in hs:       #increment hs 
            if numbers == target:   #if numbers is == target (parameter of question)
                if hs[numbers] > majorityElement: #if it is greater than output true
                    return True
            
        return False
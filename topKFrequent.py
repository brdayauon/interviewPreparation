class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         hm = {}
#         res = []
        
#         for i in nums:
#             if i not in hm:
#                 hm[i] = 1
#             else:
#                 hm[i] += 1
                
#         sortedRes = sorted(hm, key = lambda x: hm[x]) #sort hashmap based on values
#         sortedRes = sortedRes[::-1]
        
#         for i in range(0,k):
#             res.append(sortedRes[i])
            
#         return res

          #USING COUNT AND HEAP
         count = collections.Counter(nums)
         return heapq.nlargest(k, count.keys(), key = count.get)
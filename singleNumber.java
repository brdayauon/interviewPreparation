class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        
       // for i in nums:
        for(int i=0; i < nums.length; i++){
                   //  if i not in freq:
            if(!hm.containsKey(nums[i])){
                       //      freq[i] = 1
                hm.put(nums[i],1);
            }
            else{
       //  else:
       //      freq[i] += 1
            int temp = hm.get(nums[i]);
            temp += 1;
            hm.put(nums[i], temp);
            }
        }
        
        // for k,v in freq.items():
        Iterator it = hm.entrySet().iterator();
        while(it.hasNext()){
            Map.Entry pair = (Map.Entry)it.next();
            int val = (int)pair.getValue();
            int key = (int)pair.getKey();
        //     if v == 1:
        //         return k
            if (val == 1){
                return key;
            }
        }
        return -1;
    }
}
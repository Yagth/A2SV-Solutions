class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        
        for(int i = 0; i<nums.length; i++){
            if(nums[i] % 2 == 0) nums[i] = 0;
            else nums[i] = 1;
        }
        
        int answer = subarraySum(nums,k);
        return answer;
        
    }
    
    public int subarraySum(int[] nums, int k) {
        int answer = 0, prefixSum = 0;
        Map<Integer, Integer> prefixSumsFrequency = new HashMap<>();
        prefixSumsFrequency.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            prefixSum += nums[i];
            answer += prefixSumsFrequency.getOrDefault(prefixSum - k, 0);
            prefixSumsFrequency.put(prefixSum, prefixSumsFrequency.getOrDefault(prefixSum, 0) + 1);
        }
        return answer;
    }
}
class Solution {
    private int i = 0;
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int[] answer = new int[size];
        int[] prefix = new int[size];
        int[] suffix = new int[size];
        
        prefix[0] = 1;
        suffix[size - 1] = 1;
        
        for(int i = 0; i<size - 1; i++){
            prefix[i+1] = prefix[i] * nums[i];
        }
        
        for(int i = size - 1; i>0; i--){
            suffix[i-1] = suffix[i] * nums[i];
        }
        
        for(int i = 0; i<size; i++){
            answer[i] = prefix[i] * suffix[i];
        }
        
        return answer;
    }
}
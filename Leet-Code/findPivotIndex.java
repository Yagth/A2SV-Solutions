
class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;

        for(int num : nums ) total += num;

        int curSum = 0;
        for(int i = 0; i<nums.length; i++){
            if(curSum == (total - curSum) - nums[i])
                return i;
            else curSum += nums[i];
        }
        return -1;
    }
}
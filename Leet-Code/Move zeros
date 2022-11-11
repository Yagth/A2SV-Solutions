class Solution {
    public void moveZeroes(int[] nums) {
        int zeros = 0;
        int n = nums.length;
        Stack<Integer> stack = new Stack();
        
        for(int i = 0; i<n; i++){
            if(nums[i] != 0)
                stack.push(nums[i]);
            else zeros++;
        }
        
        int size = (n - zeros) - 1;
        
        while(!stack.isEmpty()){
            nums[size] = stack.pop(); 
            size -- ;
        }
        
        size = (n - zeros);
        
        while(zeros > 0){
            nums[size] = 0;
            size ++;
            zeros--;
        }
        
    }
}

/*
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroAt = 0
        
        for num in nums:
            if not num == 0:
                nums[lastNonZeroAt] = num
                lastNonZeroAt += 1
                
        for i in range(lastNonZeroAt, len(nums)):
            nums[i] = 0
*/

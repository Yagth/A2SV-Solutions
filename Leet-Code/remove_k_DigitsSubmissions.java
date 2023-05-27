class Solution {
    public String removeKdigits(String num, int k) {
        char[] nums = num.toCharArray();
        int i = 0;
        String answer = "";
        Stack<Character> stack = new Stack();
        
        while(i < nums.length){
            try{
                while(stack.peek() > nums[i] && k > 0){
                    stack.pop();
                    k--;
                }
                if(!stack.isEmpty() || nums[i] != '0'){
                    stack.push(nums[i]);
                }    
                i++;
            } catch(Exception ex){
                if(!stack.isEmpty() || nums[i] != '0'){
                    stack.push(nums[i]);
                }
                i++;
            }
        }
        
        while(!stack.isEmpty() && k > 0){
            stack.pop();
            k--;
        }
        
        if(stack.isEmpty()){
            return "0";
        }
        
        while(!stack.isEmpty()){
            answer = stack.pop() + answer;
        }
        
        
        return answer;
        
    }
}

/* 
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k-=1
            stack.append(c)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        try:
            res = str(int(res))
        except:
            "Do nothing"
            
        return res if res else "0"
*/

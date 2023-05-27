class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack();
        int i = 0, n = popped.length;
        
        for(int num : pushed){
            stack.push(num);
            
            while(!stack.isEmpty() && popped[i] == stack.peek()){
                stack.pop();
                i++;
            }
        }
        
        return i == n;
    }
}
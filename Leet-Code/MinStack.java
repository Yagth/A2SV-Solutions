class MinStack {
    Stack<Integer> numbers;
    Stack<Integer> mins;

    public MinStack() {
        numbers = new Stack();
        mins = new Stack();
    }
    
    public void push(int val) {
        try{
            if(val < mins.peek())
                mins.push(val);
        } catch(Exception ex){
            mins.push(val);
        }
        
        numbers.push(val);
    }
    
    public void pop() {
        if(numbers.pop().equals(mins.peek())){
            if(!numbers.contains(mins.peek()))
                mins.pop();
                
        }
    }
    
    public int top() {
        return numbers.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
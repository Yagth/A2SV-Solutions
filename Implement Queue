class MyQueue {
    
    Stack<Integer> lifo;
    Stack<Integer> fifo;

    public MyQueue() {
        lifo = new Stack();
        fifo = new Stack();
    }
    
    public void push(int x) {
        lifo.push(x);
    }
    
    public int pop() {
        int size = lifo.size();
        for(int i = 0; i<size; i++){
            fifo.push(lifo.pop());
        }
        
        int pop = fifo.pop();
        
        for(int i = 0; i<size-1; i++){
            lifo.push(fifo.pop());
        }
        return pop;
    }
    
    public int peek() {
        int size = lifo.size();
        for(int i = 0; i<size; i++){
            fifo.push(lifo.pop());
        }
        
        int peek = fifo.peek();
        
        for(int i = 0; i<size; i++){
            lifo.push(fifo.pop());
        }
        
        return peek;
    }
    
    public boolean empty() {        
        return lifo.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

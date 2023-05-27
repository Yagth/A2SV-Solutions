class Solution {
    public boolean isValid(String s) {
            Stack<Character> bracket = new Stack();
        for(int i = 0; i<s.length(); i++){
            Character c = s.toCharArray()[i];
            switch(c){
                case '(':
                    bracket.push(c);
                    break;
                case '{':
                    bracket.push(c);                    
                    break;
                case '[':
                    bracket.push(c);                    
                    break;
                case ')':
                    if(bracket.empty() || bracket.peek() != '(') return false;
                    else bracket.pop();
                    break;
                case '}':
                    if(bracket.empty() || bracket.peek() != '{') return false;
                    else bracket.pop();                    
                    break;
                case ']':
                    if(bracket.empty() || bracket.peek() != '[') return false;
                    else bracket.pop();                    
                    break;                   
            }
        }
        
        return bracket.empty();
    }
}

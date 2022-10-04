import java.util.Stack;

public class Solution {
    private Stack<String> input = new Stack();
    public int evalRPN(String[] tokens) {
        for(int i = tokens.length - 1; i>-1; i--){
            input.push(tokens[i]);
        }
        int result = calculate();
        return result; 
    }
    
    public boolean isOperator(String c){
        String operator = "+-/*";
        return operator.contains(c);
    }
    
    public int calculate(){
        Stack<Integer> operands = new Stack<>();
        Stack<String> operator = new Stack<>();
        while(!input.empty()){
            String temp = input.pop();
            int tempResult;
            boolean isOperator = isOperator(temp);
            if(!isOperator){
                operands.push(Integer.parseInt(temp));
            } else{
                if(operands.size()>=2){
                    int num2 = operands.pop();
                    int num1 = operands.pop();
                    operator.push(temp);
                    switch(operator.pop()){
                        case "+":
                            tempResult = num1 + num2;
                            operands.push(tempResult);
                            break;
                        case "-":
                            tempResult = num1 - num2;
                            operands.push(tempResult);
                            break;
                        case "/":
                            if(num2 == 0) continue;
                            else {
                                tempResult = num1 / num2;
                                operands.push(tempResult);
                            }
                            break;
                        case "*":
                            tempResult = num1 * num2;
                            operands.push(tempResult);
                            break;  
                    }
                    
                } else{
                    operator.push(temp);
                }
            }
        }

        return operands.pop();
    }
}

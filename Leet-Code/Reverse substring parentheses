import java.util.Stack;
class Solution {
    public static void reverse(char A[], int start, int end){
      if (start < end){
        char ch = A[start];
        A[start] = A[end];
        A[end] = ch;
        reverse(A, start + 1, end - 1);
      }
    }
     
    // Function to return the modified string
    public static String reverseParentheses(String str){
      Stack<Integer> st = new Stack<>();
      int len = str.length();
      for (int i = 0; i < len; i++){
         
        // Push the index of the current
        // opening bracket
        if (str.charAt(i) == '('){
          st.push(i);
        }
        else if (str.charAt(i) == ')'){
          char[] A = str.toCharArray();
          reverse(A, st.pop() + 1, i);
          str = String.copyValueOf(A);
        }
      }
       
      System.out.println("Str so far: "+str);

      // To store the modified string
      String res = "";
      for (int i = 0; i < len; i++){
        if (str.charAt(i) != ')' && str.charAt(i) != '('){
          res += (str.charAt(i));
        }
      }
      return res;
    }
    
  }
class Solution {
    public String sortSentence(String s) {
        String temp[] = s.split(" ");
        String sorted[] = new String[temp.length];
        String sentence = "";
    
        for(int i = 0; i<temp.length; i++){
            String st = temp[i];
            int index = Integer.parseInt(st.substring(st.length()-1)) -1;
            temp[i] = st.substring(0,st.length()-1);
            sorted[index] = temp[i];
        }
        
        for(String st: sorted){
            sentence+=st+" ";
        }
        return sentence.strip();
    }
}

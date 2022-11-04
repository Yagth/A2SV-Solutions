class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0;
        int j = 0;
        int max = 0;
        HashSet<Character> set = new HashSet();
        
        while(j < s.length()){
            if(!set.contains(s.charAt(j))){
                set.add(s.charAt(j));
                j++;
                max = Math.max(max, set.size());
            } else{
                set.remove(s.charAt(i));
                i++;
            }
        }
        
        return max;
    }
}

/* // Same Solution in python 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        i = 0   
        j = 0
        lists = set();
                
        while j < len(s):
            if s[j] not in lists:
                lists.add(s[j])
                j+=1
                maximum = max(maximum, len(lists))
                
            else:
                lists.discard(s[i])
                i+=1
                
        return maximum
 */

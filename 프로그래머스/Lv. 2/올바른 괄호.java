import java.util.*;

class Solution {
    boolean solution(String s) {
        List<Character> stack = new LinkedList<>();
        
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.add('(');
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.remove(stack.size() - 1);
            }
        }
        
        if (stack.size() != 0) {
            return false;
        }
        
        return true;
    }
}

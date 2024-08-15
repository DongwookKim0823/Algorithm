import java.util.*;

public class Solution {
    public List<Integer> solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        for (int num: arr) {
            if (list.isEmpty() || list.get(list.size()-1) != num) {
                list.add(num);
            }
        }

        return list;
    }
}

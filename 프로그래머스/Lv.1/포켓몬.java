import java.util.*;


class Solution {
    public int solution(int[] nums) {

        Set<Integer> uniquePocketmon = new HashSet<>();
        
        for (int num: nums) {
            uniquePocketmon.add(num);
        }
        
        int maxSelectable = nums.length / 2;
        int result = Math.min(maxSelectable, uniquePocketmon.size());
        
        return result;
    }
}

import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[] { priorities[i], i });
        }
        
        int executionOrder = 0;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            boolean hasHigherPriority = false;
            
            for (int[] item : queue) {
                if (item[0] > current[0]) {
                    hasHigherPriority = true;
                    break;
                }
            }
            
            if (hasHigherPriority) {
                queue.add(current);
            } else {
                executionOrder++;
                if (current[1] == location) {
                    return executionOrder;
                }
            }
        }
        
        return -1;
    }
}

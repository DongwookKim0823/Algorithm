import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        
        for (int i: scoville) {
            queue.add(i);
        }
        
        int count = 0;
        while (queue.peek() < K) {
            if (queue.size() < 2) {
                return -1;
            }
            
            int new_score = queue.poll() + queue.poll() * 2;
            queue.add(new_score);
            count++;
        }
        
        return count;
    }
}

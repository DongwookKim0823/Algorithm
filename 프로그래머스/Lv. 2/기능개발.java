import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> progressList = new ArrayList<>();
        List<Integer> speedList = new ArrayList<>();
        
        for (int progress : progresses) {
            progressList.add(progress);
        }
        for (int speed : speeds) {
            speedList.add(speed);
        }
        
        while (!progressList.isEmpty()) {
            
            for (int i = 0; i < progressList.size(); i++) {
                progressList.set(i, progressList.get(i) + speedList.get(i));
            }
            
            int count = 0;
            while (!progressList.isEmpty() && progressList.get(0) >= 100){
                progressList.remove(0);
                speedList.remove(0);
                count++;
            }
            
            if (count > 0) {
                answer.add(count);
            }
        
        }
        
        return answer;
    }
}

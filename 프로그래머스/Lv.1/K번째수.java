import java.util.*;

class Solution {
    public List<Integer> solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        for (int i: array) {
            list.add(i);
        }
        
        for (int i=0; i<commands.length; i++) {            
            List<Integer> subList = new ArrayList<>(list.subList(commands[i][0]-1, commands[i][1]));
            Collections.sort(subList);
            answer.add(subList.get(commands[i][2]-1));
        }
        
        return answer;
    }
}

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> participantMap = new HashMap<>();
        Map<String, Integer> completionMap = new HashMap<>();
        
        for (String person: participant) {
            if (participantMap.containsKey(person)) {
                participantMap.put(person, participantMap.get(person) + 1);
            } else {
                participantMap.put(person, 1);
            }
        }
        
        for (String person: completion) {
            if (completionMap.containsKey(person)) {
                completionMap.put(person, completionMap.get(person) + 1);
            } else {
                completionMap.put(person, 1);
            }
        }
        
        for (String person: participant) {
            if (!completionMap.containsKey(person) || !completionMap.get(person).equals(participantMap.get(person))) {
                return person;
            }
        }
        return "";
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;

public class Main {
    public static int bfs(Map<Integer, List<Integer>> relation, int user) {

        Queue<int[]> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        int depthSum = 0;

        queue.add(new int[]{user, 0});
        visited.add(user);

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currentUser = current[0];
            int count = current[1];
            depthSum += count;

            for (int nextUser: relation.get(currentUser)) {
                if (!visited.contains(nextUser)) {
                    queue.add(new int[]{nextUser, count + 1});
                    visited.add(nextUser);
                }
            }
        }

        return depthSum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<Integer, List<Integer>> relation = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            relation.put(i, new ArrayList<>());
        }

        for (int j = 0; j < M; j++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            relation.get(A).add(B);
            relation.get(B).add(A);
        }

        int[] result = new int[N + 1];
        for (int user = 1; user <= N; user++) {
            result[user] = bfs(relation, user);
        }

        int minIndex = 1;
        for (int i = 2; i <= N; i++) {
            if (result[i] < result[minIndex]) {
                minIndex = i;
            }
        }

        System.out.println(minIndex);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        int[][] dp = new int[num + 1][10];

        for (int i = 1; i < num + 1; i++) {
            dp[i][0] = 1;
        }

        for (int j = 0; j < 10; j++) {
            dp[1][j] = 1;
        }

        for (int i = 2; i < num + 1; i++) {
            for (int j = 1; j < 10; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10007;
            }
        }

        int result = 0;
        for (int j = 0; j < 10; j++) {
            result = (result + dp[num][j]) % 10007;
        }

        System.out.println(result);
    }
}

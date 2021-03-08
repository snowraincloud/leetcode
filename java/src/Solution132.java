import java.util.Arrays;

/**
 * //TODO
 *
 * @author wangjunhao
 **/
public class Solution132 {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] g = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(g[i], true);
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i+1; j < n; j++) {
                g[i][j] = s.charAt(i) == s.charAt(j) && g[i+1][j-1];
            }
        }
        int[] dp = new int[n];
        Arrays.fill(dp, n);
        for (int i = 0; i < n; i++) {
           if (g[0][i]){
               dp[i] = 0;
           }else {
               for (int j = 0; j < i; j++) {
                   if (g[j+1][i]){
                       dp[i] = Math.min(dp[i], dp[j] + 1);
                   }
               }
           }
           
        }
        return dp[n-1];
    }

    public static void main(String[] args) {
        String s = "aab";
        int res = new Solution132().minCut(s);
        System.out.println(res);
    }
}

import java.security.KeyStore;
import java.util.ArrayList;
import java.util.List;

/**
 * //TODO
 *
 * @author wangjunhao
 **/
public class Solution1004 {
    public int longestOnes(int[] A, int K) {
        int l = 0, r = 0;
        while (r < A.length){
            if (A[r++] == 0){
                K--;
            }
            if (K < 0 && A[l++] == 0){
                K++;
            }
        }
        return r - l;
    }

    public int longestOnes1(int[] A, int K) {
        if (A.length == 0){
            return 0;
        }
        List<Integer> list = new ArrayList<>();
        int pre = -1, count = 0, max = 0;
        for (int a : A){
            if (a == pre){
                count += 1;
            }else {
                if (count != 0){
                    if (pre == 1){
                        list.add(count);
                        max = Math.max(count, max);
                    }else {
                        list.add(-count);
                    }
                }
                count = 1;
                pre = a;
            }
        }
        if (pre > 0){
            list.add(count);
            max = Math.max(count, max);
        }else {
            list.add(-count);
        }
        if (K < 1){
            return max;
        }
        K += 1;
        int n = list.size();
        int[][] dp = new int[K][n];
        for (int i = 0; i < n; i++) {
            dp[0][i] = list.get(i);
        }
        if (dp[0][0] > 0){
            for (int i = 1; i < K; i++) {
                dp[i][0] = dp[0][0];
            }
        }else {
            for (int i = 1; i < K; i++) {
                if (i + dp[0][0] < 0){
                    dp[i][0] = i;
                }else {
                    dp[i][0] = -dp[0][0];
                }
            }
        }

        for (int i = 1; i < K; i++) {
            for (int j = 1; j < n; j++) {
                if (dp[0][j] > 0){
                    dp[i][j] = dp[0][j] + dp[i][j-1];
                }else {
                    if (i + dp[0][j] < 0){
                        dp[i][j] = i;
                    }else {
                        dp[i][j] = dp[i + dp[0][j]][j-1] - dp[0][j];
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (dp[K-1][i] > max){
                max = dp[K-1][i];
            }
        }

        return max;
    }

    public static void main(String[] args) {
        int[] A = new int[]{1,1,1,0,0,0,1,1,1,1,0};
        int k = 2;
        int res = new Solution1004().longestOnes(A, k);
        System.out.println(res);
        System.out.println(-1<<2);
    }
}

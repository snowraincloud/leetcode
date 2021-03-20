import java.util.*;

/**
 * //TODO
 *
 * @author wangjunhao
 **/
public class Solution115 {
    public int numDistinct(String s, String t) {
        if (s.length() == 0){
            return 0;
        }
        if (t.length() == 0){
            return 1;
        }
        var sc = s.toCharArray();
        var tc = t.toCharArray();

        int n = t.length();

        var hashmap = new HashMap<Character, List<Integer>>(n >> 1);
        for (int i = 0; i < tc.length; i++) {
            var c = tc[i];
            if (hashmap.containsKey(c)){
                hashmap.get(c).add(i);
            }else {
                hashmap.put(c, new ArrayList<>(Collections.singletonList(i)));
            }
        }

        var res = new int[n];
        for (char c : sc) {
            if (!hashmap.containsKey(c)){
                continue;
            }
            var list = hashmap.get(c);
            for (int i = list.size() - 1; i >= 0; i--) {
                int j = list.get(i);
                if (j == 0){
                    res[0] += 1;
                }else {
                    res[j] += res[j-1];
                }
            }
        }

        return res[n-1];
    }

    public int numDistinct1(String s, String t) {
        // dp[0]表示空串
        int[] dp = new int[t.length() + 1];
        // dp[0]永远是1，因为不管S多长，都只能找到一个空串，与T相等
        dp[0] = 1;

        //t的字典
        int[] map = new int[128];
        Arrays.fill(map, -1);


        //这段代码的寻址就可以从map[s.charAt(i)] 找到索引j 在用next[j] 一直找和 s.charAt(i)相等的字符 其他的就可以跳过了
        //所以这个代码的优化 关键要理解 上面的一维倒算
        int[] nexts = new int[t.length()];
        for(int i = 0 ; i < t.length(); i++){
            int c = t.charAt(i);
            nexts[i] = map[c];
            map[c] = i;
        }

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            for(int j = map[c]; j >= 0; j = nexts[j]){
                dp[j + 1] += dp[j];
            }
        }
        return dp[t.length()];
    }

    public static void main(String[] args) {
        String s = "babgbag";
        String t = "bag";
        int res = new Solution115().numDistinct(s, t);
        System.out.println(res);
    }
}

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/**
 * //TODO
 * https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
 * @author wangjunhao
 **/
public class Solution1047 {
    public String removeDuplicates(String S) {
        Deque<Character> strings = new ArrayDeque<>(S.length() >> 1);
        char[] s = S.toCharArray();
        strings.push('#');
        for (int i = 0; i < s.length; i++) {
            if (strings.peek() == s[i]){
                strings.pop();
            }else {
                strings.push(s[i]);
            }
        }
        StringBuilder stringBuilder = new StringBuilder(strings.size());
        strings.pollLast();
        while (!strings.isEmpty()){
            stringBuilder.append(strings.pollLast());
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        String s = "abbaca";
        String res = new Solution1047().removeDuplicates(s);
        System.out.println(res);
    }
}

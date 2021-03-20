import java.util.ArrayDeque;
import java.util.Deque;

/**
 * //TODO
 * https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/
 * @author wangjunhao
 **/
public class Solution331 {
    public boolean isValidSerialization(String preorder) {
        if (preorder.length() == 0 || "#".equals(preorder)){
            return true;
        }

        String[] arr = preorder.split(",");
        if ("#".equals(arr[0])){
            return arr.length == 1;
        }
        Deque<Integer> stack = new ArrayDeque<Integer>();
        stack.push(0);
        for (int i = 1; i < arr.length; i++) {
            if (stack.isEmpty()){
                return false;
            }
            int father = stack.pop();
            if (father == 0){
                stack.push(1);
            }
            if (!"#".equals(arr[i])){
                stack.push(0);
            }
        }
        return stack.isEmpty();
    }
    public boolean betterIsValidSerialization(String preorder) {
        int n = preorder.length();
        int i = 0;
        int slots = 1;
        while (i < n) {
            if (slots == 0) {
                return false;
            }
            if (preorder.charAt(i) == ',') {
                i++;
            } else if (preorder.charAt(i) == '#'){
                slots--;
                i++;
            } else {
                // 读一个数字
                while (i < n && preorder.charAt(i) != ',') {
                    i++;
                }
                slots++; // slots = slots - 1 + 2
            }
        }
        return slots == 0;
    }


    public static void main(String[] args) {
        String s = "9,#,92,#,#";
        boolean res = new Solution331().isValidSerialization(s);
        System.out.println(res);
    }
}

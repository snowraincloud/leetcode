/**
 * //TODO
 *
 * @author wangjunhao
 **/
public class Solution150 {
    public int evalRPN(String[] tokens) {
        int[] res = new int[tokens.length];
        int i = -1;
        for (String token : tokens) {
            switch (token){
                case "-":
                    res[--i] -= res[i+1];
                    break;
                case "+":
                    res[--i] += res[i+1];
                    break;
                case "*":
                    res[--i] *= res[i+1];
                    break;
                case "/":
                    res[--i] /= res[i+1];
                    break;
                default:
                    res[++i] = Integer.parseInt(token);
            }
        }
        return res[0];
    }
    public static void main(String[] args) {
        String[] tokens = new String[]{"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
        int res = new Solution150().evalRPN(tokens);
        System.out.println(res);
    }
}

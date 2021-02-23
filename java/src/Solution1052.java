import java.util.Arrays;
import java.util.stream.IntStream;

/**
 * //TODO
 *
 * @author wangjunhao
 **/
public class Solution1052 {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        if (customers.length < X){
            return IntStream.of(customers).sum();
        }
        int sum = 0, count = 0;
        for (int k = 0; k < X; k++) {
            if (grumpy[k] == 0){
                sum += customers[k];
            }else {
                count += customers[k];
            }
        }
        int max = count;
        int i = 0, j = X;
        while (j < customers.length){
            if (grumpy[j] == 0){
                sum += customers[j];
            }else {
                count += customers[j];
            }
            if (grumpy[i] == 1){
                count -= customers[i];
            }
            max = Math.max(count, max);
            i++;
            j++;
        }

        return sum + max;
    }

    public static void main(String[] args) {
        int[] customers = new int[]{1,0,1,2,1,1,7,5};
        int[] grumpy = new int[]{0,1,0,1,0,1,0,1};
        int x = 3;
        int res = new Solution1052().maxSatisfied(customers, grumpy, x);
        System.out.println(res);
    }
}

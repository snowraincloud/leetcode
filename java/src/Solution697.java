import java.util.*;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

/**
 * //TODO
 * <a href="https://leetcode-cn.com/problems/degree-of-an-array/">697</a>
 * @author wangjunhao
 **/
public class Solution697 {
    public int findShortestSubArray(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        Map<Integer, int[]> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])){
                map.get(nums[i])[0]++;
                map.get(nums[i])[2] = i;
            }else {
                map.put(nums[i], new int[]{1, i, i});
            }
        }

        int min = 0x3f3f3f3f;
        int max = -1;

        for (Map.Entry<Integer, int[]> entry : map.entrySet()){
            int[] arr = entry.getValue();
            if (arr[0] > max){
                min = arr[2] - arr[1];
                max = arr[0];
            }else if (arr[0] == max && arr[2] - arr[1] < min){
                min = arr[2] - arr[1];
            }
        }

        return min + 1;
    }

    public static void main(String[] args) {
        int[] A = new int[]{1,2,2,3,1,4,2};
        int res = new Solution697().findShortestSubArray(A);
        System.out.println(res);

    }
}

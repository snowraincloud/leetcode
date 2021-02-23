/**
 * //TODO
 *
 * @author wangjunhao
 **/
public class Solution1438 {
    public int longestSubarray(int[] nums, int limit) {
        if (nums.length == 0){
            return 0;
        }
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int res = 0, count = 0;
        int min_i = 0, max_i = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= min){
                min = nums[i];
                min_i = i;
            }
            if (nums[i] >= max){
                max = nums[i];
                max_i = i;
            }
            if (max - min <= limit){
                count++;
            }else {
                res = Math.max(count, res);
                i = Math.min(min_i, max_i) + 1;
                if (i >= nums.length){
                    return res;
                }
                min = nums[i];
                max = nums[i];
                min_i = i;
                max_i = i;
                count = 1;
            }
        }

        return Math.max(count, res);
    }

    public static void main(String[] args) {
        int[] A = new int[]{1,5,6,7,8,10,6,5,6};
        int res = new Solution1438().longestSubarray(A, 4);
        System.out.println(res);
    }
}

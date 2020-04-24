# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

#  

# 示例 1:

# 输入: [7,5,6,4]
# 输出: 5
#  

# 限制：

# 0 <= 数组长度 <= 50000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        def mergeSort(nums):
            if len(nums) == 1:
                return nums, 0
            mid = len(nums) // 2
            count = 0
            left, l_cnt = mergeSort(nums[:mid])
            right, r_cnt = mergeSort(nums[mid:])
            count += l_cnt + r_cnt
            res = list()
            i = j = 0
            n, m = len(left), len(right)
            temp = 0
            while i < n and j < m:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                    count += temp
                    temp = j
                else:
                    res.append(right[j])
                    j += 1
                    temp += 1
            if i < n:
                res.extend(left[i:])
                count += (n - i) * m
            else:
                res.extend(right[j:])

            return res, count
        _, count = mergeSort(nums)
        return count
# 624961946
if __name__ == "__main__":
    solution = Solution()
    res = solution.reversePairs([7,5,6,4])
    print(res)



# 给你一个整数数组 nums 和一个整数 k。

# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

# 请返回这个数组中「优美子数组」的数目。

 

# 示例 1：

# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 示例 2：

# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 示例 3：

# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/

from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        count = 0
        res = 0
        while i < n and j < n:
            while j < n and count != k:
                if nums[j] & 1:
                    count += 1
                j += 1
            left = 0
            while i < n and count == k:
                if nums[i] & 1:
                    count -= 1
                left += 1
                i += 1
            right = 1
            while j < n and not nums[j] & 1:
                right += 1
                j += 1
            res += left * right
        return res

    def numberOfSubarraysA(self, nums: List[int], k: int) -> int:
        odds = [-1]
        odds.extend([i for i in range(len(nums)) if nums[i] & 1])
        odds.append(len(nums))
        res = 0
        for i in range(1, len(odds)-k):
            res += (odds[i] - odds[i-1]) * (odds[i+k] - odds[i+k-1])
        return res

    def numberOfSubarraysAnother(self, nums: List[int], k: int) -> int:
        even = [0] * (len(nums) + 1)
        even[0] = 1
        odd = 0
        res = 0
        for num in nums:
            if num & 1:
                odd += 1
            if odd >= k:
                res += even[odd-k]
            even[odd] += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    res = solution.numberOfSubarraysAnother([91473,45388,24720,35841,29648,77363,86290,58032,53752,87188,34428,85343,19801,73201]
,4)
    print(res)
                
                


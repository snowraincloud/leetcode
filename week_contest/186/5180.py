from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * (len(nums) + k)
        res = -0x3f3f3f3f3f
        pre_max = 0
        for i in range(k, len(dp)):
            if pre_max > 0:
                dp[i] += pre_max
            dp[i] += nums[i-k]
            if pre_max < dp[i]:
                pre_max = dp[i]
            elif pre_max == dp[i-k]:
                pre_max = max(dp[i-k+1:i+1])
            if dp[i] > res:
                res = dp[i]
        return res



if __name__ == "__main__":
    solution = Solution()
    res = solution.constrainedSubsetSum([-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790]
,1)
    print(res)
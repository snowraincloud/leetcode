from typing import List

class Solution:
    def PredictTheWinnerOne(self, nums: List[int]) -> bool:
        def helper(start, end):
            if start == end:
                return nums[start]
            left = nums[start] - helper(start+1, end)
            right = nums[end] - helper(start, end-1)
            return max(left, right)
        return helper(0, len(nums)-1) >= 0
    def PredictTheWinnerTwo(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = {}
        def helper(start, end):
            if (start, end) in dp:
                return dp[(start, end)]
            if start == end:
                return nums[start]
            left = nums[start] - helper(start+1, end)
            right = nums[end] - helper(start, end-1)
            dp[(start, end)] = max(left, right)
            return dp[(start, end)]
        return helper(0, l-1) >= 0
    def PredictTheWinnerThree(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [[0] * l for i in range(l)]
        for i in range(l):
            dp[i][i] = nums[i]
        for i in range(l-2, -1, -1):
            for j in range(i+1, l):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0
        
    def PredictTheWinnerfour(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [0] * l
        for i in range(l-1, -1, -1):
            dp[i] = nums[i]
            for j in range(i+1, l):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[0][-1] >= 0

if __name__ == "__main__":
    s = Solution()
    print(s.PredictTheWinnerThree([1, 5, 233, 7]))
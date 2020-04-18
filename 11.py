# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 说明：你不能倾斜容器，且 n 的值至少为 2。

#  



# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

#  

# 示例：

# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        dp = [0] * n
        dp[1] = min(height[1], height[0])
        for i in range(2, n):
            dp[i] = dp[i-1]
            for j in range(i):
                dp[i] = max(dp[i], min(height[i], height[j]) * (i - j))

        return dp[-1]

    def maxAreaBetter(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            res = max(res, min(height[i], height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res 

if __name__ == "__main__":
    solution = Solution()
    res = solution.maxAreaBetter([1,8,6,2,5,4,8,3,7])
    print(res)
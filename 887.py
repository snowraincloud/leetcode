# 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

# 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

# 你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

# 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

# 你的目标是确切地知道 F 的值是多少。

# 无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

#  

# 示例 1：

# 输入：K = 1, N = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
# 如果它没碎，那么我们肯定知道 F = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
# 示例 2：

# 输入：K = 2, N = 6
# 输出：3
# 示例 3：

# 输入：K = 3, N = 14
# 输出：4
#  

# 提示：

# 1 <= K <= 100
# 1 <= N <= 10000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-egg-drop
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def superEggDropA(self, K: int, N: int) -> int:
        dp = [[0] * (K+1) for i in range(0, N+1)]
        for i in range(1, K+1):
            dp[1][i] = 1
        for i in range(1, N+1):
            dp[i][1] = i
        for i in range(2, N+1):
            for j in range(2, K+1):
                dp[i][j] = 1 + min(max(dp[x-1][j-1], dp[i-x][j]) for x in range(1, i))

        return dp[N][K]

    def superEggDropB(self, K: int, N: int) -> int:
        dp = [[0] * (N+1) for i in range(0, K+1)]
        for i in range(1, N+1):
            dp[1][i] = i
        for i in range(1, K+1):
            dp[i][1] = 1
        for i in range(2, K+1):
            for j in range(2, N+1):
                lo, hi = 1, j
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    broke = dp[i-1][mid-1]
                    not_broke = dp[i][j-mid]
                    if broke < not_broke:
                        lo = mid
                    elif broke > not_broke:
                        hi = mid
                    else:
                        lo = hi = mid
                dp[i][j] = 1 + min(max(dp[i-1][lo-1], dp[i][j-lo]), max(dp[i-1][hi-1], dp[i][j-hi]))
        return dp[K][N]

    def superEggDropC(self, K: int, N: int) -> int:
        dp = list(range(N+1))
        temp_dp = [0] * (N+1)
        for k in range(2, K+1):
            x = 1
            for n in range(1, N+1):
                while x < n and max(dp[x-1], temp_dp[n-x]) >= max(dp[x], temp_dp[n-x-1]):
                    x += 1
                temp_dp[n] = 1 + max(dp[x-1], temp_dp[n-x])

            dp = temp_dp[:]
        return dp[-1]

    def superEggDropAnother(self, K: int, N: int) -> int:
        if N == 1:
            return 1
        f = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, K + 1):
            f[1][i] = 1
        ans = -1
        for n in range(2, N+1):
            for k in range(1, K+1):
                f[n][k] = 1 + f[n-1][k-1] + f[n-1][k]
            if f[n][k] >= N:
                ans = n
                break
        return ans

# 2 100 14
# 3 100 9
# 3 1000 19
# 4 5000 19
# 4 7547 22
if __name__ == "__main__":
    solution = Solution()
    res = solution.superEggDropAnother(4, 7547)
    print(res)
        

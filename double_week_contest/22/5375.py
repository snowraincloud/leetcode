# 某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 [1, k] 之间，且数组中的数字都没有前导 0 。

# 给你字符串 s 和整数 k 。可能会有多种不同的数组恢复结果。

# 按照上述程序，请你返回所有可能输出字符串 s 的数组方案数。

# 由于数组方案数可能会很大，请你返回它对 10^9 + 7 取余 后的结果。

#  

# 示例 1：

# 输入：s = "1000", k = 10000
# 输出：1
# 解释：唯一一种可能的数组方案是 [1000]
# 示例 2：

# 输入：s = "1000", k = 10
# 输出：0
# 解释：不存在任何数组方案满足所有整数都 >= 1 且 <= 10 同时输出结果为 s 。
# 示例 3：

# 输入：s = "1317", k = 2000
# 输出：8
# 解释：可行的数组方案为 [1317]，[131,7]，[13,17]，[1,317]，[13,1,7]，[1,31,7]，[1,3,17]，[1,3,1,7]
# 示例 4：

# 输入：s = "2020", k = 30
# 输出：1
# 解释：唯一可能的数组方案是 [20,20] 。 [2020] 不是可行的数组方案，原因是 2020 > 30 。 [2,020] 也不是可行的数组方案，因为 020 含有前导 0 。
# 示例 5：

# 输入：s = "1234567890", k = 90
# 输出：34
#  

# 提示：

# 1 <= s.length <= 10^5.
# s 只包含数字且不包含前导 0 。
# 1 <= k <= 10^9.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/restore-the-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from functools import lru_cache

class Solution:
    
    def numberOfArrays(self, s: str, k: int) -> int:
        if int(s[1:]) == 0:
            if int(s) <= k:
                return 1
            else:
                return 0
        mod = 1e9+7
        @lru_cache()
        def f(s) -> int:
            if s == "":
                return 1
            ans = 0
            i = 0
            while i < len(s) and int(s[:i+1]) <= k:
                if i < len(s) - 1 and s[i+1] == '0':
                    i += 1
                    continue
                ans += f(s[i+1:])
                i += 1
            return ans % mod
        return f(s)

    def numberOfArraysAnother(self, s: str, k: int) -> int:
        if int(s[1:]) == 0:
            if int(s) <= k:
                return 1
            else:
                return 0
        n = len(s)
        MOD = 1e9+7
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            if s[i] != '0':
                for j in range(i, n):
                    if int(s[i:j+1]) > k:
                        break
                    dp[j+1] += dp[i]
                    dp[j+1] %= MOD
        return int(dp[n])

# "2553462832281151811513004352253111", 456 21752500
if __name__ == "__main__":
    solution = Solution()
    res = solution.numberOfArrays("2553462832281151811513004352253111", 456)
    print(res)



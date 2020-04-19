from functools import lru_cache
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @lru_cache(None)
        def f(n, m, k):
            if k == 0 or n < k:
                return 0
            if n == 1:
                return 1
            ans = 0
            for i in range(1, m):
                ans += f(n-1, i, k-1)
            ans += f(n-1, m, k) * m
            return ans % 1000000007
        ans = 0
        for i in range(1, m+1):
            ans += f(n, i, k)
        return ans % 1000000007

    def numOfArraysAnother(self, n: int, m: int, k: int) -> int:
        res = [[[0] * (k+1) for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, m+1):
            res[1][i][1] = 1
        MOD = 1e9 + 7
        for i in range(2, n+1):
            for j in range(1, m+1):
                for l in range(1, k+1):
                    for o in range(1, m+1):
                        if o < j:
                            res[i][j][l] = (res[i][j][l] + res[i-1][o][l-1]) % MOD
                        else:
                            res[i][o][l] = (res[i][o][l] + res[i-1][o][l]) % MOD
        return int(sum([res[n][i][k] for i in range(1, m+1)]) % MOD)



if __name__ == "__main__":
    solution = Solution()
    res = solution.numOfArrays(50, 100, 25)
    print(res)
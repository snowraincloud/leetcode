

class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 1e9 + 7
        f = [1] + [0] * n
        for coin in [1, 5, 10, 25]:
            for i in range(coin, n+1):
                f[i] += f[i-coin]
        return int(f[n] % mod)

if __name__ == "__main__":
    solution = Solution()
    res = solution.waysToChange(10)
    print(res)


        


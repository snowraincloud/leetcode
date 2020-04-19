class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 2 ** (n-1) * 3 < k:
            return ""
        def f(n, k, c):
            if n == 0:
                return ""
            if c == 'a':
                if k <= 2 ** (n-1):
                    return 'b' + f(n-1, k, 'b')
                else:
                    return 'c' + f(n-1, k - 2 ** (n-1), 'c')
            elif c == 'b':
                if k <= 2 ** (n-1):
                    return 'a' + f(n-1, k, 'a')
                else:
                    return 'c' + f(n-1, k - 2 ** (n-1), 'c')
            else:
                if k <= 2 ** (n-1):
                    return 'a' + f(n-1, k, 'a')
                else:
                    return 'b' + f(n-1, k - 2 ** (n-1), 'b')

        ans = None
        if k <= 2 ** (n-1):
            ans = "a" + f(n-1, k, 'a')
        elif k <= 2 ** (n-1) * 2:
            ans = "b" + f(n-1, k - 2 ** (n-1), 'b')
        else:
            ans = "c" + f(n-1, k - 2 ** (n-1) * 2, 'c')
        return ans


if __name__ == "__main__":
    solution = Solution()
    res = solution.getHappyString(10, 100)
    print(res)
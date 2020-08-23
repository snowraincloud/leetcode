class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n

if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(6, 8))
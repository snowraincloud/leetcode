class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last = 0
        last_v = '0'
        now = 0
        res = 0
        for v in s:
            if v == last_v:
                now += 1
            else: 
                res += min(last, now)
                last, last_v = now, v
                now = 1
        return res + min(last, now)


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBinarySubstrings("10101"))
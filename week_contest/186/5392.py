class Solution:
    def maxScore(self, s: str) -> int:
        one_count = 0
        res = 0
        for c in s:
            if c == '1':
                one_count += 1
        left_zero = 0
        left_one = 0
        for i in range(0, len(s)-1):
            if s[i] == '0':
                left_zero += 1
            else:
                left_one += 1
            if left_zero + (one_count - left_one) > res:
                res = left_zero + (one_count - left_one)
        return res

    

if __name__ == "__main__":
    solution = Solution()
    res = solution.maxScore("00")
    print(res)
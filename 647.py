import re
class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s) -> list:
            s = '@#' + '#'.join(s) + '#$'
            center, right = 0, 0
            res = [0] * len(s)
            for i in range(2, len(s)-1):
                if i < right:
                    res[i] = min(right - i, res[center * 2 - i])
                j = res[i] + 1
                while s[i - j] == s[i + j]:
                    res[i] += 1
                    j += 1
                if i + res[i] > right:
                    center, right = i, i + res[i]
            return res
        return sum([(i+1) // 2 for i in  manacher(s)])

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubstrings("aaa"))

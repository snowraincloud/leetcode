from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = len(digits)
        if not l:
            return []
        letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        def backtrack(i, s):
            nonlocal l, res, letter
            if i == l:
                res.append(s)
                return
            for c in letter[digits[i]]:
                backtrack(i+1, s+c)
        backtrack(0, "")
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
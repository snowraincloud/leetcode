class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        c_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c not in c_map:
                res.append(c)
            elif(not res or c_map[c] != res.pop()):
                return False
        return not res


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("{[]}"))
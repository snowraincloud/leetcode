class Solution:
    def reformat(self, s: str) -> str:
        if len(s) < 2:
            return s
        import re
        num = re.findall("\d", s)
        c = re.findall('\D', s)
        mid = len(s) // 2
        if not mid - 1 <= len(num) <= mid + 1 or len(num) == len(s) or len(c) == len(s):
            return ""
        if len(num) < len(c):
            num, c = c, num
        res = []
        for i in range(len(c)):
            res.append(num[i])
            res.append(c[i])
        if len(num) != len(c):
            res.append(num[-1])
        return ''.join(res)
        
if __name__ == "__main__":
    solution = Solution()
    res = solution.reformat("ec")
    print(res)
        
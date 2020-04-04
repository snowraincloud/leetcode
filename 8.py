class Solution:
    def myAtoi(self, str: str) -> int:
        s = str
        i = 0
        while i != len(s):
            if s[i] == ' ':
                i += 1
            else:
                break
        s = s[i:]
        n = len(s)
        if n == 0 or (s[0] not in "0123456789" and not(s[0] in "-+" and n != 1 and s[1] in "0123456789")) :
            return 0
        ans = []
        i = 0
        if s[i] in ['-', '+']:
            ans.append(s[i])
            i += 1
        while i != n and '0' <= s[i] <= '9':
            ans.append(s[i])
            i += 1

        ans = int(''.join(ans))
        return max(min(ans, (1 << 31) -1), -(1 << 31))

    def myAtoiBetter(self, str: str) -> int:
        import re
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), (1 << 31) - 1), -(1 << 31))


if __name__ == "__main__":
    solution = Solution()
    res = solution.myAtoiBetter(" 987")
    print(res)
        

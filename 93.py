from typing import List


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s)
        if l < 4 or l > 12:
            return []
        if l == 12 or l == 4:
            part = l // 4
            res = []
            for i in range(0, l, part):
                if int(s[i:i+part]) > 255:
                    return []
                else:
                    res.append(s[i:i+part])
            return [".".join(res)]
        res = []
        temp = ['0'] * 4
        def dfs(i, n):
            if n == 4:
                if i == l:
                    res.append(".".join(temp))
                return
            if i == l or n > 4:
                return
            if s[i] == '0':
                temp[n] = s[i]
                dfs(i+1,n+1)
            else:
                for e in range(i+1, min(i+4, l+1)):
                    if 0 < int(s[i:e]) <= 255:
                        temp[n] = s[i:e]
                        dfs(e,n+1)
        dfs(0,0)
        return res
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreIpAddresses("172162541"))
    


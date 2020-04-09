# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

#  

# 示例：

# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> list:
        res = list()
        def generate(n: int, m: int, now: str):
            if n != 0:
                generate(n-1, m+1, now+"(")
                if m != 0:
                    generate(n, m-1, now+")")
            else:
                now += "".join([")" for i in range(m)])
                res.append(now)

        generate(n, 0, "")
        return res
    def generateParenthesisAnother(self, n: int) -> List[str]:
        if not n:
            return []
        db = [None for _ in range(n+1)]
        db[0] = ['']
        for i in range(1, n+1):
            now = []
            for j in range(i):
                left = db[j]
                right = db[i - j - 1]
                for l in left:
                    for r in right:
                        now.append("(" + l + ")" + r)
            db[i] = now 

        return db[n]

if __name__ == "__main__":
    solution = Solution()
    ans = solution.generateParenthesisAnother(3)
    print(ans) 
            

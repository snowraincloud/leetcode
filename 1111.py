class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list:
        ans = list()
        mark = True
        n = len(seq)
        i = 0
        calculate = lambda mark: 0 if mark else 1
        while i < n: 
            if seq[i] == '(':
                ans.append(calculate(mark))
                if seq[i + 1] == ')':
                    ans.append(calculate(mark))
                    i += 1
                else:
                    mark = not mark
            else:
                mark = not mark
                ans.append(calculate(mark))
            i += 1
        return ans
    def maxDepthAfterSplitBetter(self, seq: str) -> list:
        return [i & 1 ^ (c == '(') for i, c in enumerate(seq)]

if __name__ == "__main__":
    solution = Solution()
    res = solution.maxDepthAfterSplitBetter("()((()))()")
    print(res)

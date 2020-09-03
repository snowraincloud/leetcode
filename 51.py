from typing import List
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def f(board, i):
            if i == n:
                ans.append(["".join(i) for i in board])
                return
            for j in range(n):
                mark = False
                for k in range(i-1, -1, -1):
                    if board[k][j] == 'Q':
                        mark = True
                        break
                    temp = i - k
                    if j - temp >= 0 and board[k][j-temp] == 'Q':
                        mark = True
                        break
                    if j + temp < n and board[k][j+temp] == 'Q':
                        mark = True
                        break
                if mark:
                    continue
                board[i][j] = 'Q'
                f(board, i+1)
                board[i][j] = '.'
        f([['.'] * n for i in range(n)], 0)
        return ans
if __name__ == "__main__":
    s = Solution()
    [print(*i, sep="\n") for i in s.solveNQueens(4)]



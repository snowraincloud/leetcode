from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = len(board)
        if l == 0:
            return
        w = len(board[0])
        ignore = set()
        for i in range(w):
            if board[0][i] == 'O':
                ignore.add((0, i))
            if board[l-1][i] == 'O':
                ignore.add((l-1, i))
        for i in range(l):
            if board[i][0] == 'O':
                ignore.add((i, 0))
            if board[i][w-1] == 'O':
                ignore.add((i, w-1))
        ignore_list = list(ignore)
        while ignore_list != []:
            i, j = ignore_list.pop()
            for k, h in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if 0 < k < l and 0 < h < w and board[k][h] == 'O' and (k, h) not in ignore:
                    ignore.add((k, h))
                    ignore_list.append((k, h))
        for i in range(l):
            for j in range(w):
                if board[i][j] == 'O' and (i, j) not in ignore:
                    board[i][j] = 'X'


if __name__ == "__main__":
    solution = Solution()
    q = [["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]
    solution.solve(q)
    for line in q:
        print(line)

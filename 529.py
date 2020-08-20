from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        l = len(board)
        w = len(board[0])
        points = []
        points.append((click[0], click[1]))
        while points:
            x, y = points.pop()
            if board[x][y] == 'M':
                board[x][y] = 'X'
                break
            coordinate = [(i, j) for i, j in [(x-1,y-1), (x-1, y), (x-1,y+1), 
                (x, y-1), (x, y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1)]
                if 0 <= i < l and 0 <= j < w and board[i][j] in ('M', 'E')]
            m = 0
            for i, j in coordinate:
                if board[i][j] == 'M':
                    m += 1
            if m == 0:
                board[x][y] = 'B'
                points.extend(coordinate)
            else:
                board[x][y] = str(m)
        return board

if __name__ == "__main__":
    solution = Solution()
    print(*solution.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],
[3,0]), sep='\n')

class Solution:
    def gameOfLife(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(-1, -1), (-1, 0), (-1, 1), 
                    (0, -1),(0, 1), 
                    (1, -1), (1, 0), (1, 1)]
        n = len(board)
        m = len(board[0]) if n != 0 else 0

        for i in range(n):
            for j in range(m):
                count = 0
                for d_x, d_y in direction:
                    x, y = i + d_x, j + d_y
                    if 0 <= x < n and 0 <= y < m and abs(board[x][y]) == 1:
                        count += 1
                if board[i][j]:
                    board[i][j] = 1 if 2 <= count <= 3 else -1
                else:
                    board[i][j] = 2 if count == 3 else 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

    def gameOfLifeB(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        column = len(board[0])
        neighbors = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for r in range(row):
            for c in range(column):
                lives = 0
                for i, j in neighbors:
                    if 0 <= r+i < row and 0 <= c+j < column:
                        lives += board[r+i][c+j] & 1
                if board[r][c] and lives in [2, 3]:
                    board[r][c] = 3
                if not board[r][c] and lives == 3:
                    board[r][c] = 2
        for r in range(row):
            for c in range(column):
                board[r][c] >>= 1


if __name__ == "__main__":
    solution = Solution()
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    solution.gameOfLife(board)
    print(*board, sep='\n')

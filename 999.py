class Solution:
    def numRookCaptures(self, board: list) -> int:
        if not board:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "R":
                    f_i = e_i = i
                    f_j = e_j = j
                    while f_i != 0 and board[f_i][j] != "B":
                        if board[f_i][j] == "p":
                            count += 1
                            break
                        else:
                            f_i -= 1
                    while e_i != len(board) and board[e_i][j] != "B":
                        if board[e_i][j] == "p":
                            count += 1
                            break
                        else:
                            e_i += 1
                    while f_j != 0 and board[i][f_j] != "B":
                        if board[i][f_j] == "p":
                            count += 1
                            break
                        else:
                            f_j -= 1
                    while e_j != len(board) and board[i][e_j] != "B":
                        if board[i][e_j] == "p":
                            count += 1
                            break
                        else:
                            e_j += 1
                    return count
        return 0
    def numRookCapturesB(self, board: list) -> int:
        if not board:
            return 0
        count = 0
        line = [False] * len(board)
        col = [False] * len(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "R":
                    e_i = i
                    e_j = j
                    if line[i]:
                        count += 1
                    if col[j]:
                        count += 1
                    while e_i != len(board) and board[e_i][j] != "B":
                        if board[e_i][j] == "p":
                            count += 1
                            break
                        else:
                            e_i += 1
                    while e_j != len(board) and board[i][e_j] != "B":
                        if board[i][e_j] == "p":
                            count += 1
                            break
                        else:
                            e_j += 1
                    return count
                if board[i][j] == "p":
                    line[i] = True
                    col[j] = True
                elif board[i][j] == "B":
                    line[i] = False
                    col[j] = False

        return 0
    


if __name__ == "__main__":
    solution = Solution()
    res = solution.numRookCapturesB([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]])
    print(res)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_map = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        x, y = 0, 0
        for move in moves:
            i, j = move_map[move]
            x, y = x + i, y + j
        return x == 0 and y == 0

if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle("LLL"))
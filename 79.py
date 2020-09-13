from typing import List
from collections import deque, defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(board)
        w = len(board[0])
        w_l = len(word)
        mark = False
        visited = set()
        def dfs(i, j, k):
            if k == w_l:
                nonlocal mark
                mark = True
                return
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < l and 0 <= y < w and board[x][y] == word[k] and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y, k+1)
                    visited.remove((x, y))

        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    dfs(i, j, 1)
                    visited.remove((i, j))
                    if mark:
                        return mark
        return mark
    
    # mistake
    def existTwo(self, board: List[List[str]], word: str) -> bool:
        l = len(board)
        w = len(board[0])
        w_l = len(word)
        n = 1
        points = defaultdict(set)
        queue = deque()
        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    queue.append((i, j, 1, n))
                    points[(i, j)].add(n)
                    n += 1
        while queue:
            i, j, k, n = queue.popleft()
            if k == w_l:
                return True
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < l and 0 <= y < w and n not in points[(x, y)] and board[x][y] == word[k]:
                    queue.append((x, y, k+1, n))
                    points[(i, j)].add(n)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.exist(
[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
"ABCESEEEFS"))
class Solution:
    def maxDistance(self, grid: list) -> int:
        n = len(grid)
        if sum(map(sum, grid)) == n * n or sum(map(sum, grid)) == 0:
            return -1 
        import queue
        d_x = [-1, 1, 0, 0]
        d_y = [0, 0, -1, 1]
        q = queue.Queue()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.put((i, j))
        point = None
        while(not q.empty()):
            point = q.get()
            for i in range(4):
                x, y = point[0] + d_x[i], point[1] + d_y[i]
                if  0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = grid[point[0]][point[1]] + 1
                    q.put((x, y))
        return max(map(max, grid)) - 1
        

if __name__ == "__main__":
    solution = Solution()
    res = solution.maxDistance([[0,0,0],[0,0,0],[0,0,0]])
    print(res)
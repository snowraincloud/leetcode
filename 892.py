class Solution:
    def surfaceArea(self, grid: list) -> int:
        n = len(grid)
        if n == 0:
            return 0
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 2
                if i == 0 or grid[i-1][j] < grid[i][j]:
                    res += grid[i][j] if i == 0 else grid[i][j] - grid[i-1][j]
                if i == n-1 or grid[i+1][j] < grid[i][j]:
                    res += grid[i][j] if i == n-1 else grid[i][j] - grid[i+1][j]
                if j == 0 or grid[i][j-1] < grid[i][j]:
                    res += grid[i][j] if j == 0 else grid[i][j] - grid[i][j-1]
                if j == n-1 or grid[i][j+1] < grid[i][j]:
                    res += grid[i][j] if j == n-1 else grid[i][j] - grid[i][j+1]
        return res

    def surfaceAreaOffice(self, grid: list) -> int:
        n = len(grid)
        if n == 0:
            return 0
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 2
                for n_i, n_j in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= n_i < n and 0 <= n_j < n:
                        temp = grid[n_i][n_j]
                    else:
                        temp = 0
                    res += max(grid[i][j] - temp, 0) 
        return res

    def surfaceAreaAnother(self, grid: list) -> int:
        if len(grid) == 0:
            return 0
        import numpy
        def statistics(grid: list) -> int:
            res = 0
            for i in range(len(grid)):
                last = 0
                for j in range(len(grid)):
                    res += abs(grid[i][j] - last)
                    last = grid[i][j]
                res += last
            return res
        return statistics(grid) + statistics(numpy.array(grid).T) + numpy.sign(grid).sum() * 2

if __name__ == "__main__":
    solution = Solution()
    res = solution.surfaceAreaAnother([[1,2],[3,4]])
    print(res)

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        my_map = dict()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    for x, y in [(i-1, j), (i, j-1)]:
                        if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                            if (i, j) in my_map:
                                my_map[my_map[(x,y)]] = my_map[my_map[(i,j)]]
                            else:
                                my_map[(i,j)] = my_map[my_map[(x,y)]]
                    if (i, j) not in my_map:
                        my_map[(i,j)] = (i,j)
        return len(set([v for k, v in my_map.items() if k == v]))

if __name__ == "__main__":
    solution = Solution()
    res = solution.numIslands([["1","1","1","1","1","1","1"],["0","0","0","0","0","0","1"],["1","1","1","1","1","0","1"],["1","0","0","0","1","0","1"],["1","0","1","0","1","0","1"],["1","0","1","1","1","0","1"],["1","1","1","1","1","1","1"]])
    print(res)
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

# 两个相邻元素间的距离为 1 。

# 示例 1:
# 输入:

# 0 0 0
# 0 1 0
# 0 0 0
# 输出:

# 0 0 0
# 0 1 0
# 0 0 0
# 示例 2:
# 输入:

# 0 0 0
# 0 1 0
# 1 1 1
# 输出:

# 0 0 0
# 0 1 0
# 1 2 1
# 注意:

# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/01-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0]) if n else 0
        if not n * m:
            return None
        points = [(i, j)  for i in range(n) for j in range(m) if matrix[i][j] != 0]
        from collections import deque
        for x,y in points:
            count = 0
            around = deque()
            around1 = deque()
            around.append((x, y))
            mark = True
            while mark:
                count += 1
                while around:
                    temp_x, temp_y = around.popleft()
                    for a_x, a_y in [(temp_x - 1, temp_y), (temp_x + 1, temp_y), (temp_x, temp_y - 1), (temp_x, temp_y + 1)]:
                        if 0 <= a_x < n and 0 <= a_y < m and matrix[a_x][a_y] == 0:
                            mark = False
                            break
                        around1.append((a_x, a_y))
                    if not mark:
                        break
                if not mark:
                    break
                count += 1
                while around1:
                    temp_x, temp_y = around1.popleft()
                    for a_x, a_y in [(temp_x - 1, temp_y), (temp_x + 1, temp_y), (temp_x, temp_y - 1), (temp_x, temp_y + 1)]:
                        if 0 <= a_x < n and 0 <= a_y < m and matrix[a_x][a_y] == 0:
                            mark = False
                            break
                        around.append((a_x, a_y))
                    if not mark:
                        break
            matrix[x][y] = count
        return matrix

    def updateMatrixA(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0]) if n else 0
        points = [(i, j)  for i in range(n) for j in range(m) if matrix[i][j] == 0]
        from collections import deque
        around = deque()
        around.extend(points)
        seen = set(points)
        while around:
            x, y = around.popleft()
            for a_x, a_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= a_x < n and 0 <= a_y < m and (a_x, a_y) not in seen:
                    matrix[a_x][a_y] = matrix[x][y] + 1
                    around.append((a_x, a_y))
                    seen.add((a_x, a_y))
        return matrix
                
    def updateMatrixAnother(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0]) if n else 0
        dist = [[10**9] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: 
                    dist[i][j] = 0
        for i in range(n):
            for j in range(m):
                if i - 1 >= 0: 
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j - 1 >= 0:
                     dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i + 1 < n: 
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j + 1 < m:
                     dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist

if __name__ == "__main__":
    solution = Solution()
    res = solution.updateMatrixAnother([
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
        ])
    print(res)
                




# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

#  

# 示例 1：

# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 1：

# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：

# 1 <= n,m <= 100
# 0 <= k <= 20

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#　ps： 应该有数学解法
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        
        import queue
        from functools import reduce
        arr = [[True] * n for i in range(m)]
        que = queue.Queue(n*m)
        que.put((0, 0))
        arr[0][0] = False
        res = 1
        while not que.empty():
            x, y = que.get()
            for x, y in [(x+1, y), (x, y+1)]:
                if 0 <= x < m and 0 <= y < n and arr[x][y]:
                    sum_str = str(x) + str(y)
                    temp_sum = reduce(lambda x,y : int(x)+int(y), sum_str)
                    if temp_sum <= k:
                        que.put((x, y))
                        res += 1
                    arr[x][y] = False
        return res

if __name__ == "__main__":
    solution = Solution()
    ans = solution.movingCount(3, 1, 0)
    print(ans) 
                    
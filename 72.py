# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符
#  

# 示例 1：

# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：

# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/edit-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n * m == 0:
            return n + m
        db = [[0] * m for i in range(n)]
        for i in range(m):
            if word1[0] in word2[:i+1]:
                db[0][i] = i
            else:
                db[0][i] = i + 1
        for i in range(n):
            if word2[0] in word1[:i+1]:
                db[i][0] = i
            else:
                db[i][0] = i + 1
        for i in range(1, n):
            for j in range(1, m):
                db[i][j] = min([db[i][j-1], db[i-1][j], db[i-1][j-1] + (-1 if word1[i] == word2[j] else 0)]) + 1
        return db[n-1][m-1]

    def minDistanceAnother(self, word1, word2):
        from collections import deque 
        visit, dq = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = dq.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                d += 1
                dq.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d),
                           (w1[1:], w2, d)])

if __name__ == "__main__":
    solution = Solution()
    res = solution.minDistanceAnother("intentilon", "execution")
    print(res)
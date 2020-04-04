# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def trap(self, height: list) -> int:
        n = len(height)
        if n in (0, 1, 2):
            return 0
        i = 1
        ans = 0
        while i < n-1:
            u = i-1
            l_max = i
            while u >= 0:
                if height[u] > height[i] and height[u] > height[l_max]:
                    l_max = u
                u -= 1
            if l_max != i:
                o = i+1
                r_max = i
                while o < n:
                    if height[o] > height[i] and height[o] > height[r_max]:
                        r_max = o
                    if height[r_max] >= height[l_max]:
                        break
                    o += 1
            if l_max != i and r_max != i:
                ans += (r_max - i) * min(height[l_max], height[r_max]) - sum(height[i:r_max])
                i = r_max + 1
            else:
                i += 1
        return ans

    def trapModif(self, height: list) -> int:
        n = len(height)
        if n in (0, 1, 2):
            return 0
        i = 1
        ans = 0
        while i < n-1:
            l_max = i - 1 if height[i - 1] > height[i] else i
            if l_max != i:
                o = i + 1
                r_max = i
                while o < n:
                    if height[o] > height[i] and height[o] > height[r_max]:
                        r_max = o
                    if height[r_max] >= height[l_max]:
                        break
                    o += 1
            if l_max != i and r_max != i:
                ans += (r_max - i) * min(height[l_max], height[r_max]) - sum(height[i:r_max])
                i = r_max + 1
            else:
                i += 1
        return ans



# [4,2,0,3,2,5]
if __name__ == "__main__":
    solution = Solution()
    res = solution.trapModif([0,1,0,2,1,0,1,3,2,1,2,1])
    print(res)
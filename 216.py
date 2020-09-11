from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        k -= 1
        def dfs(nums, num, i, rest):
            if i == k and rest == 0:
                ans.append(nums[:])
            elif i < k:
                for j in range(num+1, 10):
                    if j <= rest:
                        nums.append(j)
                        dfs(nums, j, i+1, rest-j)
                        nums.pop()
        dfs([], 0, -1, n)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(*s.combinationSum3(3, 9), sep="\n")
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        l = len(candidates)
        def dfs(begin: int, nums: List[int], rest: int):
            if rest == 0:
                ans.append(nums[:])
                return
            for i in range(begin, l):
                if candidates[i] > rest:
                    break
                if i > begin and candidates[i-1] == candidates[i]:
                    continue
                nums.append(candidates[i])
                dfs(i+1, nums, rest-candidates[i])
                nums.pop()
        dfs(0, [], target)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        judge = set()
        def backtrack(s: int, nums: List[int]):
            if s == target:
                temp = tuple(sorted(nums))
                if temp not in judge:
                    ans.append(nums)
                    judge.add(temp)
            else:
                for i, num in enumerate(candidates):
                    if s + num <= target:
                        backtrack(s+num, nums + [num])
                    else:
                        break
        backtrack(0, [])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(*s.combinationSum([7,3,2], 18), sep="\n")
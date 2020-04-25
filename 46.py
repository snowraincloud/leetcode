from typing import List
from functools import lru_cache
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def f(nums: List[int]):
            if len(nums) <= 1:
                return [nums]
            ans = []
            for i, num in enumerate(nums):
                res = f(nums[:i] + nums[i+1:])
                for one in res:
                    ans.append([num] + one)
            return ans
        return f(nums)

if __name__ == "__main__":
    solution = Solution()
    res = solution.permute([1,2,3])
    print(res)

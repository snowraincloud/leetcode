from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        def f(res, i):
            if i == l:
                ans.append(res[:])
                return
            f(res[:], i+1)
            res.append(nums[i])
            f(res[:], i+1)
        f([], 0)
        return ans
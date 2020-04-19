from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if min(nums) >= 0:
            return 1
        res = 0x7fffffff
        for i in range(len(nums)):
            res = min(res, sum(nums[:i+1]))
        return 1 + (abs(res) if res < 0 else 0)

if __name__ == "__main__":
    solution = Solution()
    res = solution.minStartValue([2,3,5,-5,-1])
    print(res)
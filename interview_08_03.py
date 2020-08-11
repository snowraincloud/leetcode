from typing import List

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1




if __name__ == "__main__":
    solution = Solution()
    print(solution.findMagicIndex([1, 2, 3, 3, 5]))

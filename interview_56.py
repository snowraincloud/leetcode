from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        low_bit = xor & -xor
        a = b = 0
        for num in nums:
            if num & low_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == "__main__":
    solution = Solution()
    res = solution.singleNumbers([1,2,10,4,1,4,3,3])
    print(res)

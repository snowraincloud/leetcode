from typing import List

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        mark = False
        operation = {
            "plus": lambda x,y:x+y,
            "subtract": lambda x,y:x-y,
            "multiply": lambda x,y:x*y,
            "divide": lambda x,y:x/y
        }
        def f(nums):
            nonlocal mark
            if len(nums) == 1:
                # print(nums[0])
                mark = -0.000001 <= nums[0] - 24 <= 0.000001
                return 
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        for o in operation:
                            if o == "divide" and nums[j] == 0:
                                continue
                            temp = [operation[o](nums[i], nums[j])] + [nums[k] for k in range(len(nums)) if k != i and k != j]
                            f(temp)
                            if mark:
                                return
        f(nums)
        return mark

10 

if __name__ == "__main__":
    s = Solution()
    print(s.judgePoint24([1, 2, 1, 2]))
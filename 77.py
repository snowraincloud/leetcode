from typing import List

class Solution:
    # 超出时间限制
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        n += 1
        judge = set()
        def f(nums: List[int]):
            if len(nums) == k:
                temp = tuple(sorted(nums))
                if temp not in judge:
                    ans.append(nums)
                    judge.add(temp)
                return 
            for i in range(1, n):
                if i not in nums:
                    f(nums + [i])
        f([])
        return ans
    
    def combineOne(self, n: int, k: int) -> List[List[int]]:
        ans = []
        n += 1
        judge = set()
        def f(nums: List[int], status:int):
            if len(nums) == k:
                if status not in judge:
                    ans.append(nums)
                    judge.add(status)
                return 
            for i in range(1, n):
                if i not in nums:
                    f(nums + [i], status | (1<<i))
        f([], 0)
        return ans

    def combineTwo(self, n: int, k: int) -> List[List[int]]:
        ans = []
        n += 1
        def f(nums: List[int]):
            if len(nums) == k:
                ans.append(nums)
                return 
            i =nums[-1]+1 if nums else 1
            while i != n:
                f(nums + [i])
                i += 1
        f([])
        return ans
    

if __name__ == "__main__":
    s = Solution()
    print(*s.combineTwo(4,2 ), sep="\n")
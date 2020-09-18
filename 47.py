from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)
        nums.sort()
        marks = [True] * l
        def trackback(sequence):
            if len(sequence) == l:
                ans.append(sequence[:])
                return
            pre = None
            for i in range(l):
                if marks[i] and nums[i] != pre:
                    marks[i] = False
                    sequence.append(nums[i])
                    trackback(sequence)
                    marks[i] = True
                    sequence.pop()
                    pre = nums[i]
        trackback([])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1,1,2]))
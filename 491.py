from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = [[] for i in range(l)]
        for i in range(l-2, -1, -1):
            for j in range(i+1, l):
                if nums[i] <= nums[j]:
                    ans[i].append([nums[i], nums[j]])
                    for k in ans[j]:
                        ans[i].append([nums[i]] + k)
        res = []
        mark = set()
        for i in ans:
            for j in i:
                if tuple(j) not in mark:
                    mark.add(tuple(j))
                    res.append(j)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))
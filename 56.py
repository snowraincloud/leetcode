from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            start, end = intervals[i]
            i += 1
            while i < n and end >= intervals[i][0]:
                end = intervals[i][1] if intervals[i][1] > end else end
                i += 1
            res.append([start, end])
        return res



if __name__ == "__main__":
    solution = Solution()
    res = solution.merge([[1,4],[2,3]])
    print(res)
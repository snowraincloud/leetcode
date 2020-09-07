from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        statistics = defaultdict(int)
        for num in nums:
            statistics[num] += 1
        nums = sorted([(v, k) for k, v in statistics.items()], key=lambda x:-x[0])
        return [nums[i][1] for i in range(k)]

    def topKFrequentHeapSort(self, nums: List[int], k: int) -> List[int]:
        def buildMinHeap(vals: List[tuple]):
            for i in range(len(vals)//2, -1, -1):
                heapify(vals, i)
        
        def heapify(vals: List[tuple], i: int):
            l, r = i*2+1, i*2+2
            i_min = i
            if l < len(vals) and vals[l][0] < vals[i_min][0]:
                i_min = l
            if r < len(vals) and vals[r][0] < vals[i_min][0]:
                i_min = r
            if i_min != i:
                vals[i], vals[i_min] = vals[i_min], vals[i]
                heapify(vals, i_min)
        statistics = defaultdict(int)
        for num in nums:
            statistics[num] += 1
        nums = [(v, k) for k, v in statistics.items()]
        ans = nums[:k]
        buildMinHeap(ans)
        for i in range(k, len(nums)):
            if nums[i][0] > ans[0][0]:
                ans[0] = nums[i]
                heapify(ans, 0)
        return [i[1] for i in ans]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequentHeapSort([1,1,1,2,2,3,], 2))
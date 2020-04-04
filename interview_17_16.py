class Solution:
    def massage(self, nums: list) -> int:
        if not nums: 
            return 0
        n = len(nums)
        if n < 3:
            return max(nums)
        ans = [0] * n
        ans[0] = nums[0]
        ans[1] = nums[1]
        for i in range(2, n):
            ans[i] = max(ans[:i-1]) + nums[i]
        return max(ans[n-2:])

if __name__ == "__main__":
    solution = Solution()
    ans = solution.massage([2,1,4,5,3,1,1,3])
    print(ans)

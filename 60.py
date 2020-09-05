from functools import reduce
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [True for i in range(1, n+1)]
        num = 0
        ans = []
        while any(nums):
            product = 1
            for i in range(1, n-num):
                product *= i
            quotient = k // product
            k = k % product
            if not k:
                quotient -= 1
                k = product
            i = 0
            while quotient:
                if nums[i]:
                    quotient -= 1
                i = (i + 1) % n
            while not nums[i]:
                i = (i + 1) % n
            ans.append(str(i+1))
            nums[i] = False
            num += 1
        return "".join(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(4, 9))        

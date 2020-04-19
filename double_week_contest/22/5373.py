class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        re_list = []
        a, b = 0, 1
        while b <= k:
            re_list.append(b)
            a, b = b, a+b
        if k in re_list:
            return 1
        def f(k, j) -> int:
            if k == 0:
                return 0
            for i in range(j, -1, -1):
                if re_list[i] <= k:
                    return 1 + f(k-re_list[i], i-1)
        
        return f(k, len(re_list) - 1)

    def fib_2(self, num):
        re_list = []
        a, b = 0, 1
        while b <= num:
            re_list.append(b)
            a, b = b, a+b
        return re_list


if __name__ == "__main__":
    solution = Solution()
    res = solution.findMinFibonacciNumbers(20)
    print(res)

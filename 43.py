class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        l1, l2 = len(num1), len(num2)
        l = l1 + l2
        res = ['0'] * l
        for i in range(l1-1, -1, -1):
            index = l - l1 + i
            for j in range(l2-1, -1, -1):
                num = int(num1[i]) * int(num2[j]) + int(res[index])
                offset = 0
                while num > 9:
                    res[index - offset] = str(num)[-1]
                    num = int(str(num)[:-1])
                    offset += 1
                    num += int(res[index-offset])
                else:
                    res[index - offset] = str(num)
                index -= 1
        i = 0
        for i in range(len(res)):
            if res[i] != '0':
                break
        return ''.join(res[i:])
    def multiplyOptimize(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        l1, l2 = len(num1), len(num2)
        l = l1 + l2
        res = [0] * l
        for i in range(l1-1, -1, -1):
            index = l - l1 + i
            for j in range(l2-1, -1, -1):
                num = int(num1[i]) * int(num2[j]) + res[index]
                res[index] = num % 10
                res[index-1] += num // 10 
                index -= 1
        i = 1 if res[0] == 0 else 0
        return ''.join([str(x) for x in res[i:]])

    def multiplyOther(self, num1: str, num2: str) -> str:    
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiplyOptimize("999", "999"))
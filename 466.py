class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        temp = []
        for i in range(len(s1)):
            if s1[i] in s2:
                temp.append(s1[i])
        s1 = ''.join(temp)
        s1 *= n1 
        len_n1 = len(s1)
        len_n2 = len(s2)
        i = 0
        j = 0
        count = 0
        while i < len_n1:
            if s2[j] == s1[i]:
                j += 1
                if j == len_n2:
                    j = 0
                    count += 1
            i += 1        
        return count // n2

    def getMaxRepetitionsAnother(self, s1: str, n1: int, s2: str, n2: int) -> int:
        temp = []
        for i in range(len(s1)):
            if s1[i] in s2:
                temp.append(s1[i])
        s1 = ''.join(temp)
        j = 0
        s1_cnt = 0
        s2_cnt = 0
        recall = dict()
        while True:
            s1_cnt += 1
            for c in s1:
                if s2[j] == c:
                    j += 1
                    if j == len(s2):
                        j = 0
                        s2_cnt += 1
            if s1_cnt == n1:
                return s2_cnt // n2
            if j in recall:
                pre_loop = recall[j]
                in_loop = (s1_cnt - pre_loop[0], s2_cnt - pre_loop[1])
                break
            else:
                recall[j] = (s1_cnt, s2_cnt)
        ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        rest = (n1 - pre_loop[0]) % in_loop[0]
        for i in range(rest):
            for c in s1:
                if s2[j] == c:
                    j += 1
                    if j == len(s2):
                        j = 0
                        ans += 1
        return ans // n2
        
# "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf"
# 1000000
# "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly"
# 100
# ans 303


if __name__ == "__main__":
    solution = Solution()
    res = solution.getMaxRepetitionsAnother("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf", 
    1000000, "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly", 
    100)
    print(res)


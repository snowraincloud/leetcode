# from functools import reduce
# import collections

# my_dict = collections.defaultdict(dict)

# res = reduce(dict.__getitem__, ['a', 'b', 'c', 'd', 'e'], my_dict)

# print(res)

# test = dict()
# test[1] = 2
# print(test[1])
# print(test.get(2))

# import time
# print(int(time.time()))

# test = {
#     'freq': 1
# }

# print(test['freq'])

# def test(node: dict):
#     node['1'] = 2

# my_dict = {
#     '1': 0
# }
# test(my_dict)
# print(my_dict)

# from functools import reduce
# sum_str = str("10") + str("15")
# temp_sum = reduce(lambda x,y : x+y, sum_str)
# print(temp_sum)

# import re
# print("the sky  is blue".split())

# for i in range(1, 1):
#     print(i)

# x, y = [1, 2]

# print(x)
# print(y)

# import collections
# a = collections.defaultdict(int)
# a['1'] += 1
# a['3'] += 1
# a['1'] += 1
# print(a)
print('a' * 2)


def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
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
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

def test(node: dict):
    node['1'] = 2

my_dict = {
    '1': 0
}
test(my_dict)
print(my_dict)
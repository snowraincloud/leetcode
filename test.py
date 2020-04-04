from functools import reduce
import collections

my_dict = collections.defaultdict(dict)

res = reduce(dict.__getitem__, ['a', 'b', 'c', 'd', 'e'], my_dict)

print(res)
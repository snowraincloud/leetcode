# 设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

# get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
# put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

# 进阶：
# 你是否可以在 O(1) 时间复杂度内执行两项操作？

# 示例：

# LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回 1
# cache.put(3, 3);    // 去除 key 2
# cache.get(2);       // 返回 -1 (未找到key 2)
# cache.get(3);       // 返回 3
# cache.put(4, 4);    // 去除 key 1
# cache.get(1);       // 返回 -1 (未找到 key 1)
# cache.get(3);       // 返回 3
# cache.get(4);       // 返回 4

class LFUCache:
    __data = dict()
    __length = None
    __time = 0

    def __init__(self, capacity: int):
        self.__length = capacity
        

    def get(self, key: int) -> int:
        val = self.__data.get(key)
        if val == None:
            return -1
        self.__data[key][1] += 1
        self.__time += 1
        self.__data[key][2] = self.__time
        return self.__data[key][0]

    def put(self, key: int, value: int) -> None:
        val = self.__data.get(key)
        if val != None:
            self.__data[key][0] = value
            self.__data[key][1] += 1
            self.__data[key][2] = self.__time
            return
        if len(self.__data) + 1 > self.__length:
            remove_k = None
            remove_v = [0x3f3f3f3f, self.__time+1]
            for k, v in self.__data.items():
                if v[1] < remove_v[0] or (v[1] == remove_v[0] and v[2] < remove_v[1]):
                    remove_k = k
                    remove_v = [v[1], v[2]]
            self.__data.pop(remove_k)
        self.__time += 1     
        self.__data[key] = [value, 0, self.__time]


# 11 测试用例 提交不通过但是本地测试通过
# if __name__ == "__main__":
#     cache = LFUCache(3)
#     print(cache.put(2, 2))
#     print(cache.put(1, 1))
#     print(cache.get(2))
#     print(cache.get(1))
#     print(cache.get(2))
#     print(cache.put(3, 3))
#     print(cache.put(4, 4))
#     print(cache.get(3))
#     print(cache.get(2))
#     print(cache.get(1))
#     print(cache.get(4))

class hashLink:
    __data = dict()
    __min_freq = 0

    def put(self, node: dict):
        link = self.__data.get(node['freq'])
        if link == None:
            link = {
                'head': None,
                'tail': None,
            }
            self.__data[node['freq']] = link

        node['next'] = self.__data[node['freq']]['head']
        if self.__data[node['freq']]['head'] != None:
            self.__data[node['freq']]['head']['pre'] = node
        self.__data[node['freq']]['head'] = node

        if self.__data[node['freq']]['tail'] == None:
            self.__data[node['freq']]['tail'] = node
        if node['freq'] < self.__min_freq:
            self.__min_freq = node['freq']
    
    def remove(self) -> int:
        res = self.__data[self.__min_freq]['tail']
        self.delete(self.__data[self.__min_freq]['tail'])

        return res['k']

    def delete(self, node: dict) -> None:
        if node['pre'] == None:
            if node['next'] == None:
                self.__data.pop(node['freq'])
            else:
                self.__data[node['freq']]['head'] = node['next']
                node['next']['pre'] = None
        else:
            if node['next'] == None:
                self.__data[node['freq']]['tail'] = node['pre']
                node['pre']['next'] = None
            else:
                node['pre']['next'] = node['next']
                node['next']['pre'] = node['pre']

    def update(self, node: dict) -> None:
        self.delete(node)
        if self.__min_freq not in self.__data and node['freq'] == self.__min_freq:
            self.__min_freq += 1 
        node['freq'] += 1
        node['pre'] = None
        node['next'] = None
        self.put(node)
        
            
class LFUCacheBetter:
    def __init__(self, capacity: int):
        self.__len = capacity
        self.__data = dict()
        self.__hashlink = hashLink()

    def get(self, key: int) -> int:
        if key in self.__data:
            self.__hashlink.update(self.__data[key])
            return self.__data[key]['v']
        return -1

    def put(self, key: int, value: int) -> None:
        if not self.__len:
            return 
        if len(self.__data) + 1 > self.__len:
            k = self.__hashlink.remove()
            self.__data.pop(k)
        if key in self.__data:
            self.__data[key]['v'] = value
            self.__hashlink.update(self.__data[key])
        else:
            self.__data[key] = {
                'freq': 0,
                'k': key,
                'v': value,
                'pre': None,
                'next': None
            }
            self.__hashlink.put(self.__data[key])

# 8 测试用例报 4 keyerror 错误 本地运行无误
if __name__ == "__main__":
    # cache = LFUCacheBetter(3)
    # print(cache.put(2, 2))
    # print(cache.put(1, 1))
    # print(cache.get(2))
    # print(cache.get(1))
    # print(cache.get(2))
    # print(cache.put(3, 3))
    # print(cache.put(4, 4))
    # print(cache.get(3))
    # print(cache.get(2))
    # print(cache.get(1))
    # print(cache.get(4))
    
    # cache = LFUCacheBetter(2)
    # print(cache.put(2, 1))
    # print(cache.put(2, 2))
    # print(cache.get(2))
    # print(cache.put(1, 1))
    # print(cache.put(4, 4))
    # print(cache.get(2))

    cache = LFUCacheBetter(1)
    print(cache.put(2, 1))
    print(cache.get(2))
    print(cache.put(3, 2))
    print(cache.get(2))
    print(cache.get(3))
# None
# None
# 2
# 1
# 2
# None
# None
# -1
# 2
# 1
# 4
class Solution:
    def minimumLengthEncoding(self, words: list) -> int:
        if not words:
            return 0
        words.sort(key = lambda word: word[::-1])
        res = 0
        for i in range(len(words) - 1):
            if words[i+1].endswith(words[i]):
                pass
            else:
                res += len(words[i]) + 1
        return res + len(words[-1]) + 1
    
    def minimumLengthEncodingB(self, words: list) -> int:
        import collections
        from functools import reduce
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        
        # nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        nodes = []
        for word in words:
            nodes.append(reduce(dict.__getitem__, word[::-1], trie))
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

if __name__ == "__main__":
    solution = Solution()
    res = solution.minimumLengthEncodingB(["atime", "aatime", "btime"])
    print(res)
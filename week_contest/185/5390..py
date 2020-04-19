class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 != 0:
            return -1
        frogs = dict()
        count = 0
        c_map = {
            'c': 'k',
            'r': 'c',
            'o': 'r',
            'a': 'o',
            'k': 'a'
        }
        for c in croakOfFrogs:
            pre = c_map[c]
            if pre in frogs:
                if frogs[pre] == 1:
                    frogs.pop(pre)
                else:
                    frogs[pre] -= 1
            else:
                count += 1
            if c not in frogs:
                frogs[c] = 1
            else:
                frogs[c] += 1
        if len(frogs) != 1:
            return -1
        return count


if __name__ == "__main__":
    solution = Solution()
    res = solution.minNumberOfFrogs("croakcroa")
    print(res)
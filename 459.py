class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        if l < 2:
            return False
        for i in range(1, l//2+1):
            if s[i] == s[0]:
                j = 1
                while j != i and i+j < l and s[i+j] == s[j]:
                    j += 1
                if j == i:
                    ans = [c for c in s.split(s[:j]) if c != '']
                    if not ans:
                        return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("abcabcabcabc"))
                
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s)//2, 0, -1):
            if s[:i] == s[2*i:i:-1]:
                return s[:2*i:-1] + s
            elif s[:i] == s[2*i-1:i-1:-1]:
                return s[:2*i-1:-1] + s
        return s[:0:-1] + s
if __name__ == "__main__":
    s = Solution()
    print(s.shortestPalindrome("abcd"))
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([c[::-1] for c in s.split()])

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))


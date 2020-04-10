class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        srt_list = s.split()
        srt_list.reverse()
        return " ".join(srt_list)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverseWords("a good   example")
    print(ans) 
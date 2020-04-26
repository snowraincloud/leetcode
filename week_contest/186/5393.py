from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        elif k == 1:
            return cardPoints[0] if cardPoints[0] >= cardPoints[-1] else cardPoints[-1]
        
        def f(cardPoints, i, j, k):
            if k == 0 or i > j:
                return 0
            
            sum1 = cardPoints[i] + f(cardPoints, i+1, j, k-1)
            sum2 = cardPoints[j] + f(cardPoints, i, j-1, k-1)
            return sum1 if sum1 > sum2 else sum2
        
        return f(cardPoints, 0, len(cardPoints)-1, k)


    def maxScoreAnother(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        elif k == 1:
            return cardPoints[0] if cardPoints[0] >= cardPoints[-1] else cardPoints[-1]
        pre_sum = [0]
        for i in range(0, len(cardPoints)):
            pre_sum.append(pre_sum[-1] + cardPoints[i])
        min_sum = 0x7fffffff
        for i in range(len(cardPoints) - k, len(cardPoints)+1):
            if pre_sum[i] - pre_sum[i - len(cardPoints) + k] < min_sum:
                min_sum = pre_sum[i] - pre_sum[i - len(cardPoints) + k]
        return pre_sum[-1] - min_sum



if __name__ == "__main__":
    solution = Solution()
    res = solution.maxScoreAnother([96,90,41,82,39,74,64,50,30],
8)
    print(res)
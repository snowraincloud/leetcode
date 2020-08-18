from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        stack = list()
        stack.append((sr, sc))
        image[sr][sc] = newColor
        l = len(image)
        w = len(image[sr])
        while stack:
            x, y = stack.pop()
            for j, k in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                if 0 <= j < l and 0 <= k < w and image[j][k] == oldColor:
                    image[j][k] = newColor
                    stack.append((j, k))
        return image


if __name__ == "__main__":
    solution = Solution()
    print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
from typing import List
import collections
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        if not boxes:
            return 0
        boxes_merge = []
        num = 0
        pre = boxes[0]
        box_map = collections.defaultdict(int)
        for box in boxes:
            if box == pre:
                num += 1
            else:
                boxes_merge.append((pre, num))
                box_map[pre] += 1
                pre, num = box, 1
        boxes_merge.append((pre, num))
        box_map[pre] += 1
        if len(boxes_merge) == len(boxes):
            return len(boxes)
        ans = 0
        temp = []
        for val, num in boxes_merge:
            

        
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeBoxes([1,3,2,2,2,3,4,3,1]))
    
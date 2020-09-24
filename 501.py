from utils.tree import TreeNode, buildTree
from typing import List

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        ans = []
        ans_count = 0
        cur = None
        cur_count = 0
        def f(node):
            if not node:
                return
            f(node.left)
            nonlocal ans, cur, ans_count, cur_count
            if node.val == cur:
                cur_count += 1
            else:
                cur, cur_count = node.val, 1
            if cur_count > ans_count:
                ans, ans_count = [cur], cur_count
            elif cur_count == ans_count:
                ans.append(cur)
            
            f(node.right)
        f(root)
        return ans
        

if __name__ == "__main__":
    s = Solution()
    print(s.findMode(buildTree([1, None, 2, 2])))
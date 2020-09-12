from utils.tree import TreeNode, buildTree
from typing import List

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        nodes = []
        if root:
            nodes.append((root, 0))
        while nodes:
            node, i = nodes.pop()
            if len(ans) == i:
                ans.append([0, 0])
            ans[i][0] += node.val
            ans[i][1] += 1
            if node.left:
                nodes.append((node.left, i+1))
            if node.right:
                nodes.append((node.right, i+1))
        return [s/n for s, n in ans]

if __name__ == "__main__":
    s = Solution()
    print(s.averageOfLevels(buildTree([3,9,20,15,7])))


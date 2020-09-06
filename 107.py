from typing import List
from utils.tree import buildTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def bfs(nodes: List):
            next_layer = []
            for i in range(len(nodes)):
                node = nodes[i]
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if next_layer:
                bfs(next_layer)
            ans.append([node.val for node in nodes])
        if root:
            bfs([root])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.levelOrderBottom(buildTree([3,9,20,None,None,15,7])))

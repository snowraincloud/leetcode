from utils.tree import TreeNode
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(nodes, s):
            if s == sum and not nodes[-1].left and not nodes[-1].right:
                ans.append([node.val for node in nodes])
            if nodes[-1].left and  abs(sum - s) >= abs(nodes[-1].left.val):
                nodes.append(nodes[-1].left)
                dfs(nodes, s + nodes[-1].val)
                nodes.pop()
            if nodes[-1].right and abs(sum - s) >= abs(nodes[-1].left.val):
                nodes.append(nodes[-1].right)
                dfs(nodes, s + nodes[-1].val)
                nodes.pop()
        if root:
            dfs([root], root.val)
        return ans
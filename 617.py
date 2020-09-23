from utils.tree import TreeNode

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if not (node1 and node2):
                return node1 if node1 else node2
            node1.val += node2.val
            node1.left = dfs(node1.left, node2.left)
            node1.right = dfs(node1.right, node2.right)
            return node1
        return dfs(t1, t2)
        
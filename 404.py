from utils.tree import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        def dfs(node):
            if node.left:
                
                if not node.left.left and not node.left.right:
                    nonlocal ans
                    ans += node.left.val
                else:
                    dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans
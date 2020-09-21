from utils.tree import TreeNode

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode: 
        def f(node, val):
            if not node:
                return val
            node.val += f(node.right, val)
            return f(node.left, node.val)
        f(root, 0)
        return root
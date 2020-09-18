from utils.tree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)
        helper(root)
        return root

    def invertTreeTwo(self, root: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
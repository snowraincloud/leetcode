from utils.tree import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def f(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)

            idx = idx_map[val]

            root.right = f(idx+1, right)
            root.left = f(left, idx-1)
            return root
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return f(0, len(inorder)-1)
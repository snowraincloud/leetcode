from utils.tree import TreeNode, buildTree
from typing import List

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans

    def inorderTraversalTwo(self, root: TreeNode) -> List[int]:
        ans = []
        nodes = []
        statuses = []
        nodes.append(root)
        statuses.append(True)
        while nodes:
            node = nodes.pop()
            status = statuses.pop()
            if not node:
                continue
            if status:
                nodes.append(node.right)
                statuses.append(True)
                nodes.append(node)
                statuses.append(False)
                nodes.append(node.left)
                statuses.append(True)
            else:
                ans.append(node.val)
        return ans

    def inorderTraversalThree(self, root: TreeNode) -> List[int]:
        ans = []
        nodes = []
        statuses = []
        while root or nodes:
            while root:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            ans.append(root.val)
            root = root.right
        return ans
            


if __name__ == "__main__":
    s = Solution()
    print(s.inorderTraversalThree(buildTree([1, None, 2, 3])))
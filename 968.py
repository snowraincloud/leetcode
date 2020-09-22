from utils.tree import TreeNode, buildTree

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        nodes = set()
        ans = 0
        def dfs(node, parent):
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            nonlocal ans, nodes
            if (node.left and node.left not in nodes) or (node.right and node.right not in nodes) or (node == parent and node not in nodes): 
                ans += 1
                nodes.add(node)
                if node.left:
                    nodes.add(node.left)
                if node.right:
                    nodes.add(node.right)
                nodes.add(parent)
        dfs(root, root)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.minCameraCover(buildTree([0,0,None,0,None,0,None,None,0])))



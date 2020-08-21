# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ans = 0
        def bfs(nodes):
            if not nodes:
                return
            nonlocal ans
            ans += 1
            temp = []
            for node in nodes:
                if not node.left and not node.right:
                    return
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            bfs(temp)
        if root:
            bfs([root])
        return ans

if __name__ == "__main__":
    solution = Solution()
    four = TreeNode(4)
    seven = TreeNode(7)

    fifteen = TreeNode(15)
    fifteen.left = four
    fifteen.right = seven
    twenty = TreeNode(20)
    twenty.left = fifteen
    nine = TreeNode(9)
    three = TreeNode(3)
    three.left = nine
    three.right = twenty
    print(solution.minDepth(three))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def f(root: TreeNode) -> tuple:
            l = r = 0
            if root.left:
                l, mark = f(root.left)
                l += 1
                if not mark:
                    return (-1, False)
            if root.right:
                r, mark = f(root.right)
                r += 1
                if not mark:
                    return (-1, False)
            return (max(l, r), abs(l - r) <= 1)
        return f(root)[1]

if __name__ == "__main__":
    solution = Solution()
    four = TreeNode(4)
    seven = TreeNode(7)
    seven.right = four
    fifteen = TreeNode(15)
    twenty = TreeNode(20)
    twenty.left = fifteen
    twenty.right = seven
    nine = TreeNode(9)
    three = TreeNode(3)
    three.left = nine
    three.right = twenty
    print(solution.isBalanced(three))
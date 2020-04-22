# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 示例:

# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        import queue
        now = queue.Queue()
        next = queue.Queue()
        now.put(root)
        res = list()
        while not now.empty():
            temp = now.get()
            res.append(temp.val)
            if temp.right:
                next.put(temp.right)
            if temp.left:
                next.put(temp.left)
            while not now.empty():
                temp = now.get()
                if temp.right:
                    next.put(temp.right)
                if temp.left:
                    next.put(temp.left)
            now, next = next, now
        return res


if __name__ == "__main__":
    solution = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(5)
    tree.right.right = TreeNode(4)
    res = solution.rightSideView(tree)
    print(res)
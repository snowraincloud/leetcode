from utils.tree import TreeNode, buildTree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor

if __name__ == "__main__":
    s = Solution()
    print(s.lowestCommonAncestor(buildTree([6,2,8,0,4,7,9,None,None,3,5]), TreeNode(2), TreeNode(8)))

            
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        if not vals:
            return None
        def f(l, r) -> TreeNode:
            m = (l + r) // 2
            node = TreeNode(vals[m])
            if m - l > 1:
                node.left = f(l, m-1)
            elif m - l == 1:
                node.left = TreeNode(vals[l])
            if r - m > 1:
                node.right = f(m+1, r)
            elif r - m == 1:
                node.right = TreeNode(vals[r])
            return node
        return f(0, len(vals)-1)

# 0 1 2 3 4 5 


if __name__ == "__main__":
    solution = Solution()
    nine = ListNode(9)
    five = ListNode(5, nine)
    zero = ListNode(0, five)
    negative_three = ListNode(-3, zero)
    negative_ten = ListNode(-10, negative_three) 
    print(solution.sortedListToBST(negative_ten))
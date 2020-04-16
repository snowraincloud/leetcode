# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse(self, l:ListNode) -> ListNode:
        pre, cur = None, l
        while cur:
            temp, cur.next = cur.next, pre
            pre, cur = cur, temp
        return pre


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2 
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        val = 0
        res = None
        next = None
        while l1 or l2:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            res = ListNode(val%10)
            res.next, next = next, res
            val //= 10
        if val:
            res = ListNode(val)
            res.next, next = next, res
        return res


    def addTwoNumbersAnother(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2
        
        def buildStack(l:ListNode) -> list:
            res = []
            while l:
                res.append(l.val)
                l = l.next
            return res
        l1_stack = buildStack(l1)
        l2_stack = buildStack(l2)
        val = 0
        res = None
        next = None
        while l1_stack or l2_stack or val:
            if l1_stack:
                val += l1_stack.pop()
            if l2_stack:
                val += l2_stack.pop()
            res = ListNode(val%10)
            res.next, next = next, res
            val //= 10
        return res

# if __name__ == "__main__":
#     solution = Solution()
#     l1 = ListNode(7)
#     l1.next = ListNode(2)
#     l1.next.next = ListNode(4)
#     l1.next.next.next = ListNode(3)
#     l2 = ListNode(5)
#     l2.next = ListNode(6)
#     l2.next.next = ListNode(4)
#     res = solution.addTwoNumbers(l1, l2)
#     print(res)

if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    res = solution.addTwoNumbersAnother(l1, l2)
    print(res)
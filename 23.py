from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [node for node in lists if node != None and isinstance(node, ListNode)]
        res_head = ListNode(0)
        res_end = res_head
        max_node = ListNode(0x7fffffff)
        while len(lists):
            min_node = max_node
            min_index = 0
            for i in range(len(lists)):
                if lists[i].val < min_node.val:
                    min_node = lists[i]
                    min_index = i
            res_end.next = min_node
            res_end = res_end.next
            if min_node.next == None:
                lists.pop(min_index)
            else:
                lists[min_index] = min_node.next
        return res_head.next


if __name__ == "__main__":
    solution = Solution()
    print(isinstance([], ListNode))
    # lists = []
    # lists.append(ListNode(1))
    # lists[0].next = ListNode(4)
    # lists[0].next.next = ListNode(5)
    # lists.append(ListNode(1))
    # lists[1].next = ListNode(3)
    # lists[1].next.next = ListNode(4)
    # lists.append(ListNode(2))
    # lists[2].next = ListNode(6)
    res = solution.mergeKLists([[]])
    print(res)
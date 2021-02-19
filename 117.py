"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        dummy_left_node = Node()
        pre = dummy_left_node
        current_node = root
        while current_node:
            if current_node.left:
                pre.next = current_node.left
                pre = pre.next
            if current_node.right:
                pre.next = current_node.right
                pre = pre.next
            current_node = current_node.next
            if not current_node:
                current_node = dummy_left_node.next
                dummy_left_node.next = None
                pre = dummy_left_node
        return root
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(nodes:List[int]) -> TreeNode:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    tree_nodes = deque()
    tree_nodes.append(root)
    i, l = 1, len(nodes)
    while tree_nodes and i < l:
        tree_node = tree_nodes.popleft()
        if nodes[i] != None:
            tree_node.left = TreeNode(nodes[i])
            tree_nodes.append(tree_node.left)
        i += 1
        if i < l:
            if nodes[i] != None:
                tree_node.right = TreeNode(nodes[i])
                tree_nodes.append(tree_node.right)
            i += 1
        
    return root

if __name__ == "__main__":
    root = buildTree([0,0,None,0,0])

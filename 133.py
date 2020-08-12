
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_map = dict()
        def dfs(node: 'Node'):
            if not node: 
                return None
            if node.val not in node_map:
                node_map[node.val] = res = Node(node.val, None)
                # neighbors = []
                # for neighbor in node.neighbors:
                #     neighbors.append(f(neighbor))
                # res.neighbors = neighbors
                res.neighbors = [*map(dfs, node.neighbors)]
            return node_map[node.val]
        return dfs(node)


if __name__ == "__main__":
    solution = Solution()
    
    node1 = Node(1)
    node3 = Node(3)
    node2 = Node(2, [node3, node1])
    test = Node(0, [node1, node2])
    solution.cloneGraph(test)
from typing import List


class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))
    
    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)
    
    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]


class Solution:

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        uf = UnionFind(nodesCount + 1)
        parent = list(range(nodesCount + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]

    def findRedundantDirectedConnectionTwo(self, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        roots = [-1] * (l+1)
        parents = [i for i in range(l+1)]
        conflict = -1
        cycle = -1
        mark = True
        for i, (start, end) in enumerate(edges):
            if parents[end] != end:
                conflict = i
            else:
                parents[end] = start
                while roots[start] != -1:
                    if roots[start] == end:
                        cycle = i
                        mark = False
                    start = roots[start]
                if mark:
                    roots[end] = start
                else:
                    mark = True
        if conflict < 0:
            return edges[cycle]
        else:
            if cycle > 0:
                return [parents[edges[conflict][1]], edges[conflict][1]]
            else:
                return edges[conflict]


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))

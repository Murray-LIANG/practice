"""
https://leetcode.com/problems/graph-valid-tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all
edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear
together in edges.
"""


class Solution(object):
    def validTree_BFS(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        There are three solutions: BFS, DFS and union find.
        """

        # BFS
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,

        queue = [0]
        for v in queue:
            queue.extend(neighbors.pop(v, []))

        return not neighbors

    def validTree_DFS(self, n, edges):
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)

        def visit(v):
            map(visit, neighbors.pop(v, []))

        visit(0)
        return not neighbors

    def validTree_UnionFind(self, n, edges):
        if len(edges) != n-1:
            return False

        s = range(n)

        def find(v):
            return v if s[v] == v else find(s[v])

        def union(edge):
            v, w = map(find, edge)
            s[v] = w
            return v != w

        return all(map(union, edges))


print(Solution().validTree_UnionFind(5, [[0, 1], [1, 2], [2, 3], [1, 3]]))

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
class UF:
    def __init__(self, N):
        self.ranks = [0]*N
        self.parents = list(range(N))
    
    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x == p_y:
            return False # already unioned
        if self.ranks[p_x] < self.ranks[p_y]:
            self.parents[p_x] = p_y
        elif self.ranks[p_x] > self.ranks[p_y]:
            self.parents[p_y] = p_x
        else:
            self.parents[p_x] = p_y
            self.ranks[p_y] += 1
        return True
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges))
        for e in edges:
            if not uf.union(e[0]-1, e[1]-1):
                return e

            
                    
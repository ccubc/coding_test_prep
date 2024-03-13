"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


"""

# O(N2) time limit exceeded solution (graph BFS)
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = self.edges_to_d(edges)
        min_height = float('inf')
        ans = []
        for i in range(n):
            cur_level = [i]
            visited = {i:1}
            height = 1
            while len(cur_level) > 0 and height < min_height:
                for _ in range(len(cur_level)):
                    cur_v = cur_level.pop(0)
                    for j in d[cur_v]:
                        if j not in visited:
                            visited[j] = 1
                            cur_level.append(j)
                height += 1
            if height < min_height:
                min_height = height
                ans = [i]
            elif len(cur_level) == 0 and height == min_height:
                ans.append(i)
        return ans
                    
    
    def edges_to_d(self, edges):
        d = defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        return d


# O(N) search from all the leaves (nodes with only 1 edge!!!), find their connected node, remove the connecting edge,
# repeat until finding the inner most layer
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        edge = [set() for _ in range(n)]
        for e in edges:
            edge[e[0]].add(e[1])
            edge[e[1]].add(e[0])
        cur_level = [i for i in range(n) if len(edge[i]) == 1] # all leaves
        upper_level = [] # one level upper the cur_level in the tree
        while True:
            for i in cur_level: # for each current leave
                for j in edge[i]: # for each node connected to leaf i
                    edge[j].remove(i) # delete edge (i, j)
                    if len(edge[j]) == 1: # if j becomes leaf after removing i from tree
                        upper_level.append(j)
            if len(upper_level) == 0: # cur_level is already the inner level
                return cur_level
            cur_level, upper_level = upper_level, []
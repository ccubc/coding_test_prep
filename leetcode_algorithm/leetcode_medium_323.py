"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_lists = [[] for _ in range(n)]
        for e in edges:
            adj_lists[e[0]].append(e[1])
            adj_lists[e[1]].append(e[0])
        seen = set()
        def dfs(r):
            if r in seen:
                return
            seen.add(r)
            for n in adj_lists[r]:
                adj_lists[n].remove(r)
                dfs(n)
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans
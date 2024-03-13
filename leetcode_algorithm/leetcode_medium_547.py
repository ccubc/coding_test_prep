"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # BFS graph
        visited = set()
        ans = 0
        for i in range(len(isConnected)):
            # BFS from i
            if i not in visited:
                queue = [i]
                while queue:
                    cur = queue.pop(0)
                    if cur not in visited:
                        visited.add(cur)
                        for j in range(i + 1, len(isConnected)):
                            if isConnected[cur][j] == 1:
                                queue.append(j)
                ans += 1
        return ans
      

# DFS graph
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        
        def dfs(i):
            for j, connected in enumerate(isConnected[i]):
                if connected and j not in seen:
                    seen.add(j)
                    dfs(j)
        
        ans = 0
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans     


# Union Find
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
        self.ranks = [0]*N
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        elif self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        else:
            self.parents[py] = px
            self.ranks[px] += 1

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j]:
                    uf.union(i, j)
        for i in range(len(isConnected)):
            uf.find(i)
        return len(collections.Counter(uf.parents))   
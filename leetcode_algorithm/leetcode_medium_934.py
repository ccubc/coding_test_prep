"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # first find one island
        # then BFS from this island to the nearest 1
        cur_level = self.findOneIsland(grid)
        # print(cur_level)
        # return
        cost = 0
        visited = {}
        for i in cur_level:
            visited[i] = 1
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        while True:
            for i in range(len(cur_level)):
                cur_v = cur_level.pop(0)
                for d in directions:
                    i1 = cur_v[0] + d[0]
                    i2 = cur_v[1] + d[1]
                    if (-1 < i1 < len(grid)) and (-1 < i2 < len(grid)) and (i1,i2) not in visited:
                        if grid[i1][i2] == 1:
                            return cost
                        else:
                            visited[(i1, i2)] = 1
                            cur_level.append((i1, i2))
            cost += 1
            
        
    def findOneIsland(self, grid):
        # find first 1
        entry = self.findEntry(grid)
        visited = {entry: 1}
        cur_level = [entry]
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        while len(cur_level) > 0:
            for i in range(len(cur_level)):
                cur_v = cur_level.pop(0)
                for d in directions:
                    i1 = cur_v[0] + d[0]
                    i2 = cur_v[1] + d[1]
                    if (-1 < i1 < len(grid)) and (-1 < i2 < len(grid)) and grid[i1][i2] == 1 and (i1,i2) not in visited:
                        visited[(i1, i2)] = 1
                        cur_level.append((i1, i2))
        return list(visited.keys())
            
    
    def findEntry(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i,j)
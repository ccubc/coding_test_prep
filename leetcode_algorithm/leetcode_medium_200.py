"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # wrap one more row of 0 above and one more col of 0 to the left
        if len(grid) == 0:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j] = ' ' # mark the cells that have been visited
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        

# 20220310
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ct = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i, j):
            grid[i][j] = 0
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if 0<=x<m and 0<=y<n and grid[x][y] == '1':
                    dfs(x,y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ct += 1
                    dfs(i, j) # mark i, j and all cells belonged to the same island as 0
        return ct


# 20220313
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(i, j):
            grid[i][j] = 0
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if 0<=x<m and 0<=y<n and grid[x][y] == "1":
                    grid[x][y] = 0
                    dfs(x,y)
            return
        ct = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ct += 1
                    dfs(i,j)
        return ct

#20220816
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ctr = 0
        def dfs(i, j):
            if grid[i][j] != '1':
                return
            grid[i][j] = 'x'
            if 0 <= i < len(grid) - 1:
                dfs(i+1, j)
            if 0 < i < len(grid):
                dfs(i-1, j)
            if 0 <= j < len(grid[0]) - 1:
                dfs(i, j+1)
            if 0 < j < len(grid[0]):
                dfs(i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ctr += 1
                    dfs(i, j)
        return ctr
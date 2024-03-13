"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #BFS
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: # if top left is non-zero or bottom right is non-zero
            return -1
        grid[0][0] = 1
        queue = [(0,0)] # a queue to look around
        for i, j in queue:
            if i == n-1 and j == n-1: # reached the exit cell
                return grid[n-1][n-1]
            for p, q in ((i-1,j), (i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)):
                if 0 <= p < n and 0 <= q < n and not grid[p][q]: # if valid index and cell not visited
                    grid[p][q] = grid[i][j]+1
                    queue.append((p,q))
        return -1

# 20220308
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        # BFS out from 0s
        dir8 = [[-1, -1], [-1, 0], [-1, 1],
               [0, -1], [0, 1],
               [1, -1], [1, 0], [1, 1]] # 8 directions
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = 1
        cur_level = [(0,0)]
        l_path = 1
        while len(cur_level) > 0:
            l_path += 1
            len_cur_level = len(cur_level)
            for _ in range(len_cur_level):
                cur_cell = cur_level.pop(0)
                for d in dir8:
                    i1, i2 = cur_cell[0] + d[0], cur_cell[1] + d[1]
                    if -1 < i1 < n and -1 < i2 < n:
                        if visited[i1][i2] == False and grid[i1][i2] == 0:
                            visited[i1][i2] = l_path
                            if i1 == n-1 and i2 == n-1:
                                return visited[i1][i2]
                            cur_level.append((i1, i2))
        if not visited[-1][-1]:
            return -1
        return visited[-1][-1]
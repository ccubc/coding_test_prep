"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = -1
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        if len(queue) == 0:
            time = 0
        # initialize queue with rotted oranges
        dir4 = [[-1,0],[1,0],[0,-1],[0,1]]
        while len(queue) > 0:
            for _ in range(len(queue)):
                cur_rot = queue.pop(0)
                for d in dir4:
                    i1, i2 = cur_rot[0]+d[0], cur_rot[1]+d[1]
                    if 0<=i1<len(grid) and 0<=i2<len(grid[0]) and grid[i1][i2]==1:
                        queue.append((i1,i2))
                        grid[i1][i2] = 2
            time += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # scan for rotten oranges
        m, n = len(grid), len(grid[0])
        queue = []
        ct = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    ct += 1
        if ct == 0:
            return 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = -1
        while queue:
            cur_q_len = len(queue)
            for _ in range(cur_q_len):
                cur = queue.pop(0)
                for d in dirs:
                    i, j = cur[0] + d[0], cur[1] + d[1]
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        ct -= 1
                        grid[i][j] = 2
                        queue.append([i, j])
            ans += 1
        return ans if ct == 0 else -1
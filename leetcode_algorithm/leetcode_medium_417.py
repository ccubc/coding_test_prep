"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(queue):
            access = [[0]*n for _ in range(m)]
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for x, y in queue:
                access[x][y] = 1
            while queue:
                cur_q_len = len(queue)
                for _ in range(cur_q_len):
                    cur = queue.pop(0)
                    for d in dirs:
                        x, y = cur[0]+d[0], cur[1]+d[1]
                        if 0<=x<m and 0<=y<n and access[x][y] == 0 and heights[x][y]>=heights[cur[0]][cur[1]]:
                            access[x][y] = 1
                            queue.append((x,y))
            return access
        accessA = bfs([(i, n-1) for i in range(m)]+[(m-1,i) for i in range(n-1)])
        accessP = bfs([(i, 0) for i in range(m)] + [(0, i) for i in range(1, n)])
        res = []
        for x in range(m):
            for y in range(n):
                if accessA[x][y] == 1 and accessP[x][y] == 1:
                    res.append([x,y])
        return res
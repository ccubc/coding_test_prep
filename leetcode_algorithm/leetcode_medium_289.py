"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""


from collections import defaultdict
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # solve it in two passes
        # store the position where a change needs to be made in the 1st pass
        # make the changes in the 2nd pass
        to_change = defaultdict(list)
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                count = 0
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        count += board[i-1][j-1]
                    if j + 1 < cols:
                        count += board[i-1][j+1]
                    count += board[i-1][j]
                if j - 1 >= 0:
                    count += board[i][j-1]
                if j + 1 < cols:
                    count += board[i][j+1]
                if i + 1 < rows:
                    if j - 1 >= 0:
                        count += board[i+1][j-1]
                    if j + 1 < cols:
                        count += board[i+1][j+1]
                    count += board[i+1][j]
                if board[i][j] == 0 and count == 3:
                    to_change[i].append(j)
                if board[i][j] == 1 and (count < 2 or count > 3):
                    to_change[i].append(j)
        for i in range(rows):
            for j in to_change[i]:
                board[i][j] = 1 - board[i][j]
        
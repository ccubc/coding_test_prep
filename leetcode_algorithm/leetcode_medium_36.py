"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_dic = {}
            for cell in row:
                if not cell.isdigit(): 
                    continue
                if cell not in row_dic:
                    row_dic[cell] = 1
                else:
                    return False
        for col in range(9):
            col_dic = {}
            for row in range(9):
                cell = board[row][col]
                if not cell.isdigit():
                    continue
                if cell not in col_dic:
                    col_dic[cell] = 1
                else:
                    return False
        for i in range(3):
            for j in range(3):
                cell_dic = {}
                for m in range(3):
                    for n in range(3):
                        cell = board[i*3+m][j*3+n]
                        if cell.isdigit():
                            if cell not in cell_dic:
                                cell_dic[cell] = 1
                            else:
                                return False
        return True
                            
from collections import Counter
class Solution(object):
    def checkDuplicate(self, nums):
        ct = Counter([i for i in nums if i != "."])
        ct["."] = 0
        return max(ct.values()) <= 1

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check whether all rows are valid
        for r in board:
            if not self.checkDuplicate(r):
                return False
        # check whether all cols are valid
        for i in range(9):
            c = [row[i] for row in board]
            if not self.checkDuplicate(c):
                return False
        # check whether all squares are valid
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                sq = []
                for k in range(3):
                    sq.extend(board[i+k][j: j+3])
                if not self.checkDuplicate(sq):
                    return False
        return True
            
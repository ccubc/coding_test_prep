"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, word):
                    return True
        return False
    
    
    def dfs(self, i, j, board, word):
        # base case: checked all letters in word
        if len(word) <= 0:
            return True
        # out of boundary
        if i < 0 or i >= len(board) or j < 0 or j >=len(board[0]):
            return False
        if board[i][j] != word[0]:
            return False
        # board[i][j] = word[0]
        tmp = board[i][j] # save board[i][j] to be restored after dfs (backtreking)
        board[i][j] = "1"
        res = self.dfs(i+1, j, board, word[1:]) or \
                self.dfs(i-1, j, board, word[1:]) or \
                self.dfs(i, j+1, board, word[1:]) or \
                self.dfs(i, j-1, board, word[1:])
        board[i][j] = tmp # restore original letter
        return res
        
        
            
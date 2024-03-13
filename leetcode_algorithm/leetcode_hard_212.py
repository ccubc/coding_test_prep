"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add(w)
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, "", i, j)
        return self.res
    
    
    def dfs(self, board, node, path, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return  
        node = node.children[board[i][j]]
        path += board[i][j]
        tmp = board[i][j]
        board[i][j] = '#'
        if node.isEnd:
            self.res.append(path)
            node.isEnd = False
        self.dfs(board, node, path, i+1, j)
        self.dfs(board, node, path, i-1, j)
        self.dfs(board, node, path, i, j+1)
        self.dfs(board, node, path, i, j-1)
        board[i][j] = tmp
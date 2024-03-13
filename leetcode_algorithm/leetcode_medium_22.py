"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs to write string from left to right
        # left_remain tracks how many ( remains to be written into the string
        # right_remain tracks how many ) remains to be written into the string
        
        def dfs(res, string, left_remain, right_remain):
            if left_remain > right_remain or left_remain <0 or right_remain < 0:
                # left_remain < right_remain means current string looks like ")" or "())"
                # left_remain or right_remain < 0 means we ended the DFS traversal
                return
            if left_remain == right_remain == 0:
                res.append(string)
                return
            if left_remain > 0:
                dfs(res, string+"(", left_remain-1, right_remain)
            if right_remain > 0:
                dfs(res, string+")", left_remain, right_remain-1)
                
        res = []
        dfs(res, "", n, n)
        return res
        
"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19

"""



class Solution:
    def numTrees(self, n: int) -> int:
        # for a BST with n nodes of unique values
        # if root = i, left = a tree with i-1 nodes, right = a tree with n-i nodes
        # total number of nodes: 1(root) + (i-1) + (n-i) = n
        # subtree of a BST must be a BST
        # how many unique BST can there be for a tree with (i-1) nodes and (n-i) nodes? 
        dp = [0] * (n+1)
        dp[0] = 1 # 0 children 1 possibility
        dp[1] = 1 # 1 child 1 possibility
        
        for i in range(2, n + 1):
            # calculate all subproblems
            for j in range(1, i+1): # j is index+1 of root
                left = dp[j-1]
                right = dp[i-j]
                dp[i] += (left * right)
        return dp[-1]
"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 2d DP
        # pad 1st row and 1st col
        t = '_' + t
        s = '_' + s
        m, n = len(t), len(s)
        dp = [[1]*(n+1)] + [[0]*(n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if t[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j] # breakdown the problem to 2 situations
                    # A: numDistinct(s[i-1], t[j-1]) -- this set of solutions would include s[i]
                    # B: numDistinct(s[i-1], t[j]) -- this set of solutions would not include s[i]
                else:
                    dp[i+1][j+1] = dp[i+1][j] # i.e. must find all subsequences before s[i]
        #print(dp)
        return dp[-1][-1]                    
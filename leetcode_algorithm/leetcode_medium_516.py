"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [[1]*l for _ in range(l)] # dp[i][j]: longest palindromic subsequence length for subproblem s[i][j]
        # i <= j, only need to fill out upper right triangle of the DP matrix
        for i in range(l-1):
            dp[i][i+1] = (s[i] == s[i+1])*1 + 1
        for k in range(3, l+1):
            for i in range(l - k + 1):
                j = i + k - 1 # max j: l - k + k - 1 = l - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
        
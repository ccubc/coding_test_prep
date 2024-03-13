"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        # num_insertions = len(s) - len(longest palindrome subsequence)
        # so the problem is equivalent to: longest palindrome subsequence
        l_s = len(s)
        dp = [[1]*l_s for _ in range(l_s)]
        # dp[i][j]: len longest palindrome subsequence
        lps = 1 # global to record longest palindrome subsequence
        for i in range(l_s-1): # handle the case where substring len = 2
            j = i+1
            if s[i]==s[j]:
                dp[i][j] = 2
        for l in range(3, l_s+1):
            for i in range(l_s-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return l_s - dp[0][-1]
                
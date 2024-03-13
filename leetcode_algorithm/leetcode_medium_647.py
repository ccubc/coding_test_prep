"""Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        # each row_id of dp matrix corresponds to length of substring
        # each col_id of dp matrix corresponds to starting index of the substring
        # dp[i][j] would mean: substring of s from index j to j + i
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s) - i):
                if i < 2: # for substrings with len 1 or 2, only need to check self
                    dp[i][j] = s[j]==s[j+i]
                else: # no need for this else but I like it
                    dp[i][j] = (dp[i-2][j+1]) and (s[j]==s[j+i])
        ans = 0
        for i in range(len(dp)):
            ans += sum(dp[i])
        return ans

# 20220327
class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        
        def countFromCenter(l, r):
            ct = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ct += 1
                l -= 1
                r += 1
            return ct
            
        for i in range(len(s)):
            ct += countFromCenter(i, i)
            if i < len(s) - 1 and s[i] == s[i+1]:
                ct += countFromCenter(i, i+1)
        return ct
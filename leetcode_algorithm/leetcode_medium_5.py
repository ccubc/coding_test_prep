"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_res, longest_res, max_len = "", "", 0
        
        # detect Palindrome with even number of chars e.g. abba
        for i in range(len(s)):
            l,r = i, i+1
            cur_res = ""
            while l >= 0 and r < len(s) and s[l]==s[r]:
                cur_res = s[l] + cur_res + s[r]
                l -= 1
                r += 1
            if len(cur_res) > max_len:
                max_len = len(cur_res)
                longest_res = cur_res

        # detect Palindrome with odd number of chars e.g. abcba
        for i in range(len(s)):
            l, r = i-1, i+1
            cur_res = s[i]
            while l >= 0 and r < len(s) and s[l]==s[r]: # skip the center char
                cur_res = s[l] + cur_res + s[r]
                l -= 1
                r += 1
            if len(cur_res) > max_len:
                max_len = len(cur_res)
                longest_res = cur_res
                
        return longest_res


# 20220217
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False] * l for _ in range(l)] # dp[i][j]: whether s[i:j+1] is palindrom
        # because j >= i, we only need to fill out the upper right triangle of this DP matrix
        
        ans = s[0]
        max_l = 1
        for i in range(l):
            dp[i][i] = True # single char always palindrom
        
        for i in range(l-1):
            if s[i] == s[i+1]: # case where substring consists of only 2 char
                dp[i][i+1] = True
                ans = s[i:i+2]
                max_l = 2
                
        for k in range(3, l + 1):
            for i in range(l - k + 1): # left index of substring
                j = i + k - 1 # j max is l - k + k - 1, i.e. l - 1
                if dp[i+1][j-1] and (s[i]==s[j]):
                    dp[i][j] = True
                    max_l = k
                    ans = s[i: j+1]
        
        return ans


# 20220327 expand around centre
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # middle out, note that the cases of odd/even length palindrom differ
        ans, cur_max = "", 0
        def check(l, r, ans, cur_max):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > cur_max:
                cur_max = r - l - 1
                ans = s[l+1: r]
            return ans, cur_max
                                     
        for i in range(len(s)):
            ans, cur_max = check(i, i, ans, cur_max)
            if i < len(s)-1 and s[i] == s[i+1]:
                ans, cur_max = check(i, i+1, ans, cur_max)
        return ans
        
        

"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
Accepted
723K
Submissions
2.4M
Seen this question in a real interview before?
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # 0 needs to be treated special
        # 0 will break down a normal dp pattern, and break the problem to s[first] and s[second], ...
        # final result would be s[first] * s[second] * ... if contains 0
        def no_zero_decodings(s):
            if s == "":
                return 1
            dp = [0] * (len(s)+1)
            dp[0] = dp[1] = 1
            for i in range(1, len(s)):
                dp[i+1] += dp[i]
                if ((int(s[i]) < 7) and s[i-1]=='2') or (s[i-1]=='1'):
                    dp[i+1] += dp[i-1]
            return dp[-1]
        
        no_zero_substrings = []
        pre = 0
        for i, c in enumerate(s):
            if c == '0':
                if i == 0 or s[i-1] not in ['1', '2']: # check for invalid input string
                    return 0
                no_zero_substrings.append(s[pre: i-1])
                pre = i+1
        if pre < len(s):
            no_zero_substrings.append(s[pre:len(s)])
        res = 1
        for s in no_zero_substrings:
            res *= no_zero_decodings(s)
        return res

# more elegant solution:
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i-1]) <= 9: # one-step jump
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <=26: # two-step jump
                dp[i] += dp[i-2]

        return dp[-1]
 

 class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [1] + [0] * len(s)
        for i in range(len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
            else:
                dp[i+1] += dp[i]
                if i>0 and 10 < int(s[i-1:i+1]) < 27:
                    dp[i+1] += dp[i-1]
        return dp[-1]
        
"""
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 

Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
 

Constraints:

1 <= pattern.length, s.length <= 20
pattern and s consist of only lowercase English letters.
"""

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pattern, s, mapping):
            # base case, when we exhausted all chars in pattern, check whether length of str is 0
            if len(pattern) == 0:
                return len(s) == 0
            if pattern[0] in mapping:
                # we saw this char at the head of pattern before, now need to check whether it is valid
                if s[:len(mapping[pattern[0]])] != mapping[pattern[0]]:
                    return False
                return backtrack(pattern[1:], s[len(mapping[pattern[0]]):], mapping)
            # pattern[0] not in mapping, we are free to assign pattern[0] to s[:x]
            for i in range(len(s)):
                if s[:i+1] in mapping.values(): # two keys can not map to a single value as defined by the problem
                    continue
                mapping[pattern[0]] = s[:i+1]
                if backtrack(pattern[1:], s[i+1:], mapping):
                    return True
                del mapping[pattern[0]]
            return False
        return backtrack(pattern, s, {})
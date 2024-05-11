"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        for i in range(len(s2) - len(s1)+1):
            c2 = Counter(s2[i:i+len(s1)])
            if c1 == c2:
                return True
        return False

# 不那么暴力的解法
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        matches = []
        c2 = Counter(s2[:len(s1)])
        for c in "qwertyuiopasdfghjklzxcvbnm":
            if c1.get(c, 0) == c2.get(c, 0):
                matches.append(1)
            else:
                matches.append(0)
        cur_matched_ct = sum(matches)
        if cur_matched_ct == 26:
            return True
        for i in range(len(s2) - len(s1)):
            if cur_matched_ct == 26:
                return True
            c2[s2[i]] -= 1
            if c1.get(s2[i], 0) == c2.get(s2[i], 0):
                cur_matched_ct += 1
            elif c1.get(s2[i], 0) == c2.get(s2[i], 0) + 1:
                cur_matched_ct -= 1
            c2[s2[i+len(s1)]] += 1
            if c1.get(s2[i+len(s1)], 0) == c2.get(s2[i+len(s1)], 0):
                cur_matched_ct += 1
            elif c1.get(s2[i+len(s1)], 0) == c2.get(s2[i+len(s1)], 0) - 1:
                cur_matched_ct -= 1
        return cur_matched_ct == 26

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


# 20220320
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctr1 = collections.Counter(s)
        ctr2 = collections.Counter(t)
        for k in ctr1:
            if k not in ctr2 or ctr2[k]!=ctr1[k]:
                return False
            del ctr2[k]
        if len(ctr2) > 0:
            return False
        return True


# 20231007
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

# 20231007
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ct = defaultdict(int)
        for c in s:
            ct[c] += 1
        for c in t:
            ct[c] -= 1
        for k, v in ct.items():
            if v != 0:
                return False
        return True

# 20240430
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

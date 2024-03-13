"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        dic = {}
        dic_v = {}
        i = 0
        while i < l:
            if s[i] not in dic:
                if t[i] in dic_v:
                    return False
                else:
                    dic_v[t[i]]=1
                dic[s[i]] = t[i]
            else:
                if t[i] != dic[s[i]]:
                    return False
            i+=1
        return True

        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        for i in range(len(s)):
            if s[i] not in d_s:
                if t[i] not in d_t:
                    d_s[s[i]] = t[i]
                    d_t[t[i]] = 1
                else:
                    return False # s[i] not seen but t[i] mapped to other char in s
            else:
                if d_s[s[i]] != t[i]:
                    return False
        return True
        
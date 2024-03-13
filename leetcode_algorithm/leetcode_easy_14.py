"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        ans = ""
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for word in strs[1:]:
                if len(word) <= i or word[i] != c:
                    return ans
            ans = ans + c
            i += 1
        return ans


# 20220906
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        pt = 0
        while True:
            if pt >= len(strs[0]):
                return res
            c = strs[0][pt]
            res += c
            for s in strs[1:]:
                if pt >= len(s) or s[pt] != c:
                    return res[:-1]
            pt += 1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return res
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                res += c
            else:
                break
        return res

# 20230117
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, ans = 0, ""
        while i < len(strs[0]):
            cur = strs[0][i]
            for s in strs[1:]:
                if len(s) <= i or s[i] != cur:
                    return ans
            ans += cur
            i += 1
        return ans

# 20230930 感觉代码有变酷炫一点了
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans, p = "", 0
        while True:
            if any (len(s) <= p for s in strs) or not all (s[p] == strs[0][p] for s in strs[1:]):
                return ans
            else:
                ans += strs[0][p]
                p += 1
"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pre_list, post_list = [], []
        res = 0
        for c in s:
            for l in pre_list:
                if c not in l:
                    l.append(c)
                    post_list.append(l)
            post_list.append([c])
            res = max([res]+[len(x) for x in post_list])
            pre_list, post_list = post_list, []
        return res

# 20220320
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = start = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1 # restart a new list
            else:
                # cur str is still valid
                ans = max(ans, i+1-start)
            seen[c] = i # where c is last seen
        return ans

# 20221002
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, pt1, pt2 = 0, 0, 0
        d = {}
        while pt2 < len(s):
            if s[pt2] in d:
                while s[pt1] != s[pt2]:
                    del d[s[pt1]]
                    pt1 += 1
                pt1 += 1
            else:
                d[s[pt2]] = 1
                ans = max(ans, pt2 - pt1 + 1)
            pt2 += 1
        return ans


# 20230116
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans, seen = 0, 0, 0, set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                ans = max(ans, r - l + 1)
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return ans


# 20230408
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                ans = max(ans, r - l)
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
        return ans

# 20230930
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length, set_char = 0, set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in set_char:
                set_char.add(s[r])
                max_length = max(max_length, r - l + 1)
            else:
                while s[l] != s[r]:
                    set_char.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return max_length

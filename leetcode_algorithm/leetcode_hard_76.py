"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        i, j = 0, 0
        seen = collections.defaultdict(int)
        target = collections.defaultdict(int)
        for c in t:
            target[c] += 1
        ans, cur_len, n_found = "", float('inf'), 0
        while j < len(s):
            while n_found < len(t) and j < len(s):
                # move pt j to the right while cur substring is not legit
                if s[j] in target:
                    if seen[s[j]] < target[s[j]]:
                        n_found += 1
                    seen[s[j]] += 1
                j += 1
            if n_found < len(t):
                break
            # print('j')
            # print(j)
            # print(seen)
            while i < j:
                # move pt i to the right while cur substring is still legit
                if s[i] in target:
                    seen[s[i]] -= 1
                    if seen[s[i]] < target[s[i]]:
                        if j-i < cur_len:
                            cur_len = j-i
                            ans = s[i:j]
                        n_found -= 1
                        i += 1
                        break
                i += 1
            # print('i')
            # print(i)
            # print(seen)
        return ans
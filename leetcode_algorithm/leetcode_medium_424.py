"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ctr = collections.Counter()
        l = r = most_freq = 0
        for r in range(len(s)):
            ctr[s[r]] += 1
            most_freq = max(most_freq, ctr[s[r]])
            if most_freq + k < r + 1 - l:
                ctr[s[l]] -= 1
                l += 1
        return len(s) - l


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

# 20240505
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # sliding window, maintain a legit substr, 

        l = 0
        seen = {}
        ans = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            # if the most frequent char (the char you won't need to replace with other chars) + k (replacement action) < len of cur window
            if max(seen.values()) + k < r - l + 1: 
                # slide the left pt to the right by 1, and update the counter of the latest window 
                seen[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

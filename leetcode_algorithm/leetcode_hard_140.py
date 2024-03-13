"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        dic = {}
        for w in wordDict:
            dic[w] = 1
        
        def dfs(s, current, dic):
            if s in dic:
                current2 = current.copy()
                current2.append(s)
                ans.append(" ".join(current2))
            # can not have "else" here! for edge case ("aaaaaaa", ["a", "aa", "aaa"])

            for i in range(len(s)-1):
                current2 = current.copy()
                if s[: i+1] in dic:
                    current2.append(s[: i+1])
                    dfs(s[i+1:], current2, dic)
        dfs(s, [], dic)
        return ans
                        

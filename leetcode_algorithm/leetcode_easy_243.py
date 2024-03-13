"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lookfor, ans, pre = None, float('inf'), None
        for i, w in enumerate(wordsDict):
            if w == word1:
                if lookfor == 1:
                    ans = min(ans, i - pre)
                lookfor = 2
                pre = i
            elif w == word2:
                if lookfor == 2:
                    ans = min(ans, i - pre)
                lookfor = 1
                pre = i
        return ans
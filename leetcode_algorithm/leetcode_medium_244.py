"""
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.d[w].append(i)

            
    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.d[word1]
        l2 = self.d[word2]
        r = float('inf')
        p1, p2 = 0,0
        while p1 < len(l1) and p2 < len(l2):
            r = min(r, abs(l1[p1] - l2[p2]))
            if l1[p1] < l2[p2]:
                p1 += 1
            else:
                p2 += 1
        return r

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
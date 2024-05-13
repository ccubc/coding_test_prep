"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

"""

from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) 
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0

# graph BFS time-out answer
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph BFS
        graph = self.constructGraph(wordList)
        current_level = []
        for w in wordList:
            if self.adjacent(beginWord, w):
                current_level.append(w)
        if len(current_level) == 0 or endWord not in graph.keys():
            return 0
        
        cost = 1
        while len(current_level) > 0:
            cost += 1
            cur_level_len = len(current_level)
            for i in range(cur_level_len):
                cur_w = current_level.pop(0)
                if cur_w == endWord:
                    return cost
                if cur_w in graph: # not visited yet
                    current_level += graph[cur_w]
                    del graph[cur_w]
        return 0
        
        
    def constructGraph(self, wordList):
        graph = {}
        for w in wordList:
            graph[w] = []
        for i in range(len(wordList)-1):
            for j in range(i+1, len(wordList)):
                if self.adjacent(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        return graph
    
    
    def adjacent(self, w1, w2):
        ctr = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                ctr += 1
            if ctr > 1:
                return False
        if ctr == 1:
            return True
        return False


# 20231001 Graph BFS
# (I did wrote out the code on my own but it was really slow)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = []
        level = 0
        visited = [False for _ in range(len(wordList))]

        for i, w in enumerate(wordList):
            if endWord == w:
                visited[i] = True
                queue.append(endWord)
        
        while queue:
            cur_q_len = len(queue)
            level += 1
            for _ in range(cur_q_len):
                cur_node = queue.pop(0)
                if self.verify_link(cur_node, beginWord):
                    return level + 1
                else:
                    for i, w in enumerate(wordList):
                        if not visited[i] and self.verify_link(cur_node, w):
                            queue.append(w)
                            visited[i] = True
        return 0
                            
        
    def verify_link(self, w1, w2):
        # verify whether w1 can be turned to w2 by only changing one single char; w1 and w2 have the same length
        diff = 0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1


# 20240513
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        queue = [beginWord]
        visited = set()
        visited.add(beginWord)
        level = 1
        graph = self.buildGraph(wordList)
        # print(graph)
        # print(level)
        # print(queue)
        while queue:
            cur_level_len = len(queue)
            for _ in range(cur_level_len):
                cur_node = queue.pop(0)
                if cur_node == endWord:
                    return level
                for n in graph[cur_node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)

            level += 1
            # print(level)
            # print(queue)
        return 0

    def buildGraph(self, wordList):
        graph = collections.defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.isOneCharDiff(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        return graph
            

    def isOneCharDiff(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
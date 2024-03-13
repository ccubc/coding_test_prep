"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        ctr = 0
        for word in strs:
            sorted_wd = ''.join(sorted(list(word)))
            if sorted_wd not in dic:
                dic[sorted_wd] = ctr
                ctr += 1
                ans.append([word])
            else:
                ans[dic[sorted_wd]].append(word)
        return ans
            
# 20220320
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(s):
            ctr = collections.Counter(s)
            code = '-'.join([str(ctr.get(c, 0)) for c in 'abcdefghijklmnopqrstuvwxyz'])
            return code
        
        d_encode = collections.defaultdict(list)
        for s in strs:
            k = encode(s)
            d_encode[k].append(s)
        ans = []
        for k in d_encode:
            ans.append(d_encode[k])
        return ans

# sort word居然比counter快。。。哦因为word len都不是特别长～ 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        idx = 0
        for word in strs:
            sorted_wd = ''.join(sorted(word))
            if sorted_wd not in dic:
                dic[sorted_wd] = idx
                idx += 1
                ans.append([word])
            else:
                ans[dic[sorted_wd]].append(word)
        return ans


# 20230117
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i, w in enumerate(strs):
            d[''.join(sorted(w))].append(i)
        ans = []
        for _, v in d.items():
            ans.append([strs[i] for i in v])
        return ans

# 20230930
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        d = {}
        for s in strs:
            if ''.join(sorted(s)) not in d:
                d[''.join(sorted(s))] = len(ans)
                ans.append([s])
            else:
                ans[d[''.join(sorted(s))]].append(s)
        return ans
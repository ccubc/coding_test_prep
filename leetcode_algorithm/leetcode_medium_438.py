
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


# O(n)
import collections
class Solution:
    def dict_greater(self, dict1,dict2):
        if [x for x in dict1.keys() if x not in dict2.keys()]:
            return True
        elif any([dict1[key]>dict2[key] for key in dict1.keys()]):
            return True
        else:
            return False
    def dict_plus(self, dict_temp,x):
        if x in dict_temp:
            dict_temp[x]+=1
        else:
            dict_temp[x]=1
        return dict_temp

    def dict_minus(self, dict_temp,x):
        if x not in dict_temp:
            return dict_temp
        if dict_temp[x]>1:
            dict_temp[x]=dict_temp[x]-1
        else:
            del dict_temp[x]
        return dict_temp

    def findAnagrams(self, s: str, p: str) -> List[int]:
        i=0
        dict_p=collections.Counter(p)
        index=0
        dict_temp={}
        output=[]
        while i<len(s):
            dict_temp=self.dict_plus(dict_temp,s[i])
            while self.dict_greater(dict_temp,dict_p):
                dict_temp=self.dict_minus(dict_temp,s[index])
                index=index+1
            if dict_temp==dict_p:
                output.append(i)
            i+=1
        return [x-len(p)+1 for x in output]
        

# O(n*k) --- time limit exceeded
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_p = collections.Counter(p)
        dic_s = {}
        ans = []
        for i, c in enumerate(s+"*"): # * is a place holder to indicate end of str
            if c in dic_p:
                dic_s[i] = dic_p.copy()
            dic_s_keys = list(dic_s.keys())
            for start_pos in dic_s_keys:
                if c not in dic_s[start_pos]:
                    if len(dic_s[start_pos]) == 0: # found a position
                        ans.append(start_pos)
                        del dic_s[start_pos]
                    else:
                        del dic_s[start_pos]
                else:
                    dic_s[start_pos][c] -= 1
                    if dic_s[start_pos][c] == 0:
                        del dic_s[start_pos][c]
        return ans
    


# 20220824 sliding window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount, pCount, sLen, pLen = {}, {}, len(s), len(p)
        if pLen > sLen: 
            return []
        for i in range(pLen):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        res = [0] if pCount == sCount else []
        l = 0
        for r in range(pLen, sLen):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if pCount == sCount:
                res.append(l)
        return res
               
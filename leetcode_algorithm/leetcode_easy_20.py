#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:29:09 2019

@author: chengchen

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c not in dic.keys():
                stack.append(c)
            else:
                if (len(stack) > 0) and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
        return (len(stack) == 0)


s = "{{[]}}"
def isValid(s):
    list_s = list(s)
    dic = {'{':'}',
       '[':']',
       '(':')'}
    stack = []
    flag = True
    for i in range(len(list_s)):
        if list_s[i] in dic.keys():
            stack.append(dic[list_s[i]])
        else:
            if len(stack)==0:
                return False
            else:
                if (list_s[i] != stack.pop()):
                    return False
    if len(stack)>0:
        return False
    return flag
print(isValid(s))




class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',
              ']': '[',
              '}': '{'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                try:
                    if stack.pop() == dic[c]:
                        continue
                    else:
                        return False
                except:
                    return False
        return len(stack)==0


# 20220327
class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
            }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif len(stack) < 1 or d[c] != stack[-1]:
                return False
            else: # c in ')]}' and d[c] == stack[-1]
                stack.pop()
        if len(stack) > 0:
            return False
        return True
                
        

    
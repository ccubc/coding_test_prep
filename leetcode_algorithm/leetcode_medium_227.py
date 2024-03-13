#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:29:03 2020

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1

@author: chengchen
"""
class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, num = [], '+', 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in ('+-*/') or i == (len(s)-1):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(num*stack.pop())
                else:
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
        return sum(stack)

# 20220207               
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                while i + 1 < len(s) and s[i+1].isdigit():
                    c += s[i+1]
                    i += 1
                stack.append(int(c))
            elif c in "+-":
                stack.append(c)
            elif c == "*":
                prev_num = stack.pop()
                i += 1
                while s[i] == " ":
                    i += 1
                post_c = s[i]
                while i + 1 < len(s) and s[i+1].isdigit():
                    post_c += s[i+1]
                    i += 1
                post_num = int(post_c)
                stack.append(prev_num*post_num)
            elif c == "/":
                prev_num = stack.pop()
                i += 1
                while s[i] == " ":
                    i += 1
                post_c = s[i]
                while i + 1 < len(s) and s[i+1].isdigit():
                    post_c += s[i+1]
                    i += 1
                post_num = int(post_c)
                stack.append(prev_num//post_num)
            i += 1
        ans = stack[0]
        i = 1
        while i < len(stack):
            if stack[i] == "+":
                ans += stack[i+1]
            elif stack[i] == "-":
                ans -= stack[i+1]
            i += 1
        return ans
         
                
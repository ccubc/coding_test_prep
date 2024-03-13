#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:32:11 2020
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
@author: chengchen
"""
# recursion
def climbStairs(self, n: int) -> int:
    if n < 3: return n
    else: return self.climbStairs(n-1) + self.climbStairs(n-2)
        

# dynamic programing
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        elif n == 2: return 2
        pre2, pre1 = 1, 2
        for i in range(n - 2):
            cur = pre1 + pre2
            pre2, pre1 = pre1, cur
        return cur

# dynamic programming 20200314
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        res = [1,2]
        for i in range(2, n):
            res = [res[1], sum(res)]
        return res[1]

# 20210113
class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion takes too long to run, hence will use iteration
        if n < 4:
            return n
        s1 = 1
        s2 = 2
        for i in range(3, n+1):
            s = s1+s2
            s1 = s2
            s2 = s
        return s

# 20220205
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(1, n):
            dp[i+1] = dp[i] + dp[i-1]
        return dp[-1]

# 20220227
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, ans = 1,1
        for _ in range(1,n):
            prev, ans = ans, ans + prev
        return ans


# 20220820
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b
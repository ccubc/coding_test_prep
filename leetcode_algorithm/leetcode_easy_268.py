#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:16:49 2020
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
@author: chengchen
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = n*(n+1)//2
        return s - sum(nums)


# 20220227
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum_ = (1+l)*l//2
        return sum_ - sum(nums)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:52:43 2020
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
@author: chengchen
"""

# normal solution using dictionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic: return True
            dic[i] = i
        return False
        
    
# 骚操作
class Solution:
def containsDuplicate(self, nums: List[int]) -> bool:
    return not (len(nums) == len(set(nums)))

# 20240430
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ct = collections.defaultdict(int)
        for i in nums:
            ct[i] += 1
            if ct[i] > 1:
                return True
        return False
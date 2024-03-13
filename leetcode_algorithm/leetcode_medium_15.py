#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:55:24 2019

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

@author: chengchen
"""

# Use 2 pointer with sorted list to fasten the computation
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue            
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    solution.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
        return solution
                
        


# The below solution is O(N2), similar to the classic 2-sum solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        for i in range(len(nums)):
            dic = {}
            for j in range(i+1, len(nums)):
                if - nums[j] - nums[i] not in dic:
                    dic[nums[j]] = nums[j]
                else:
                    print(i,j)
                    s = [nums[i], dic[-nums[j]-nums[i]], nums[j]]
                    s.sort()
                    if s not in solution:
                        solution.append(s)
        return solution
                


# 20220224
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        k = len(nums) - 1
        while k > 1 and nums[k] >= 0:
            if k < len(nums) - 1 and nums[k] == nums[k+1]:
                k -= 1
                continue # this case has been visited
            # look for nums[i] + nums[j] = -nums[k] where i < j < k
            j = k-1
            i = 0
            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    ans.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i+1] == nums[i]:
                        i += 1
                    i += 1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    j -= 1
            k -= 1
        return ans
                
        
                
        
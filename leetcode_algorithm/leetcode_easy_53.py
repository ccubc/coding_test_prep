#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:42:23 2019

@author: chengchen

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
def solution(nums):
    if (len(nums)==0):
        return None
    else:
        max_carry = nums[0]
        pre_max = nums[0]
        for i in range(1,len(nums)):
            max_carry = max(max_carry+nums[i], nums[i])
            pre_max = max(pre_max, max_carry)
        return pre_max

print(solution([-2,1,-3,4,-1,2,1,-5,4])==6)
print(solution([-2,3,-1,4,-1,2,1,-5,4])==8)

# 20220205, DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0] # initialize maximum subarray sum
        dp = [0] * len(nums) # dp stores maximum subarray sum that ends with current index
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ans = max(ans, dp[i])
        return ans

# 20220221
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)
        # 1-d dp to store: max subarray sum where the subarray includes index i
        cur_ans = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], 0) + nums[i]
            cur_ans = max(cur_ans, dp[i])
        return cur_ans

# 20220614
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = ans = nums[0]
        for i in nums[1:]:
            cur = i if pre < 0 else i + pre
            ans = max(ans, cur)
            pre = cur
        return ans
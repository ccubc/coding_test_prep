"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


import numpy as np
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_abs_delta = np.inf
        for i in range(len(nums)-2):
            new_target = target - nums[i]
            left = i + 1
            right = len(nums)-1
            while left < right:
                delta = new_target - nums[left] - nums[right]
                if delta == 0:
                    return target
                if abs(delta) < abs(min_abs_delta):
                    min_abs_delta = delta                    
                if nums[left] + nums[right] < new_target:
                    left += 1
                else:
                    right -= 1
        return target - min_abs_delta


# 20221003
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return res
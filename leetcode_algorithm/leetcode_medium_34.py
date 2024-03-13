"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search
        # need to adjust array index when returning answer
        # challenge is when mid = target => need to search both left & right
        
        # or, this question is 99% same as find first target + find last target in a sorted array
        l = self.searchFirst(nums, target)
        if l != -1:
            r = self.searchLast(nums, target)
            return [l, r]
        else:
            return [-1, -1]
        
        
    def searchFirst(self, nums, target):
        # return index of 1st target in array, if not existing return -1
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return -1  
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l) //2 # if nums contain even number, mid = last in left half
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        else:
            return -1

    
    def searchLast(self, nums, target):
        # return index if last target in array (guarantee target exists in array)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l+1)//2 # if nums contain even number, mid = first in right half
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return l
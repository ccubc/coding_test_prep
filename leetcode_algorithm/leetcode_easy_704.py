"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


class Solution:
    def search_rec(self, nums, target):
        if len(nums) == 0:
            return -20000
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else: 
                return -20000
        else:
            mid_i = len(nums)//2
            if target == nums[mid_i]:
                return mid_i
            elif target < nums[mid_i]:
                return self.search_rec(nums[:mid_i], target)
            else:
                return mid_i+1 + self.search_rec(nums[mid_i+1:], target)

    
    def search(self, nums: List[int], target: int) -> int:
        return max(-1, self.search_rec(nums, target))


# 202208
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target and len(nums) > 2: # search the right part
            right_search = self.search(nums[mid+1:], target)
            if right_search > -1:
                return mid + 1 + right_search
            else:
                return -1
        if nums[mid] > target and len(nums) > 1: # search the left part
            left_search = self.search(nums[:mid], target)
            if left_search > -1:
                return left_search
            else:
                return -1
        else:
            return -1

# 202212
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
			# the above is same as mid = (l + r) // 2 但是可以防止溢出报错
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else: # target == nums[mid]
                return mid
        return -1 
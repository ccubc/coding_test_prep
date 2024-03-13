"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0 or len(nums) == 1 and nums[0] != target:
            return -1
        l, r = 0, len(nums) - 1
        mid = l + (r-l) // 2 # if even numbers, mid in left half
        if nums[mid] == target:
            return mid
        if target == nums[-1]:
            return r
        elif nums[mid] > nums[0]: # left half is sorted
            if nums[0] <= target < nums[mid]:
                return self.search(nums[:mid], target)
            else:
                search_right = self.search(nums[mid+1:], target)
                return search_right + mid + 1 if search_right != -1 else -1
        else: # right half is sorted

            if nums[mid] < target <= nums[-1]:
                search_right = self.search(nums[mid+1:], target)
                return search_right + mid + 1 if search_right != -1 else -1
            else:
                return self.search(nums[:mid], target)


# 20220916
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
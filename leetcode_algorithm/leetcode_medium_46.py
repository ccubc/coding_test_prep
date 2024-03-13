"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        res = []
        
        def backtrack(nums, i):
            if i >= len(nums): # out of boundary/at the end of permutation
                ans = nums.copy()
                res.append(ans)
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(nums, i+1)
                nums[i], nums[j] = nums[j], nums[i]
            return
        
        backtrack(nums, 0) # backtrack(nums, i), i is the next index to permulate
        return res
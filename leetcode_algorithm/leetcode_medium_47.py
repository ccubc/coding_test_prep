"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(nums, i):
            if i >= len(nums): # base case
                ans = nums.copy()
                res.append(ans)
                return
            seen = {}
            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen[nums[j]] = 0
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(nums, i+1)
                nums[i], nums[j] = nums[j], nums[i]
            return
        
        backtrack(nums, 0)
        return res
"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary search solution:
        # helper function split_subarray(nums, X) -- Given list nums and integer X, 
        # return n (the minimum number of subarrays nums needs to be split into), 
        # such that the sum of subarray elements all <= X
        # min(X) = max(nums)
        # max(X) = sum(nums)
        # if n > m --- we needed more splits to achieve X, meaning X is too small (answer is to the right of X)
        # if n <= m --- we might be able to use m splits to achieve a smaller X, meaning X might be too large (answer = X or answer to the left of X)
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            n = Solution.split_subarray(nums, mid)
            if n > m:
                left = mid + 1
            else:
                right = mid
        return left
        
    
    def split_subarray(nums, X):
        cur_sum, i, nums_length, splits = 0, 0, len(nums), 0
        while i < nums_length:
            cur_sum += nums[i]
            if cur_sum > X:
                cur_sum = nums[i]
                splits += 1
            i += 1
        return splits + 1
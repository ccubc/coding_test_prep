"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum, cur_len, l, r, ans = 0, 1, 0, 0, float('inf')
        for r in range(len(nums)):
            cur_sum += nums[r]
            cur_len = r - l + 1
            if cur_sum >= target:
                ans = min(ans, cur_len)
                while l < r and cur_sum >= target:
                    cur_len -= 1
                    cur_sum -= nums[l]
                    l += 1
                    if cur_sum >= target:
                        ans = min(ans, cur_len)
        return ans if ans != float('inf') else 0
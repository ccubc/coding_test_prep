"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.rob_linear(nums[1:]), 
                   self.rob_linear(nums[:-1]),
                  nums[0]) # can not rob 1st and last together because it's a circle, so return the max result of 2 sublists that eliminates 1st and last respectively from the entire list
    
    def rob_linear(self, nums):
        nums = [0]+nums
        dp = nums
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]


# 20220301
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp_w_head, dp_wo_head = [0,0,0], [0,0,0]
        for n in nums:
            dp_w_head.append(max(dp_w_head[-2], dp_w_head[-3])+n)
        for n in nums[1:]:
            dp_wo_head.append(max(dp_wo_head[-2], dp_wo_head[-3])+n)
        # print(dp_w_head)
        # print(dp_wo_head)
        return max(dp_w_head[-2], dp_w_head[-3], dp_wo_head[-1], dp_wo_head[-2])
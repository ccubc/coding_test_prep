"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        # dp[(i,j)]: result of subproblem (i,j)
        
        # dfs: break down problem to what if we pop ith balloon LAST (instead of first)
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            dp[(left, right)] = 0
            for i in range(left, right + 1):
                coins = nums[left-1] * nums[i] * nums[right+1] # when everything else other than nums[i] has been popped
                coins += dfs(left, i-1) # left remaining subarray
                coins += dfs(i+1, right) # right remaining subarray
                dp[(left, right)] = max(dp[(left, right)], coins) # update dp result
            #print(f"left{left}, right{right}, return{dp[(left, right)]}")
            return dp[(left, right)]
        return dfs(1, len(nums) - 2)
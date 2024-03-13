"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            return 0
        pre_take, pre_not_take = cost[0], 0
        for i in range(1, len(cost)):
            cost_take_i = min(pre_take, pre_not_take) + cost[i] # cost if take i
            cost_not_take_i = pre_take # cost if not take i
            pre_take = cost_take_i
            pre_not_take = cost_not_take_i
        return min(cost_take_i, cost_not_take_i)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """The below recursion answer would time out 
        if len(cost) < 2:
            return 0
        return min(cost[0]+self.minCostClimbingStairs(cost[1:]), cost[1]+self.minCostClimbingStairs(cost[2:]))
        """
        # DP solution
        # use a DP to track "min cost if have to step on this stair"
        # start from the end
        
        dp = [0] * len(cost)
        dp[len(cost)-1] = cost[-1]
        dp[len(cost)-2] = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            dp[i]=cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])


# 20220822
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp to track min cost of whether or not stepping on current stair
        dp_step, dp_skip = cost[0], 0
        for i in range(1, len(cost)):
            prev_step, prev_skip = dp_step, dp_skip
            dp_skip = prev_step
            dp_step = min(prev_step, prev_skip) + cost[i]
        return min(dp_skip, dp_step)
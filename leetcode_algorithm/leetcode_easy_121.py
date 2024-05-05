#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:59:57 2019

@author: chengchen

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""



"""
20191117
"""
def maxProfit(prices):
    if (len(prices)==0):
        return 0
    else:
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]< min_price:
                min_price = prices[i]
            if prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit

print(maxProfit([7,6,4,3,1]))
print(maxProfit([7,1,5,3,6,4]))


"""
20200117
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit

"""
20200126
"""           
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        for i in prices:
            min_price = min(i, min_price)
            res = max(res, i - min_price)
        return res


"""
20210115
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min, result = float('inf'), 0
        for i in prices:
            cur_min = min(cur_min, i)
            result = max(i - cur_min, result)
        return result

# 20220206
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur_min = prices[0]
        for i in prices[1:]:
            ans = max(ans, i - cur_min)
            cur_min = min(cur_min, i)
        return ans

# 20220221
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min, cur_ans = 10001, 0
        for i in prices:
            cur_ans = max(i-cur_min, cur_ans)
            cur_min = min(i, cur_min)
        return cur_ans


# 20220809
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        for i in prices:
            low = min(low, i)
            ans = max(ans, i - low)
        return ans

# 20240504
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_min, ans = float('inf'), 0
        for p in prices:
            cur_min = min(cur_min, p)
            ans = max(ans, p-cur_min)
        return ans

            
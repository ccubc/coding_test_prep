"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: # edge case
            return 1 
        if n == 3:
            return 2 # edge case
        dic = {1:1}
        for i in range(2, n + 1):
            dic[i] = 1
            for j in range(1, i//2+1):
                dic[i] = max(dic[i], dic[j]*dic[i-j], i)
        return dic[n]
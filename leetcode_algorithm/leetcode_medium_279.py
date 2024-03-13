"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104

"""

import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        lst = [i**2 for i in range(1, round(math.sqrt(n))+1)] # create a list of perfect square numbers that can be used to sum to n
        counter = 0
        current_level = {n} # set
        while len(current_level) > 0:
            counter += 1
            next_level = set() 
            for i in current_level:
                for j in lst:
                    if i < j:
                        break
                    elif i == j:
                        return counter
                    next_level.add(i-j)
                current_level = next_level


# the DP answer below was OK but exceeded time limit
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10000] * n
        for i in range(n): # i is index, i+1 is value
            if int(math.sqrt(i+1))**2 == i+1:
                dp[i] = 1
            else:
                for ps in range(1, int(math.sqrt(i+1))+1):
                    dp[i] = min(dp[i], dp[ps**2-1]+dp[i-ps**2])
        return dp[-1]
                

# The DP solution below won't time out but is not "that much different"
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]

        
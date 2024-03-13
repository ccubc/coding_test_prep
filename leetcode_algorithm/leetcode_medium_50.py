"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # brute force O(N) will time out
        # to reduce time complexity, x**n would be equal to (x**(n/2))**2 if n is even number, etc.
        # the solution would be O(logN)
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n%2 == 0:
            return self.myPow(self.myPow(x, n//2), 2)
        
        else: 
            return self.myPow(self.myPow(x, n//2), 2) * x
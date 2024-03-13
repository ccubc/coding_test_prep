"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 4:
            return True
        l, r = 1, num // 2
        while l < r - 1:
            mid = l + (r-l+1)//2
            mid_sq = mid*mid
            if mid_sq > num:
                r = mid
            elif mid_sq < num:
                l = mid
            else: # mid_sq == num
                return True
        return False
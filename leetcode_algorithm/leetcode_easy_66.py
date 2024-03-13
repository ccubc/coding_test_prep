com.# -*- coding: utf-8 -*-
"""

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
This is a temporary script file.
"""

# recursion
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            return digits[:-1] + [digits[-1]+1]
        else:
            if len(digits)>1:
                return self.plusOne(digits[:-1]) + [0]
            else: return [1,0]

# iteration
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits.copy()

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                res[i] += 1
                return res
            else:
                res[i] = 0
        if res[0] == 0:
            res = [1] + res
        return res
        
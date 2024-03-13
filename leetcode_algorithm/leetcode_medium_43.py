"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2) # max length of result str
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(l2):
            for j in range(l1):
                multiplication = res[i + j] + int(num2[i]) * int(num1[j])
                res[i + j] = multiplication % 10
                res[i + j + 1] += multiplication // 10
        if res[-1] == 0:
            res.pop()
        return "".join([str(i) for i in res[::-1]])
                
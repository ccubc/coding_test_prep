#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:02:17 2019

@author: chengchen

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

def to_digits(a):
    """ a is a positive integer """
    digits = []
    while a!=0:
        b = a%10
        a = int((a-b)/10)
        digits.append(b)
    return digits

print(to_digits(153))
print(to_digits(1))

digit_list = to_digits(162)
def sum_square_digits(digit_list):
    s = 0
    for i in digit_list:
        s += (i**2)
    return s

print(sum_square_digits(digit_list))

def happy_number(n):
    """ n is a positive integer"""
    dic = {}
    while True:
        if n not in dic:
            dic[n] = 1
            n = sum_square_digits(to_digits(n))
            if n == 1: return True
        else:
            return False
print(happy_number(19))



# 20220904
class Solution:
    def getDigits(self, n):
        res = []
        while n > 0:
            res.append(n % 10)
            n //= 10
        return res
    
    def isHappy(self, n: int) -> bool:
        d = {n:1}
        digits = self.getDigits(n)
        new_n = sum([x**2 for x in digits])
        while new_n not in d and new_n != 1:
            d[new_n] = 1
            digits = self.getDigits(new_n)
            new_n = sum([x**2 for x in digits])
        if new_n == 1:
            return True
        return False



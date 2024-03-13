"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        i = prev_2n = 0
        next_2n = 1 # next number which is 2**n
        ans = [0]
        for j in range(n): # j is index, j+1 would be value
            if j+1 == next_2n:
                prev_2n = next_2n
                next_2n *= 2
                ans.append(1)
            else:
                ans.append(ans[-prev_2n]+1)
        return ans


# 20220227
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        i = 1
        base = 1
        ctr = 0
        while i <= n:
            ans.append(ans[i-base]+1)
            ctr += 1
            i += 1
            if ctr == base:
                base *= 2
                ctr = 0
        return ans


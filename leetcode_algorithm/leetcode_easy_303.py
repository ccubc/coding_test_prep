"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
 

Constraints:

You may assume that the array does not change.
There are many calls to sumRange function.
0 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.l = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.l[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# 20220206: O(N) to initialize, O(1) for the method
class NumArray:

    def __init__(self, nums: List[int]):
        self.acc_sum = [0]
        for i, n in enumerate(nums):
            self.acc_sum.append(self.acc_sum[i] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc_sum[right+1] - self.acc_sum[left]

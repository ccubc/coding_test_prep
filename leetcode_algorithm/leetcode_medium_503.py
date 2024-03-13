"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        stack = []
        res = [-1] * len(nums2)
        for i in range(len(nums2)-1, -1, -1):
            while (len(stack) > 0) and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) == 0 or stack[-1] > nums2[i]:
                stack.append(nums2[i])
            if len(stack) > 1:
                res[i] = stack[-2]
        return res[:len(nums)]
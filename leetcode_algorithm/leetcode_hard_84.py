"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 
Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find the next number smaller than current in array
        # find the previous number smaller than current in array
        # through the above, we could calculate max_width
        # then iterate over index, to get max area of any rectangle that includes the full bar of this index --- this would exhaust all the possibilities
        
        stack_right = []
        heights.append(0) # edge case e.g. [1,1]
        max_width_right = [1] * len(heights)
        res = 0
        for i in range(len(heights)-1, -1, -1):
            while len(stack_right) > 0 and heights[stack_right[-1]] >= heights[i]:
                stack_right.pop()
            if len(stack_right) > 0:
                    max_width_right[i] = stack_right[-1] - i             
            stack_right.append(i)
            
        stack_left = [-1]
        max_width_left = [0] * len(heights)
        for i in range(len(heights)):
            while len(stack_left) > 0 and heights[stack_left[-1]] >= heights[i]:
                stack_left.pop()
            if len(stack_left) > 0:
                max_width_left[i] = i - stack_left[-1] - 1
            stack_left.append(i)
        print(max_width_left)
        print(max_width_right)
        for i, h in enumerate(heights):
            res = max(res, (max_width_right[i] + max_width_left[i])*h)
        return res

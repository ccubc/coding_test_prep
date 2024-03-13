"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Approach 4: Using 2 pointers
Intuition

As in Approach 2, instead of computing the left and right parts seperately, we may think of some way to do it in one iteration. From the figure in dynamic programming approach, notice that as long as \text{right\_max}[i]>\text{left\_max}[i]right_max[i]>left_max[i] (from element 0 to 6), the water trapped depends upon the left_max, and similar is the case when \text{left\_max}[i]>\text{right\_max}[i]left_max[i]>right_max[i] (from element 8 to 11). So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain \text{left\_max}left_max and \text{right\_max}right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

Algorithm

Initialize \text{left}left pointer to 0 and \text{right}right pointer to size-1
While \text{left}< \text{right}left<right, do:
If \text{height[left]}height[left] is smaller than \text{height[right]}height[right]
If \text{height[left]} \geq \text{left\_max}height[left]≥left_max, update \text{left\_max}left_max
Else add \text{left\_max}-\text{height[left]}left_max−height[left] to \text{ans}ans
Add 1 to \text{left}left.
Else
If \text{height[right]} \geq \text{right\_max}height[right]≥right_max, update \text{right\_max}right_max
Else add \text{right\_max}-\text{height[right]}right_max−height[right] to \text{ans}ans
Subtract 1 from \text{right}right.

"""


# 这题好难啊，看solution + 自己画图才搞明白的。
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max, right_max = height[0], height[j]
        ans = 0
        while i < j:
            if height[i] <= height[j]:
                i += 1
                if height[i] > left_max:
                    left_max = height[i]
                else:
                    ans += (left_max - height[i])
            else:
                j -= 1
                if height[j] > right_max:
                    right_max = height[j]
                else:
                    ans += (right_max - height[j])
        return ans


# 这个解法时间也是O(N)，空间是O(N)，这个解法非常非常非常易懂也好写。
class Solution:
    def trap(self, height: List[int]) -> int:
        # for position i, the max amount of rain water that could be trapped is:
        # max(0, min(max_left, max_right)-height[i])
        # max_left is max height of bars to the left of i
        # similarly for max_right
        # getting this clear you've solved 70% of the problem
        
        # O(N), DP, space O(N)
        max_left, max_right, rain = [0]*len(height), [0]*len(height), [0]*len(height)
        # use DP to solve for max_left and max_right
        cur_max_left, cur_max_right = 0, 0
        for i in range(1, len(height)):
            max_left[i] = max(cur_max_left, height[i-1])
            cur_max_left = max_left[i]
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(cur_max_right, height[i+1])
            cur_max_right = max_right[i]
        for i in range(len(height)):
            rain[i] = max(0, min(max_left[i], max_right[i]) - height[i])
        # print(max_left)
        # print(max_right)
        # print(rain)
        return sum(rain)
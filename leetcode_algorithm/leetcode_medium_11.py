"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

# O(N) 思路是先看最胖的，再慢慢找更瘦但更高的。
# 在找更高的同时，寄希望于用更高的替换掉当前的短板，因此当前的矮板不用考虑了。
import numpy as np
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            res = max(res, (j-i)*min(height[j], height[i]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
            
                


# O(Nlog(N)) ugly code that I would not understand tomorrow if I read it myself
# 思路是先看高的，再慢慢找更矮但更胖的
import numpy as np
class Solution:
    def maxArea(self, height: List[int]) -> int:
        idx = np.argsort(height)[::-1]
        right, left = max(idx[0], idx[1]), min(idx[0], idx[1])
        min_height = height[idx[1]]
        res = min_height * (right - left)
        if len(height) == 2: 
            return res
        ct = 2
        right_candidate, left_candidate = max(idx[0], idx[1]), min(idx[0], idx[1])
        #print(f"current largest is left {left}, right {right}, height {height[1]}")
        for i in idx[2:]:
            ct += 1
            #print(f"inspect {ct} largest number, which is {height[i]}")
            if i > right:
                compare = height[i] * (i-left)
                if compare > res:
                    #print(f"current largest is left {left}, right {i}, height {height[i]}")
                    res = compare
                    right = i
                else:
                    right_candidate = i
                compare = height[i] * (i-left_candidate)
                if compare > res:
                    res = compare
                    right = i
                    left = left_candidate
            elif i < left:
                compare = height[i] * (right - i)
                if compare > res:
                    #print(f"current largest is left {i}, right {right}, height {height[i]}")
                    res = compare
                    left = i
                else:
                    left_candidate = i
                compare = height[i] * (right_candidate - i)
                if compare > res:
                    res = compare
                    right = right_candidate
                    left = i
        return res




# brute force one-liner, time limit exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        return max([(j-i)*min(height[i], height[j]) for i in range(len(height)) for j in range(i+1, len(height))])


# 20220223
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, l, r = 0, 0, len(height)-1
        while l < r:
            ans = max(ans, (r-l)*min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
                

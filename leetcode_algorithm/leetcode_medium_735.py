"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack: all asteroid surviving so far
        stack = [asteroids[0]] # push the 1st asteroid into stack (it's ok even if it's <- / negative)
        for i, a in enumerate(asteroids[1:]):
            if a > 0: # push the -> (positive) asteroids into stack
                stack.append(a)
            else:
                while (len(stack) > 0) and (stack[-1] > 0) and (stack[-1] < -a):
                    stack.pop()
                if (len(stack) > 0) and (stack[-1] == -a):
                    stack.pop()
                elif (len(stack) == 0) or (stack[-1] < 0):
                    stack.append(a)
        return stack
                
            
"""
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
 

Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example 
Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true
 

Constraints:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106
"""


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        seen = set()
        def dfs(tot):
            if tot == targetCapacity:
                return True
            if tot > jug1Capacity + jug2Capacity or tot in seen or tot < 0:
                return False
            seen.add(tot)
            return dfs(tot + jug1Capacity) or dfs(tot - jug1Capacity) or dfs(tot + jug2Capacity) or dfs(tot - jug2Capacity)
        return dfs(0)


# 20230402 BFS solution
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # BFS solution
        queue = [0]
        seen = set()
        seen.add(0)
        while queue:
            cur = queue.pop(0)
            for tot in [cur+jug1Capacity, cur-jug1Capacity, cur+jug2Capacity, cur-jug2Capacity]:
                if tot == targetCapacity:
                    return True
                if 0 < tot < jug1Capacity+jug2Capacity and tot not in seen:
                    seen.add(tot)
                    queue.append(tot)
        return False
"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def mergeKEmp(self, schedule):
        # return list of intervals
        n = len(schedule)
        if n <= 2:
            return self.merge2Emp(schedule)
        return self.merge2Emp([self.mergeKEmp(schedule[:n//2])]+[self.mergeKEmp(schedule[n//2:])])
    
    
    def merge2Emp(self, schedule):
        # input [[Interval], [Interval]]
        # return [Interval]
        if not schedule:
            return []
        if len(schedule) == 1:
            return schedule[0]
        # case that len(schedule) = 2
        m, n = len(schedule[0]), len(schedule[1])
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if schedule[0][i].end < schedule[1][j].start:
                res.append(schedule[0][i])
                i += 1
            elif schedule[0][i].start > schedule[1][j].end:
                res.append(schedule[1][j])
                j += 1
            elif schedule[1][j].start <= schedule[0][i].start < schedule[0][i].end <= schedule[1][j].end:
                i += 1
            elif schedule[0][i].start <= schedule[1][j].start < schedule[1][j].end <= schedule[0][i].end:
                j += 1
            elif schedule[0][i].start < schedule[1][j].start:
                schedule[1][j].start = schedule[0][i].start
                i += 1
            else:
                schedule[0][i].start = schedule[1][j].start
                j += 1
        if i < m:
            res += schedule[0][i:]
        if j < n:
            res += schedule[1][j:]
        return res
    
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        merged_intervals = self.mergeKEmp(schedule)
        res = []
        for i in range(len(merged_intervals)-1):
            res.append(Interval(start=merged_intervals[i].end,
                               end=merged_intervals[i+1].start))
        return res


# beautiful solution
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([i for e in schedule for i in e], key = lambda x:x.start)
        res, end = [], intervals[0].end
        for i in intervals[1:]:
            if i.start > end:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res
    
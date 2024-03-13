"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals using the left value
        intervals.sort(key = lambda x: x[0])
        res = []        
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval doesn't overlap with previous, then append the current interval
            if (not res) or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # otherwise, there is overlap, so we update the result to merge the overlapping intervals
                res[-1][1] = max(res[-1][1], interval[1])
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals using their left boundry
        intervals.sort(key = lambda x:x[0])
        ans = []
        for i in intervals:
            if len(ans) == 0 or i[0] > ans[-1][1]:
                ans.append(i)
            elif i[0] <= ans[-1][1] < i[1]:
                ans[-1][1] = i[1]
        return ans

# 20220318
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by their starting value
        def takeFirst(l):
            return l[0]
        intervals.sort(key=takeFirst)
        res = []
        i = 0
        while i < len(intervals):
            s, e = intervals[i][0], intervals[i][1]
            while i < len(intervals) - 1 and intervals[i+1][0] <= e:
                e = max(e, intervals[i+1][1])
                i += 1
            res.append([s, e])
            i += 1
        return res

# 20220417
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        cur = intervals[0]
        for i in intervals[1:]:
            if i[0] > cur[1]:
                res.append(cur)
                cur = i
            else:
                # i[0] <= cur[1], i.e. the two intervals need to be merged
                cur[1] = max(i[1], cur[1])
        res.append(cur)
        return res

# 20230117
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) # sort with starting position of intervals
        ans = []
        cur = intervals[0]
        i = 1
        while i < len(intervals):
            if cur[1] >= intervals[i][0]:
                cur[1] = max(cur[1], intervals[i][1])
            else:
                ans.append(cur)
                cur = intervals[i]
            i += 1
        ans.append(cur)
        return ans

# 20231001
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.sort(key=lambda x: x[0])
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[i][1]) # made a mistake here and forgot using max() 
            else:
                ans.append(cur)
                cur = intervals[i]
        ans.append(cur)
        return ans

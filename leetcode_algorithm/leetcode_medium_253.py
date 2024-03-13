"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

# naive approach
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        max_overlap = 1
        for i in range(1, len(intervals)):
            overlap = 1
            for j in range(i):
                if intervals[j][1] > intervals[i][0]:
                    overlap += 1
            max_overlap = max(max_overlap, overlap)
        return max_overlap

# using a MinHeap
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        rooms = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] < heap[0]:
                rooms += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return rooms
                

# 20231012
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        intervals.sort(key = lambda x: x[0])
        for i in intervals:
            if len(heap)==0 or heap[0] > i[0]:
                heapq.heappush(heap, i[1])
            else:
                pop = heapq.heappop(heap)
                heapq.heappush(heap, max(pop, i[1]))
        return len(heap)
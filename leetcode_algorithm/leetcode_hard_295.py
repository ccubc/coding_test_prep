"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
"""


import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] # maintain a MaxHeap for the smaller half of the array
        self.large = [] # maintain a MinHeap for the larger half of the array
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # would increase self.large size by 1 and keep the self.small at the same size
            # can not push into self.large directly, but need to push into self.small and pop from self.small and push that popped item into self.large
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
            
        else: 
            # self.large has 1 more element then self.small
            # would increase self.small size by 1 and keep the self.large at the same size
            # can not push into self.small directly, but need to push into self.large and pop from self.large and push that popped item into self.small
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
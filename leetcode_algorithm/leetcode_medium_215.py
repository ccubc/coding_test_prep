"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""


# method 1: Sort and select: Time complexity O(NlogN), space complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# method 2: quicksort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quicksort(nums)[-k]
    
    
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left_list, right_list = [], []
            for i in nums[1:]:
                if i <= pivot:
                    left_list.append(i)
                else:
                    right_list.append(i)
            return self.quicksort(left_list) + [pivot] + self.quicksort(right_list)


# method 3: quicksort in place
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums)[-k]
    
    
    def quickSort(self, x):
        if len(x) <= 1:
            return x
        else:
            pivot = self.partition(x)
            return self.quickSort(x[:pivot]) + [x[pivot]] + self.quickSort(x[pivot+1:])
    
    
    def partition(self, x):
        pivot = 0
        pt = 1
        right_p = len(x)-1
        while pt <= right_p:
            if x[pivot] <= x[pt]:
                x[pt], x[right_p] = x[right_p], x[pt]
                right_p -= 1
            else:
                x[pt], x[pivot] = x[pivot], x[pt]
                pivot += 1
                pt += 1
        return pivot


# 20220314: Using a min heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # priority queue and heap
        heap = nums[:k]
        heapq.heapify(heap) # a size-K MinHeap
        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappush(heap, i)
                heapq.heappop(heap)
        return heap[0]
        

# 20230113
from heapq import heapify, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapify(h)
        for n in nums[k:]:
            if n > h[0]:
                heappushpop(h, n)
        return h[0]
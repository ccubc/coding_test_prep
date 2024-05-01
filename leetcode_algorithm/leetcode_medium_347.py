"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N) to count frequency
        cnt = Counter(nums)
        cnt_vals = list(cnt.values())
        
        # initialize a size-k min heap
        h = cnt_vals[:k]
        heapq.heapify(h)
        # push and pop if next element has greater value than current heap root
        for i in cnt_vals[k:]:
            if i > h[0]:
                heapq.heappush(h, i)
                heapq.heappop(h)
        ans = []
        for i in cnt:
            if cnt[i] in h:
                ans.append(i)
        return ans


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        heap = heapq.nsmallest(k, ct.items(), lambda x:-x[1])
        return [x[0] for x in heap]


# 20230113
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = [(-freq, num) for num, freq in c.items()]
        heapify(h)
        return [heappop(h)[1] for _ in range(k)]


from collections import Counter
from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = nlargest(k, c.items(), key=lambda x:x[1])
        return [i[0] for i in h]


# 20231007
from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct = Counter(nums)
        hp = []
        heapq.heapify(hp)
        n = 0
        for key, v in ct.items():
            heapq.heappush(hp, [v, key])
            n += 1
            if n > k:
                heapq.heappop(hp)
        return [x[1] for x in hp]

# 20240430
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        h = []
        heapq.heapify(h)
        # push all the (value, key) pair into a max-heap
        # note that python heapq is implemented as a min heap
        for key, ct in c.items():
            heapq.heappush(h, (-ct, key))
        output = []
        for _ in range(k):
            output.append(heapq.heappop(h)[1])
        return output
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) find min and max of the array

        d = {} # so that lookup takes O(1)
        for i in nums:
            d[i] = 1
        
        def dfs(i):
            if i not in d:
                return 0
            del d[i]
            return 1 + dfs(i-1) + dfs(i+1)
        
        ans = 0
        for n in nums:
            ans = max(ans, dfs(n))

        return ans

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_max_dict = {}
        ans = 0
        for i in nums:
            if i in min_max_dict:
                # seen
                continue
            min_max_dict[i] = [i, i]

            if i-1 in min_max_dict:
                # e.g. cur number is 4, we saw 3 has been seen before
                # extend consecutive number range
                min_max_dict[i][0] = min_max_dict[i-1][0]
                # update min_max_dict[i-1][0]'s right boundary
                min_max_dict[min_max_dict[i-1][0]][1] = min_max_dict[i][1]

            if i+1 in min_max_dict:
                # e.g. cur number is 4, we saw 5 has been seen before
                # extend consecutive number range
                min_max_dict[i][1] = min_max_dict[i+1][1]
                # update min_max_dict[i+1][1]'s left boundary
                min_max_dict[min_max_dict[i+1][1]][0] = min_max_dict[i][0]
            
                if i-1 in min_max_dict:
                    # update the left ends's limits again
                    min_max_dict[min_max_dict[i-1][0]][1] = min_max_dict[i+1][1]
        return max([v[1]-v[0] for v in min_max_dict.values()])+1
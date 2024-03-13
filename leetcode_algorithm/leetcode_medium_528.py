"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.
"""


import numpy as np
class Solution:

    def __init__(self, w: List[int]):
        self.runningSum = []
        curSum = 0
        for i in w:
            curSum += i
            self.runningSum.append(curSum)


    def search(self, target, array):
        # binary search; return the index of the largest num in array that's <= target
        l, r = 0, len(array) - 1
        while l < r:
            mid = l + (r-l)//2
            if target <= array[mid]:
                r = mid
            else:
                l = mid + 1
        return l


    def pickIndex(self) -> int:
        pick = np.random.random_integers(self.runningSum[-1])
        return self.search(pick, self.runningSum)

        # the code below will TLE (but it works)
        # for i, s in enumerate(self.runningSum):
        #     if pick <= s:
        #         return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# 20230930
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        running_sum_w = [w[0]]
        for i in range(1, len(w)):
            running_sum_w.append(running_sum_w[i-1] + w[i])
        self.running_sum_w = running_sum_w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        rdm = random.randint(1, self.running_sum_w[-1])
        return find_idx_min_greater_than(self.running_sum_w, rdm)

def find_idx_min_greater_than(num_list, tgt):
    # brute_force
    # if method == 'bf':
    #     for i, n in enumerate(num_list):
    #         if n >= tgt:
    #             return i

    # binary search
    l, r = 0, len(num_list) - 1
    while l < r - 1:
        mid = l + (r - l + 1) // 2
        if num_list[mid] == tgt:
            return mid
        elif num_list[mid] < tgt:
            l = mid
        else:
            r = mid
    if num_list[l] < tgt:
        return r
    else:
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
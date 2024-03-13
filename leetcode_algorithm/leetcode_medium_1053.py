"""
Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]). If it cannot be done, then return the same array.

 

Example 1:

Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 104
"""


from collections import defaultdict
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # look from the right
        d = defaultdict(int) # store left most index of seen number
        d[arr[-1]] = -1
        for i in range(2, len(arr)+1):
            candidates = [j for j in d.keys() if j < arr[-i]]
            if len(candidates) > 0:
                max_right_part = max(candidates)
                arr[-i], arr[d[max_right_part]] = arr[d[max_right_part]], arr[-i]
                return arr
            else:
                d[arr[-i]] = -i
        return arr


# 省一点空间但思路类似的做法：
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # look from the right
        # look for an i where A[i] > A[i+1] -- this is a necessary condition that answer exists
        i = len(arr) - 2
        while i > -1 and arr[i] <= arr[i+1]:
            i -= 1
        if i > -1: # means we found such i exists in arr
            max_right_idx = i + 1
            for j in range(i + 2, len(arr)):
                if arr[max_right_idx] < arr[j] < arr[i]:
                    max_right_idx = j
            arr[i], arr[max_right_idx] = arr[max_right_idx], arr[i]
        return arr

        
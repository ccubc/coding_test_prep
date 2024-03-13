Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # hmm so it needs to use techniques including both DP and Binary search
        
        # first you need to calc prefix sum of all [i,j] combinations in the matrix
        # then any submatrix (left_up, right_up, left_bottom, right_bottom)'s sum could be calculated as:
        # prefix_sum(right_bottom) - prefix_sum(left_bottom) - prefix_sum(right_up) + prefix_sum(left_up)
        
        # max_side_length of a sub-matrix could be the answer to the whole matrix
        # we could keep updating max_side_length
        
        # for i in rows, for j in cols, within the submatrix of ([0,0], [0,j], [i,0], [i,j]):
        # find max_side_length and update answer
        
        # how binary search would fit in
        # 每次遍历(i,j)组合时，通过BS找到满足条件的max_side_length
        # 这里的inner loop，本来需要遍历以(i,j)为右下角的各种side_length可能性，内圈O(min(i,j))
        # 但是可以用binary search不必遍历每一个side_length了，内圈O(log(min(i,j)))
        
        msl = 0 # initialize max side length
        height, width = len(mat), len(mat[0])
        dp = [[0]*(width+1) for _ in range(height+1)] # initialize DP matrix, with 0th row and 0th col
        for i in range(1, height+1):
            for j in range(1, width+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
                left = 1
                right = min(i, j)
                while left < right:
                    mid = left + (right - left + 1)//2
                    sum_square_mid = dp[i][j] - dp[i-mid][j] - dp[i][j-mid] + dp[i-mid][j-mid]
                    if sum_square_mid > threshold: # this square (hence mid) is too big, ans < mid
                        right = mid - 1
                    else:
                        left = mid
                        msl = max(msl, left)
        return msl    
                
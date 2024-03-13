"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        up, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        while (bottom - up > 0) and (right - left > 0):
            ans += self.skirtTraverse([[matrix[i][j] for j in range(left, right)] for i in range(up, bottom)])
            up += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans
        
    
    def skirtTraverse(self, matrix):
        # len(matrix) must be positive
        # len(matrix[0]) must also be positive
        ans = []
        # traverse upper boundary
        i = 0
        for j in range(len(matrix[0])):
            ans.append(matrix[i][j])
        # traverse right boundary
        j = len(matrix[0]) - 1
        for i in range(1, len(matrix)):
            ans.append(matrix[i][j])
        # traverse lower boundary
        i = len(matrix) - 1
        if i > 0:
            for j in range(len(matrix[0])-2, -1, -1):
                ans.append(matrix[i][j])
        # traverse left boundary
        if len(matrix[0]) > 1:
            j = 0
            for i in range(len(matrix)-2, 0, -1):
                ans.append(matrix[i][j])
        return ans
    
# 20220904
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, u = 0, 0
        r, d = len(matrix[0]) - 1, len(matrix) - 1
        res = []
        row, col = 0, 0
        while l <= r and u <= d:
            while col <= r:
                res.append(matrix[row][col])
                col += 1
            col -= 1
            row += 1
            u += 1
            while row <= d and l <= r and u <= d:
                res.append(matrix[row][col])
                row += 1
            row -= 1
            col -= 1
            r -= 1
            while col >= l and l <= r and u <= d:
                res.append(matrix[row][col])
                col -= 1
            col += 1
            row -= 1
            d -= 1
            while row >= u and l <= r and u <= d:
                res.append(matrix[row][col])
                row -= 1
            row += 1
            col += 1
            l += 1
        return res
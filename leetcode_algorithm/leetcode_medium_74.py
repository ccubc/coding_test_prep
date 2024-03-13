"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p, q = 0, len(matrix) - 1
        if matrix[p][0] == target: 
            return True
        while p < q:
            mid = (p + q + 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                p = mid
            else:
                q = mid - 1
        nums = matrix[p]
        p, q = 0, len(nums) - 1
        while p < q:
            mid = (p + q + 1) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                p = mid
            else:
                q = mid - 1
        return False
        
            
                
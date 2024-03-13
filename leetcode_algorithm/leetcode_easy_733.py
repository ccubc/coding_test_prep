"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        return self.dfs(image, sr, sc, newColor, image[sr][sc])
    
    def dfs(self, image, sr, sc, newColor, oldColor):
        if image[sr][sc]!=oldColor:
            return
        else:
            image[sr][sc] = newColor
            if sr > 0:
                self.dfs(image, sr-1, sc, newColor, oldColor)
            if sr < len(image)-1:
                self.dfs(image, sr+1, sc, newColor, oldColor)
            if sc > 0:
                self.dfs(image, sr, sc-1, newColor, oldColor)
            if sc < len(image[0]) -1:
                self.dfs(image, sr, sc+1, newColor, oldColor)
        return image
            
# 20220817
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        queue = [[sr, sc]]
        old_color = image[sr][sc]
        image[sr][sc] = color
        while queue:
            cur_pixel = queue.pop(0)
            for d in [[0,1],[0,-1],[1,0],[-1,0]]:
                neigh = [cur_pixel[0]+d[0], cur_pixel[1]+d[1]]
                if 0 <= neigh[0] < len(image) and 0 <=neigh[1] < len(image[0]) and image[neigh[0]][neigh[1]] == old_color:
                    image[neigh[0]][neigh[1]] = color
                    queue.append(neigh)
        return image
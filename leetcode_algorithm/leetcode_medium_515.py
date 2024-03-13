"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        res = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            cur_level = []
            cur_level_len = len(queue)
            for i in range(cur_level_len):
                cur_node = queue.pop(0)
                cur_level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(max(cur_level))
        return res
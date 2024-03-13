"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        elif root.left and not root.right:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right) + 1


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # level order traversal
        res = 0
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            res += 1
            cur_level_len = len(queue)
            for i in range(cur_level_len):
                cur_node = queue.pop(0)
                if (not cur_node.left) and (not cur_node.right):
                    return res
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return res
            
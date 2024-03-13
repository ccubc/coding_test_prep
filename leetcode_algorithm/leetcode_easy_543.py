"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_depth(root):
    """return max depth of a tree"""
    if root == None:
        return 0
    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(max_depth(root.left) + max_depth(root.right),  
                   self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))

# 20220913
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def getHeight(root):
            if not root:
                return (-1, -1)
            l, r = max(getHeight(root.left)) + 1, max(getHeight(root.right)) + 1
            self.res = max(self.res, l + r)
            return (l, r)
        getHeight(root)
        return self.res
            
"""Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildSubTree(lower, upper):
            nonlocal idx
            # idx is index of preorder list
            if idx == len(preorder):
                return None
                # meaning we've put all the nodes into the tree, the last node has both children as None
            cur = preorder[idx]
            if cur < lower or cur > upper:
                return None
                # meaning preorder[idx] is not a child / subtree of the currently built tree
            root = TreeNode(cur)
            idx += 1
            root.left = buildSubTree(lower, cur)
            root.right = buildSubTree(cur, upper)
            return root
        idx = 0
        return buildSubTree(float("-inf"), float("inf"))

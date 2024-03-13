"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
 

Accepted
218,820
Submissions
496,482
Seen this question in a real interview before?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def areSame(self, t, s):
        if (not t) and (not s):
            return True
        elif t and s:
            return (t.val==s.val) and self.areSame(t.left, s.left) and self.areSame(t.right, s.right)
        else:
            return False
    
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.areSame(s, t):
            return True
        elif not s:
            return False
        else:            
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
        
# 20220324
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root1, root2):
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if not root1 and not root2:
            return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            else:
                return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        
        
        
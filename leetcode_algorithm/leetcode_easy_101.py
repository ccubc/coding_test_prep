#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:49:41 2020

@author: chengchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
class Solution:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False



        
class Solution:
    def isSymmetric(self, root):
        # level order traversal (BFS)
        queue = [root]
        while len(queue) > 0:
            cur_level_len = len(queue)
            cur_level = []
            for i in range(cur_level_len):
                if queue[0]:
                    cur_node = queue.pop(0)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
                    cur_level.append(cur_node.val)
                else:
                    queue.pop(0)
                    cur_level.append(101)
            i, j = 0, len(cur_level) - 1
            while i < j:
                if cur_level[i] != cur_level[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True


# 20221004
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left, root.right)
    
    
    def mirror(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            return root1.val == root2.val and self.mirror(root1.left, root2.right) and self.mirror(root1.right, root2.left)
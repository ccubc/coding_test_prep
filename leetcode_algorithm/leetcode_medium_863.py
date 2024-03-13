"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        edges = defaultdict(list)
        
        def tree_to_graph(root):
            if not root:
                return
            if root.left:
                edges[root.val].append(root.left.val)
                edges[root.left.val].append(root.val)
                tree_to_graph(root.left)
            if root.right:
                edges[root.val].append(root.right.val)
                edges[root.right.val].append(root.val)
                tree_to_graph(root.right)
        
        tree_to_graph(root)
        
        queue = [target.val]
        for _ in range(k):
            len_queue = len(queue)
            for _ in range(len_queue):
                cur_node = queue.pop(0)
                for i in edges[cur_node]:
                    queue.append(i)
                    edges[i].remove(cur_node)
        return queue
                
            
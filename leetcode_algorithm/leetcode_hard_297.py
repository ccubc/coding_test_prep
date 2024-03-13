"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        l = []
        while queue:
            cur_level = len(queue)
            if not any(queue):
                break
            for _ in range(cur_level):
                cur_node = queue.pop(0)
                if not cur_node:
                    l.append('n')
                else:
                    l.append(cur_node.val)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    else:
                        queue.append(False)
                    if cur_node.right:
                        queue.append(cur_node.right)
                    else:
                        queue.append(False)
        return '$'.join(str(i) for i in l)
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if data == "":
            return None
        d = {}
        l = data.split('$')
        for i, n in enumerate(l):
            if n == 'n':
                d[i] = None
            else:
                d[i] = TreeNode(int(n))
        pt_c = 1
        for pt_p, node in enumerate(l):
            if node != 'n' and pt_c in d:
                d[pt_p].left = d[pt_c]
                pt_c += 1
                d[pt_p].right = d[pt_c]
                pt_c += 1
        return d[0]
    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



# below answer would TLE; it best suits complete binary tree but will take too much space for very deep and non-complete tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        l = []
        while queue:
            cur_level = len(queue)
            if not any(queue): # we're below the bottom level
                break
            for _ in range(cur_level):
                cur_node = queue.pop(0)
                if not cur_node:
                    l.append('n')
                    queue += [False, False]
                else:
                    l.append(cur_node.val)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    else:
                        queue.append(False)
                    if cur_node.right:
                        queue.append(cur_node.right)
                    else:
                        queue.append(False)
        return '$'.join(str(i) for i in l)
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        if data == "":
            return None
        d = {}
        l = data.split('$')
        for i in range(len(l)-1, -1, -1):
            self.createNode(l, i, d)
        return d[0]
    
    
    def createNode(self, l, i, d):
        if l[i] == 'n':
            d[i] = None
        else:
            node = TreeNode(int(l[i]))
            if 2*i + 1 in d:
                node.left = d[2*i+1]
                node.right = d[2*i+2]
            d[i] = node
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
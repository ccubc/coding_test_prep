"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]



Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""

class Solution(object):
    # 2 pointers + recursion
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count) # this will result in two separated linked list
        head.next = self.reverseKGroup(new_head, k) # head is the tail of the reversed part of the linked list, so this step connects the two linked lists
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, None
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev) # cur is the head of the next part of the linked list (the new head), prev is the head of the reversed part of the linked list
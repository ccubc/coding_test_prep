"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first find the (n//2+1)th of the linked list and reverse the right half of the linked list
        pt1 = pt2 = head
        while pt2 and pt2.next:
            pt1 = pt1.next
            pt2 = pt2.next.next
        cur = pt1.next
        pt1.next = None
        pre = None
        while cur:
            next_ = cur.next
            cur.next = pre
            pre, cur = cur, next_
        # pre would be the head of the reversed right half of the original linked list
        # re-combine the two partial linkedlist
        cur = head
        while pre:
            tmp_l, tmp_r = cur.next, pre.next
            cur.next = pre
            pre.next = tmp_l
            cur = tmp_l
            pre = tmp_r
        


# 20240323
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # slow would be the end of 1st half

        second_half_head = slow.next
        
        # cut off left part from right part
        slow.next = None

        # reverse the right part
        cur, prev = second_half_head, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        # prev will be head of reversed right part

        # merge left part and reversed right part
        right_head = prev
        cur = head
        while right_head:
            tmp = cur.next
            cur.next = right_head
            right_head = right_head.next
            cur = cur.next
            cur.next = tmp
            cur = cur.next    
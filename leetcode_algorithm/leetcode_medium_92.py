"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # recursion
        while left < right:
            idx = 1
            pt_1 = head
            pt1_prev = None
            while idx < left:
                pt1_prev = pt_1
                pt_1 = pt_1.next
                idx += 1
            
            pt2_prev = pt1_prev
            pt_2 = pt_1
            while idx < right:
                pt2_prev = pt_2
                pt_2 = pt_2.next
                idx += 1
            if left == right - 1:
                if pt1_prev:
                    pt1_prev.next = pt_2
                else:
                    head = pt_2
                pt_1.next = pt_2.next
                pt_2.next = pt_1
            else:    
                pt1_next = pt_1.next
                pt2_next = pt_2.next
                if pt1_prev:
                    pt1_prev.next = pt_2
                else:
                    head = pt_2
                pt2_prev.next = pt_1
                pt_2.next = pt1_next
                pt_1.next = pt2_next
            return self.reverseBetween(head, left + 1, right - 1)
        return head
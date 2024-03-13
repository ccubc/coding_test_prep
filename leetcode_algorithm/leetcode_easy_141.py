"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pt = head
        while pt:
            if pt.val == "visited":
                return True
            else:
                pt.val = "visited"
                pt = pt.next
        return False


# Two pointers
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1, p2 = head, head
        while p2 and p2.next and p2.next.next:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                return True
        return False

# 20220321
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head and head.val != 'v':
            head.val = 'v'
            head = head.next
        if not head:
            return False
        return True
            
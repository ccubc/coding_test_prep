"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = {}
        pos = 0
        pad_head = ListNode(0, head)
        node = pad_head
        while node:
            d[pos] = node
            node = node.next
            pos += 1
        if n > 1:
            d[pos-n-1].next = d[pos-n+1]
        else:
            d[pos-n-1].next = None
        return pad_head.next

# 别人的解法，有点厉害。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
            
# 20220321
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt1 = pt2 = head
        pre = dummy = ListNode()
        dummy.next = head
        for _ in range(n):
            pt2 = pt2.next
        while pt2:
            pt2 = pt2.next
            pre = pt1
            pt1 = pt1.next
        pre.next = pt1.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pt1 = pt2 = dummy
        for _ in range(n):
            pt2 = pt2.next
        while pt2.next:
            pt2 = pt2.next
            pt1 = pt1.next
        pt1.next = pt1.next.next
        return dummy.next
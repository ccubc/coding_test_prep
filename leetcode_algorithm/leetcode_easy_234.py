"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l =[]
        while head:
            l.append(head.val)
            head = head.next
        i, j = 0, len(l)-1
        while i < j:
            if l[i]==l[j]:
                i+=1
                j-=1
            else:
                return False
        return true

# 20220907
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        i, j = 0, len(vals) - 1
        while i < j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        # reverse 2nd half
        dummy = None
        pre, cur = dummy, p1
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        # compare
        tail = pre
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
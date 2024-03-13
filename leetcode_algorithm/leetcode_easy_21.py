#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:30:37 2019

@author: chengchen

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

l1 = [1,2,4,5,7,8,10]
l2 = [1,3,4,9]

def solution(l1, l2):
    l3 = []
    while l1 and l2:
        if l1[0]<=l2[0]:
            l3.append(l1.pop(0))
        else: 
            l3.append(l2.pop(0))
    while l1:
        l3.append(l1.pop(0))
    while l2:
        l3.append(l2.pop(0))
    return l3

print(solution(l1,l2))


# Using LinkedList

class ListNode:
    def __init__(self, x): 
        self.val = x
        self.next = None
l1_node = ListNode(1)
l1_node2 = ListNode(3)
l1_node.next = l1_node2
l1_node3 = ListNode(5)
l1_node2.next = l1_node3
print(l1_node.next.val)
l1_node.next.val
l2_node = ListNode(2)
l2_node2 = ListNode(4)
l2_node3 = ListNode(6)
l2_node.next= l2_node2
l2_node2.next = l2_node3

def mergeTwoLists(l1, l2):
    head = ListNode(-1)
    current = head
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    if l2: 
        current.next = l2
    return head.next


solution_linked_list = mergeTwoLists(l1_node, l2_node)

# 20220315
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pt = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                pt.next = list1
                list1 = list1.next
                pt = pt.next
            else:
                pt.next = list2
                list2 = list2.next
                pt = pt.next
        if list1:
            pt.next = list1
        if list2:
            pt.next = list2
        return dummy.next


# 20220806
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pt = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                pt.next = list1
                list1 = list1.next
            else:
                pt.next = list2
                list2 = list2.next
            pt = pt.next
        if list1:
            pt.next = list1
        if list2:
            pt.next = list2
        return dummy.next
        
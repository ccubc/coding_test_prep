"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        d = defaultdict(list)
        h = []
        non_empty_lists = list(range(len(lists)))
        head = pt = ListNode()
        
        for i, l in enumerate(lists):
            if l:
                d[l.val].append(i)
                h.append(l.val)
            else:
                non_empty_lists.remove(i)
                
        heapq.heapify(h) # heapify h as MinHeap
        while non_empty_lists:
            cur_min = heapq.heappop(h)
            i = d[cur_min][0]
            pt.next = lists[i]
            pt = pt.next
            d[cur_min].pop(0)
            if not lists[i].next:
                non_empty_lists.remove(i)
                continue
            lists[i] = lists[i].next
            heapq.heappush(h, lists[i].val)
            d[lists[i].val].append(i)
        return head.next


# 20220318
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 2:
            return self.merge2Lists(lists[0], lists[1])
        if l == 1:
            return lists[0]
        if l == 0:
            return None
        return self.merge2Lists(self.mergeKLists(lists[:l//2]), self.mergeKLists(lists[l//2:]))
    
    
    def merge2Lists(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
            
                
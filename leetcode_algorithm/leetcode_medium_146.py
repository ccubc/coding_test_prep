"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
Accepted
979,666
Submissions
2,500,542
"""


# a dictionary to store key: pointer to Node (key, val, prev, next), where Node is part of a double linked list
# removing a node, insert node at an end, lookup all happen in O(1)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = Node(0, 0) # least recent unit, make it the left most node in the double linked list
        self.mru = Node(0, 0) # most recent unit, make it the right most node in the double linked list
        self.lru.next, self.mru.prev = self.mru, self.lru # link lru and mru nodes
        self.cache = {}
        
        
    def remove(self, key):
        # remove node from DLL
        cur = self.cache[key]
        prev, nxt = cur.prev, cur.next
        prev.next, nxt.prev = nxt, prev
        
        
    def insert(self, node):
        # insert node into DLL at the right (prev to mru node)
        prev = self.mru.prev
        nxt = self.mru
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        new_node = Node(key, value)
        self.cache[key]= new_node
        self.insert(new_node)
        if len(self.cache) > self.cap: # if after the insertion, size of cache is larger than cap
            deque_node = self.lru.next
            self.remove(deque_node.key)
            del self.cache[deque_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""


class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []


    def push(self, x: int) -> None:
        while self.stack_pop:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(x)

    def pop(self) -> int:
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()
        

    def peek(self) -> int:
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]
        

    def empty(self) -> bool:
        return not self.stack_pop+self.stack_push
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# optimized version: 不用每次push都倒腾一遍
class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []


    def push(self, x: int) -> None:
        # while self.stack_pop:
        #     self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(x)

    def pop(self) -> int:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()
        

    def peek(self) -> int:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]
        

    def empty(self) -> bool:
        return not self.stack_pop+self.stack_push
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
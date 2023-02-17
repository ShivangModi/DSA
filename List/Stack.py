# Stacks and Queues are dynamic sets in which the element removed from the set by the Delete Operation is prescribed.
# In a Stack, the element deleted from the set is the most recently inserted: the stack implements a last-in,first-out or LIFO.
# Similarly, in a queue, the element deleted is always the one that has been in the set for the longest time: the queue implements a first-in, first-out or FIFO.

# Stack:-
# The INSERT operation on a stack is often called PUSH, and the DELETE operation, which does not take an element argument, is often called POP.
# These names are allusions to physical stacks, such as the spring-load stacks of plates used in cafeterias. 
# The order in which plates are popped from the stack is the reverse of the order in which they were pushed onto the stack, since only the top plate is accessible.
# Upon an attempt to top an empty stack, the stack underflow's, which is normally an error.
# If top exceeds size, the stack overflows.
# Each of the three stack operations takes O(1) time.
class Stack:
    def __init__(self):
        self.__size = 10 ** 5
        self.__data = [None]*self.__size
        self.__top = 0
    
    def isEmpty(self):
        return self.__top == 0
    
    def isFull(self):
        return self.__top == self.__size

    def push(self, x):
        if self.isFull():
            print("Overflow")
            return
        self.__data[self.__top] = x
        self.__top += 1

    def pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            self.__top -= 1
            res = self.__data[self.__top]
            self.__data[self.__top] = None
            return res
    
    def peek(self):
        if self.isEmpty():
            print('Underflow')
        else:
            return self.__data[self.__top-1]

    def len(self):
        return self.__top

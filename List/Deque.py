# Double-Ended Queue:-
# Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

# Operations on Deque:- 
# Mainly the following four basic operations are performed on queue:
#   - enqueueFront(): Adds an item at the front of Deque.
#   - enqueueRear(): Adds an item at the rear of Deque.
#   - dequeueFront(): Deletes an item from the front of Deque.
#   - dequeueRear(): Deletes an item from the rear of Deque. In addition to the above operations, the following operations are also supported.
#   - getFront(): Gets the front item from the queue.
#   - getRear(): Gets the last item from queue.
#   - isEmpty(): Checks whether Deque is empty or not.
#   - isFull(): Checks whether Deque is full or not.

# Applications of Deque:- 
# Since Deque supports both stack and queue operations, it can be used as both. 
# The Deque data structure supports clockwise and anticlockwise rotations in O(1) time which can be useful in certain applications. 
# Also, the problems where elements need to be removed and or added to both ends can be efficiently solved using Deque. 
# For example see the Maximum of all subarrays of size k problem., 0-1 BFS, and Find the first circular tour that visits all petrol pumps. 
# Example of the A-Steal job scheduling algorithm where Deque is used as deletions operation is required at both ends. 

# Some Practical Applications of Deque:
#   - Applied as both stack and queue, as it supports both operations.
#   - Storing a web browser’s history.
#   - Storing a software application’s list of undo operations.
#   - Job scheduling algorithm

# Implementation:- 
# A Deque can be implemented either using a doubly-linked list or a circular array. 
# In both implementations, we can implement all operations in O(1) time. 
class Deque:
    def __init__(self, size):
        self.__front = -1
        self.__rear = -1
        self.__size = size
        self.__data = [None] * 10**5
    
    def isEmpty(self):
        return self.__front == -1
    
    def isFull(self):
        return (self.__front == 0 and self.__rear == self.__size-1) or self.__front == self.__rear+1
    
    def enqueueFront(self, val):
        if self.isFull():
            print("Overflow")
            return
        
        if self.isEmpty():
            self.__front = 0
            self.__rear = 0
        elif self.__front == 0:
            self.__front = self.__size - 1
        else:
            self.__front -= 1
        self.__data[self.__front] = val

    def enqueueRear(self, val):
        if self.isFull():
            print("Overflow")
            return
        
        if self.isEmpty():
            self.__front = 0
            self.__rear = 0
        elif self.__rear == self.__size-1:
            self.__rear = 0
        else:
            self.__rear += 1
        self.__data[self.__rear] = val

    def dequeueFront(self):
        if self.isEmpty():
            print("Underflow")
            return
        if self.__front == self.__rear:
            self.__front = -1
            self.__rear = -1
        elif self.__front == self.__size-1:
            self.__front = 0
        else:
            self.__front += 1

    def dequeueRear(self):
        if self.isEmpty():
            print("Underflow")
            return
        
        if self.__front == self.__rear:
            self.__front = -1
            self.__rear = -1
        elif self.__rear == 0:
            self.__rear = self.__size-1
        else:
            self.__rear -= 1

    def getFront(self):
        if self.isEmpty():
            print("Underflow")
            return
        print(self.__data[self.__front])

    def getRear(self):
        if self.isEmpty():
            print("Underflow")
            return
        print(self.__data[self.__rear])


if __name__ == "__main__":
    dq =Deque(5)
    dq.enqueueFront(1)
    dq.enqueueRear(2)
    dq.enqueueFront(3)
    dq.enqueueRear(4)
    dq.enqueueFront(5)
    dq.enqueueRear(6)
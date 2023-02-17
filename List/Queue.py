# Stacks and Queues are dynamic sets in which the element removed from the set by the Delete Operation is prescribed.
# In a Stack, the element deleted from the set is the most recently inserted: the stack implements a last-in,first-out or LIFO.
# Similarly, in a queue, the element deleted is always the one that has been in the set for the longest time: the queue implements a first-in, first-out or FIFO.

# Queue:-
# We call the INSERT operation on a queue ENQUEUE, and we call the DELETE operaation DEQUEUE.
# Like the stack operation POP, DEQUEUE takes no element argument.
# The FIFO property of a queue causes it to operate like a line of customers waiting for service.
# The queue has a head and tail. 
# When an element is enqueued, it takes its place at the tail of the queue, just as a newly arriving customer takes a place at the end of the line.
# An element dequeued is always the one at the head of the queue, like customer at the head of the line, who has waited the longest.
# An attempt to dequeue an element from an empty queue causes the queue to underflow.
# When head=tail+1 or both head-1 and tail=size, the queue is full and an attempt to enqueue an element causes the queue to overflow.
# Each operation takes O(1) time.
class Queue:
    def __init__(self):
        self.__size = 10 ** 5
        self.__data = [None]*self.__size
        self.__front = self.__rear = 0
    
    def isEmpty(self):
        return self.__front == self.__rear
    
    def isFull(self):
        return self.__rear == self.__size

    def enqueue(self, x):
        if self.isFull():
            print("Overflow")
            return
        self.__data[self.__rear] = x
        self.__rear += 1

    def dequeue(self):
        if self.isEmpty():
            self.__front = self.__rear = 0
            print("Underflow")
        else:
            # O(n) time
            # res = self.__data[self.__front]
            # self.__rear -= 1
            # for i in range(self.__rear):
            #     self.__data[i] = self.__data[i+1]
            # return res
            
            # O(1) Time
            res = self.__data[self.__front]
            self.__data[self.__front] = None
            self.__front += 1
            return res
    
    def peek(self):
        if self.isEmpty():
            print('Underflow')
        else:
            return self.__data[self.__front]

    def len(self):
        return self.__rear - self.__front

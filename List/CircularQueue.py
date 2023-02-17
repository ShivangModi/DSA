# Circular Queue:-
# A Circular Queue is a special version of queue where the last element of the queue is connected to the first element of the queue forming a circle.
# The operations are performed based on FIFO (First In First Out) principle. It is also called ‘Ring Buffer’. 
# In a normal Queue, we can insert elements until queue becomes full. But once queue becomes full, we can not insert the next element even if there is a space in front of queue.

# Operation on Circular Queue:
#   Front: Get the front item from queue.
#   Rear: Get the last item from queue.
#   enQueue(value): This function is used to insert an element into the circular queue. In a circular queue, the new element is always inserted at Rear position. 
#       1. Check whether queue is Full – Check ((rear == SIZE-1 && front == 0) || (rear == front-1)).
#       2. If it is full then display Queue is full. If queue is not full then, check if (rear == SIZE – 1 && front != 0) if it is true then set rear=0 and insert element.
#   deQueue(): This function is used to delete an element from the circular queue. In a circular queue, the element is always deleted from front position. 
#       1. Check whether queue is Empty means check (front==-1).
#       2. If it is empty then display Queue is empty. If queue is not empty then step 3
#       3. Check if (front==rear) if it is true then set front=rear= -1 else check if (front==size-1), if it is true then set front=0 and return the element.

class CircularQueue:
    def __init__(self):
        self.__size = 10 ** 5
        self.__data = [None]*self.__size
        self.__front = self.__rear = -1
    
    def isEmpty(self):
        return self.__front == -1
    
    def isFull(self):
        return self.__front == 0 and self.__rear == self.__size-1 or self.__front == self.__rear+1

    def enqueue(self, data):
        if self.isFull():
            print("Overflow")
            return

        if self.isEmpty():
            self.__front = 0
        self.__rear = (self.__rear+1)%self.__size
        self.__data[self.__rear] = data

    def dequeue(self):
        if self.isEmpty():
            return "Underflow"
        else:
            temp = self.__data[self.__front]
            if self.__front == self.__rear:
                self.__front = self.__rear = -1
            else:
                self.__front = (self.__front+1)%self.__size
            return temp
    
    def peek(self):
        if self.isEmpty():
            print('Underflow')
        else:
            return self.__data[self.__front]

    def display(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            i = self.__front
            while i != self.__rear:
                print(self.__data[i], end=' ')
                i = (i+1)%self.__size
            print(self.__data[i])

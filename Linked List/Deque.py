# Operation on Deque:
#   insertFront() : Adds an item at the front of Deque.
#   insertRear()  : Adds an item at the rear of Deque.
#   deleteFront() : Deletes an item from front of Deque.
#   deleteRear()  : Deletes an item from rear of Deque.
#   getFront() : Gets the front item from queue.
#   getRear()  : Gets the last item from queue.
#   isEmpty()  : Checks whether Deque is empty or not.
#   size()     : Gets number of elements in Deque.
#   erase()    : Deletes all the elements from Deque.

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.__front = self.__rear = None
        self.__size = 0
    
    def isEmpty(self):
        return self.__front is None
    
    def insertFront(self, data):
        new = Node(data)
        if self.isEmpty():
            self.__front = self.__rear = new
            return
        
        new.next = self.__front
        self.__front.prev = new
        self.__front = new
        self.__size += 1

    def insertRear(self, data):
        new = Node(data)
        if self.isEmpty():
            self.__front = self.__rear = new
            return
        
        new.prev = self.__rear
        self.__rear.next = new
        self.__rear = new
        self.__size += 1

    def deleteFront(self):
        if self.isEmpty():
            print("Underflow")
        
        temp = self.__front
        self.__front = self.__front.next
        if self.__front is None:
            self.__rear = None
        else:
            self.__front.prev = None
        del temp
        self.__size -= 1

    def deleteRear(self):
        if self.isEmpty():
            print("Underflow")
        
        temp = self.__rear
        self.__rear = self.__rear.prev
        if self.__rear is None:
            self.__front = None
        else:
            self.__rear.next = None
        del temp
        self.__size -= 1

    def size(self):
        return self.__size
    
    def getFront(self):
        if self.isEmpty():
            print("Empty")
        else:
            print(self.__front.data)
    
    def getRear(self):
        if self.isEmpty():
            print("Empty")
        else:
            print(self.__rear.data)
    
    def erase(self):
        self.__rear = None
        while self.__front:
            temp = self.__front
            self.__front = self.__front.next
            del temp
        self.__size = 0